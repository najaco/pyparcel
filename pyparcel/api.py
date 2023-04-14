import struct
from typing import TypeVar, Tuple, Any, Callable, Dict, List

from .architecture import Architecture

T = TypeVar("T")


def raise_(ex):
    raise ex


X86_ARCHITECTURE: Architecture = Architecture()


def generate_pack_with_architecture(
    arc: Architecture = X86_ARCHITECTURE,
) -> Callable[[Any], bytes]:
    pack_dict: Dict[type, Callable[[Any], bytes]] = {
        int: (lambda obj: struct.pack(arc.format_of(int), obj)),
        bool: (lambda obj: struct.pack(arc.format_of(bool), obj)),
        float: (lambda obj: struct.pack(arc.format_of(float), obj)),
        bytes: (
            lambda obj: struct.pack(
                "i" + arc.format_of(bytes).format(len(obj)), len(obj), obj
            )
        ),
        str: (
            lambda obj: struct.pack(
                "i" + arc.format_of(str).format(len(obj)),
                len(obj),
                obj.encode(arc.encoding),
            )
        ),
        list: (lambda obj: b"".join([_pack(x) for x in vars(obj)])),
        set: (lambda obj: raise_(NotImplementedError)),
        dict: (lambda obj: raise_(NotImplementedError)),
        tuple: (lambda obj: _pack(*obj)),
    }

    def _pack(*objs: Any) -> bytes:
        return b"".join(
            [
                pack_dict.get(
                    type(obj),
                    lambda o: b"".join([_pack(o.__getattribute__(x)) for x in vars(o)]),
                )(obj)
                for obj in objs
            ]
        )

    return _pack


def generate_unpack_with_architecture(
    arc: Architecture = X86_ARCHITECTURE,
) -> Callable[[bytes, Any], Tuple[Any, ...]]:
    unpack_dict: Dict[type, Callable[[T, bytes], T]] = {
        int: (
            lambda _, data: (
                struct.unpack("i", data[: arc.size_of(int)])[0],
                data[arc.size_of(int) :],
            )
        ),
        bool: (
            lambda _, data: (
                struct.unpack("?", data[: arc.size_of(bool)])[0],
                data[arc.size_of(bool) :],
            )
        ),
        float: (
            lambda _, data: (
                struct.unpack("f", data[: arc.size_of(float)])[0],
                data[arc.size_of(float) :],
            )
        ),
        bytes: (lambda _, data: unpack_bytes(data)),
        str: (lambda _, data: unpack_string(data)),
        list: (lambda obj, _: raise_(NotImplementedError)),
        set: (lambda obj, _: raise_(NotImplementedError)),
        dict: (lambda obj, _: raise_(NotImplementedError)),
        tuple: (lambda obj, data: unpack_tuple(data, obj)),
    }

    def unpack_string(data: bytes) -> (str, bytes):
        result, data = unpack_bytes(data)
        return result.decode(arc.encoding), data

    def unpack_bytes(data: bytes) -> (bytes, bytes):
        length = struct.unpack(
            arc.format_of("str_length"), data[: arc.size_of("str_length")]
        )[0]
        data = data[arc.size_of("str_length") :]
        return (
            struct.unpack(arc.format_of(bytes).format(length), data[:length])[0],
            data[length:],
        )

    def unpack_tuple(data: bytes, t: Tuple[Any]) -> (Tuple[Any], bytes):
        unpacked_objs: List[Any] = []
        for obj in t:
            (result, data) = _unpack_helper(data, obj)
            unpacked_objs.append(result)
        return tuple(unpacked_objs), data

    def _unpack_helper(data: bytes, obj: T) -> (T, bytes):
        if type(obj) in unpack_dict:
            return unpack_dict[type(obj)](obj, data)
        else:
            for v in vars(obj):
                (result, data) = _unpack_helper(data, obj.__getattribute__(v))
                obj.__dict__[v] = result
        return obj, data

    def _unpack(data: bytes, *objs: Any) -> Tuple[Any]:
        if len(objs) == 0:
            raise TypeError("unpack() takes a variable number of objects")
        if len(objs) == 1:
            return _unpack_helper(data, objs[0])[0]
        else:
            unpacked_objs: List[Any] = []
            for obj in objs:
                (result, data) = _unpack_helper(data, obj)
                unpacked_objs.append(result)
            return tuple(unpacked_objs)

    return _unpack


pack: Callable[[Any], bytes] = generate_pack_with_architecture()
unpack: Callable[[bytes, Any], Tuple[Any, ...]] = generate_unpack_with_architecture()

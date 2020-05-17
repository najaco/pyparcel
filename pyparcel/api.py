from typing import Generic, List, TypeVar, Tuple, Any
import struct

T = TypeVar("T")
INT_MAX = (1 << 31) - 1
INT_MIN = -1 << 31
ENCODING = "utf-8"


def raise_(ex):
    raise ex


size_dict = {
    int: 4,
    bool: 1,
    float: 4,
    "str_length": 8,
}
# find a way to set default size for int
pack_dict = {
    int: (
        lambda obj: struct.pack("i", obj)
    ),  # if INT_MIN <= obj <= INT_MAX else pack("q", obj)),
    bool: (lambda obj: struct.pack("?", obj)),
    float: (lambda obj: struct.pack("f", obj)),
    bytes: (lambda obj: struct.pack("q{}s".format(len(obj)), len(obj), obj)),
    str: (
        lambda obj: struct.pack("q{}s".format(len(obj)), len(obj), obj.encode(ENCODING))
    ),
    list: (lambda obj: b"".join([pack(x) for x in vars(obj)])),
    set: (lambda obj: raise_(NotImplementedError)),
    dict: (lambda obj: raise_(NotImplementedError)),
    tuple: (lambda obj: pack(*obj)),
}

unpack_dict = {
    int: (
        lambda _, data: (
            struct.unpack("i", data[: size_dict[int]])[0],
            data[size_dict[int]:],
        )
    ),
    bool: (
        lambda _, data: (
            struct.unpack("?", data[: size_dict[bool]])[0],
            data[size_dict[bool]:],
        )
    ),
    float: (
        lambda _, data: (
            struct.unpack("f", data[: size_dict[float]])[0],
            data[size_dict[float]:],
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
    return result.decode(ENCODING), data


def unpack_bytes(data: bytes) -> (bytes, bytes):
    length = struct.unpack("q", data[: size_dict["str_length"]])[0]
    data = data[size_dict["str_length"]:]
    return struct.unpack("{}s".format(length), data[:length])[0], data[length:]


def unpack_tuple(data: bytes, t: Tuple[Any]) -> (Tuple[Any], bytes):
    unpacked_objs = []
    for obj in t:
        (result, data) = _unpack(data, obj)
        unpacked_objs.append(result)
    return tuple(unpacked_objs), data


def pack(*objs) -> bytes:
    return b"".join(
        [
            pack_dict.get(
                type(obj),
                lambda o: b"".join([pack(o.__getattribute__(x)) for x in vars(o)]),
            )(obj)
            for obj in objs
        ]
    )


def _unpack(data: bytes, obj: T) -> (T, bytes):
    if type(obj) in unpack_dict:
        return unpack_dict[type(obj)](obj, data)
    else:
        for v in vars(obj):
            (result, data) = _unpack(data, obj.__getattribute__(v))
            obj.__dict__[v] = result
    return obj, data


def unpack(data: bytes, *objs) -> Tuple[Any]:
    if len(objs) == 0:
        raise TypeError("unpack() takes a variable number of objects")
    if len(objs) == 1:
        return _unpack(data, objs[0])[0]
    else:
        unpacked_objs = []
        for obj in objs:
            (result, data) = _unpack(data, obj)
            unpacked_objs.append(result)
        return tuple(unpacked_objs)

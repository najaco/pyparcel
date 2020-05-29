# pyparcel

[![Build Status](https://travis-ci.org/najaco/pyparcel.svg?branch=master)](https://travis-ci.org/najaco/pyparcel)

pyparcel is the simple and secure way to convert python objects to [`bytestrings`](https://docs.python.org/3/library/stdtypes.html#bytes). pyparcel extends the usage of [`struct`](https://docs.python.org/3/library/struct.html) and provides a simpler way to pack classes and [built-in types](https://docs.python.org/3/library/stdtypes.html).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyparcel:

```bash
pip install pyparcel
```
or using [pipenv](https://pipenv.pypa.io/en/latest/):
```bash
pipenv install pyparcel
```

## Usage

```python
import pyparcel

foo: Foo = Foo(8, 5.7, "Hello World") # Foo(int, float, str)
data: bytes = pyparcel.pack(foo) # b'\x08\x00\x00\x00ff\xb6@\x0b\x00\x00\x00Hello World'

# ...

bar: Foo = Foo()
pyparcel.unpack(data, bar) # foo == bar
# or
baz: Foo = pyparcel.unpack(data, Foo()) # foo == baz

```

## Contributing
This repository follows a "fork-and-pull" workflow. If you would like to contribute perform the following:
1. **Fork** the repostiory to your Github.
2. **Clone** your fork to your local machine.
3. **Checkout** a new branch with a meaningful name.
4. **Commit** your changes to your fork.
5. **Submit a pull request** with a description of changes and enhancements made for further review.

Check out some issues to work on in the [*issues*](https://github.com/najaco/pyparcel/issues) section.

## Documentation is available at [https://najaco.github.io/pyparcel/](https://najaco.github.io/pyparcel/)

## License
[MIT](https://choosealicense.com/licenses/mit/)



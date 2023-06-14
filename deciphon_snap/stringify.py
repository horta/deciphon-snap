from typing import Union

__all__ = ["stringify"]


def stringify(x: Union[bytes, str]):
    if isinstance(x, bytes):
        return x.decode()
    return x

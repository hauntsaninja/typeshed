from types import TracebackType
from typing import List, Optional, Type, TypeVar, Union, overload

_T = TypeVar("_T")
_KeyType = str | bytes
_ValueType = str | bytes

class error(OSError): ...

library: str = ...

# Actual typename dbm, not exposed by the implementation
class _dbm:
    def close(self) -> None: ...
    def __getitem__(self, item: _KeyType) -> bytes: ...
    def __setitem__(self, key: _KeyType, value: _ValueType) -> None: ...
    def __delitem__(self, key: _KeyType) -> None: ...
    def __len__(self) -> int: ...
    def __del__(self) -> None: ...
    def __enter__(self) -> _dbm: ...
    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    @overload
    def get(self, k: _KeyType) -> bytes | None: ...
    @overload
    def get(self, k: _KeyType, default: bytes | _T) -> bytes | _T: ...
    def keys(self) -> List[bytes]: ...
    def setdefault(self, k: _KeyType, default: _ValueType = ...) -> bytes: ...
    # Don't exist at runtime
    __new__: None  # type: ignore
    __init__: None  # type: ignore

def open(__filename: str, __flags: str = ..., __mode: int = ...) -> _dbm: ...

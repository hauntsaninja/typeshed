import io
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import IO, Any, Iterable, List, Text, TypeVar
from typing_extensions import SupportsIndex

_PathOrFile = Text | IO[bytes]
_T = TypeVar("_T")

def compress(data: bytes, compresslevel: int = ...) -> bytes: ...
def decompress(data: bytes) -> bytes: ...

class BZ2File(io.BufferedIOBase, IO[bytes]):
    def __enter__(self: _T) -> _T: ...
    def __init__(
        self, filename: _PathOrFile, mode: str = ..., buffering: Any | None = ..., compresslevel: int = ...
    ) -> None: ...
    def read(self, size: int | None = ...) -> bytes: ...
    def read1(self, size: int = ...) -> bytes: ...
    def readline(self, size: SupportsIndex = ...) -> bytes: ...  # type: ignore
    def readinto(self, b: WriteableBuffer) -> int: ...
    def readlines(self, size: SupportsIndex = ...) -> List[bytes]: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...
    def write(self, data: ReadableBuffer) -> int: ...
    def writelines(self, seq: Iterable[ReadableBuffer]) -> None: ...

class BZ2Compressor(object):
    def __init__(self, compresslevel: int = ...) -> None: ...
    def compress(self, __data: bytes) -> bytes: ...
    def flush(self) -> bytes: ...

class BZ2Decompressor(object):
    def decompress(self, data: bytes) -> bytes: ...
    @property
    def unused_data(self) -> bytes: ...

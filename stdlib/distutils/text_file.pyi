from typing import IO, List, Optional, Tuple, Union

class TextFile:
    def __init__(
        self,
        filename: str | None = ...,
        file: Optional[IO[str]] = ...,
        *,
        strip_comments: bool = ...,
        lstrip_ws: bool = ...,
        rstrip_ws: bool = ...,
        skip_blanks: bool = ...,
        join_lines: bool = ...,
        collapse_join: bool = ...,
    ) -> None: ...
    def open(self, filename: str) -> None: ...
    def close(self) -> None: ...
    def warn(self, msg: str, line: Optional[List[int] | Tuple[int, int] | int] = ...) -> None: ...
    def readline(self) -> str | None: ...
    def readlines(self) -> List[str]: ...
    def unreadline(self, line: str) -> str: ...

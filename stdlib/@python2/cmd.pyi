from typing import IO, Any, Callable, List, Optional, Tuple

class Cmd:
    prompt: str
    identchars: str
    ruler: str
    lastcmd: str
    intro: Any | None
    doc_leader: str
    doc_header: str
    misc_header: str
    undoc_header: str
    nohelp: str
    use_rawinput: bool
    stdin: IO[str]
    stdout: IO[str]
    cmdqueue: List[str]
    completekey: str
    def __init__(self, completekey: str = ..., stdin: IO[str] | None = ..., stdout: IO[str] | None = ...) -> None: ...
    old_completer: Optional[Callable[[str, int], str | None]]
    def cmdloop(self, intro: Any | None = ...) -> None: ...
    def precmd(self, line: str) -> str: ...
    def postcmd(self, stop: bool, line: str) -> bool: ...
    def preloop(self) -> None: ...
    def postloop(self) -> None: ...
    def parseline(self, line: str) -> Tuple[str | None, str | None, str]: ...
    def onecmd(self, line: str) -> bool: ...
    def emptyline(self) -> bool: ...
    def default(self, line: str) -> bool: ...
    def completedefault(self, *ignored: Any) -> List[str]: ...
    def completenames(self, text: str, *ignored: Any) -> List[str]: ...
    completion_matches: List[str] | None
    def complete(self, text: str, state: int) -> List[str] | None: ...
    def get_names(self) -> List[str]: ...
    # Only the first element of args matters.
    def complete_help(self, *args: Any) -> List[str]: ...
    def do_help(self, arg: str) -> bool | None: ...
    def print_topics(self, header: str, cmds: List[str] | None, cmdlen: Any, maxcol: int) -> None: ...
    def columnize(self, list: List[str] | None, displaywidth: int = ...) -> None: ...

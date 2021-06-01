from typing import Any, Dict, Optional

class Completer:
    def __init__(self, namespace: Optional[Dict[str, Any]] = ...) -> None: ...
    def complete(self, text: str, state: int) -> str | None: ...

import threading
from typing import Any, Optional

SUBDEBUG: Any
SUBWARNING: Any

def sub_debug(msg, *args): ...
def debug(msg, *args): ...
def info(msg, *args): ...
def sub_warning(msg, *args): ...
def get_logger(): ...
def log_to_stderr(level: Any | None = ...): ...
def get_temp_dir(): ...
def register_after_fork(obj, func): ...

class Finalize:
    def __init__(self, obj, callback, args=..., kwargs: Any | None = ..., exitpriority: Any | None = ...): ...
    def __call__(self, wr: Any | None = ...): ...
    def cancel(self): ...
    def still_active(self): ...

def is_exiting(): ...

class ForkAwareThreadLock:
    def __init__(self): ...

class ForkAwareLocal(threading.local):
    def __init__(self): ...
    def __reduce__(self): ...

from types import CodeType, ModuleType
from typing import Optional, Union

class ZipImportError(ImportError): ...

class zipimporter(object):
    archive: str
    prefix: str
    def __init__(self, path: str | bytes) -> None: ...
    def find_module(self, fullname: str, path: str | None = ...) -> zipimporter | None: ...
    def get_code(self, fullname: str) -> CodeType: ...
    def get_data(self, pathname: str) -> str: ...
    def get_filename(self, fullname: str) -> str: ...
    def get_source(self, fullname: str) -> str | None: ...
    def is_package(self, fullname: str) -> bool: ...
    def load_module(self, fullname: str) -> ModuleType: ...

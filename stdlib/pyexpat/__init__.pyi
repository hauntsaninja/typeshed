import pyexpat.errors as errors
import pyexpat.model as model
from _typeshed import SupportsRead
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

EXPAT_VERSION: str  # undocumented
version_info: Tuple[int, int, int]  # undocumented
native_encoding: str  # undocumented
features: List[Tuple[str, int]]  # undocumented

class ExpatError(Exception):
    code: int
    lineno: int
    offset: int

error = ExpatError

XML_PARAM_ENTITY_PARSING_NEVER: int
XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE: int
XML_PARAM_ENTITY_PARSING_ALWAYS: int

_Model = Tuple[int, int, str | None, Tuple[Any, ...]]

class XMLParserType(object):
    def Parse(self, __data: str | bytes, __isfinal: bool = ...) -> int: ...
    def ParseFile(self, __file: SupportsRead[bytes]) -> int: ...
    def SetBase(self, __base: str) -> None: ...
    def GetBase(self) -> str | None: ...
    def GetInputContext(self) -> bytes | None: ...
    def ExternalEntityParserCreate(self, __context: str | None, __encoding: str = ...) -> XMLParserType: ...
    def SetParamEntityParsing(self, __flag: int) -> int: ...
    def UseForeignDTD(self, __flag: bool = ...) -> None: ...
    buffer_size: int
    buffer_text: bool
    buffer_used: int
    namespace_prefixes: bool  # undocumented
    ordered_attributes: bool
    specified_attributes: bool
    ErrorByteIndex: int
    ErrorCode: int
    ErrorColumnNumber: int
    ErrorLineNumber: int
    CurrentByteIndex: int
    CurrentColumnNumber: int
    CurrentLineNumber: int
    XmlDeclHandler: Optional[Callable[[str, str | None, int], Any]]
    StartDoctypeDeclHandler: Optional[Callable[[str, str | None, str | None, bool], Any]]
    EndDoctypeDeclHandler: Optional[Callable[[], Any]]
    ElementDeclHandler: Optional[Callable[[str, _Model], Any]]
    AttlistDeclHandler: Optional[Callable[[str, str, str, str | None, bool], Any]]
    StartElementHandler: Optional[
        Union[
            Callable[[str, Dict[str, str]], Any],
            Callable[[str, List[str]], Any],
            Callable[[str, Union[Dict[str, str]], List[str]], Any],
        ]
    ]
    EndElementHandler: Optional[Callable[[str], Any]]
    ProcessingInstructionHandler: Optional[Callable[[str, str], Any]]
    CharacterDataHandler: Optional[Callable[[str], Any]]
    UnparsedEntityDeclHandler: Optional[Callable[[str, str | None, str, str | None, str], Any]]
    EntityDeclHandler: Optional[Callable[[str, bool, str | None, str | None, str, str | None, str | None], Any]]
    NotationDeclHandler: Optional[Callable[[str, str | None, str, str | None], Any]]
    StartNamespaceDeclHandler: Optional[Callable[[str, str], Any]]
    EndNamespaceDeclHandler: Optional[Callable[[str], Any]]
    CommentHandler: Optional[Callable[[str], Any]]
    StartCdataSectionHandler: Optional[Callable[[], Any]]
    EndCdataSectionHandler: Optional[Callable[[], Any]]
    DefaultHandler: Optional[Callable[[str], Any]]
    DefaultHandlerExpand: Optional[Callable[[str], Any]]
    NotStandaloneHandler: Optional[Callable[[], int]]
    ExternalEntityRefHandler: Optional[Callable[[str, str | None, str | None, str | None], int]]

def ErrorString(__code: int) -> str: ...

# intern is undocumented
def ParserCreate(
    encoding: str | None = ..., namespace_separator: str | None = ..., intern: Dict[str, Any] | None = ...
) -> XMLParserType: ...

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GraphDebugInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FileLineCol(google.protobuf.message.Message):
        """This represents a file/line location in the source code."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FILE_INDEX_FIELD_NUMBER: builtins.int
        LINE_FIELD_NUMBER: builtins.int
        COL_FIELD_NUMBER: builtins.int
        FUNC_FIELD_NUMBER: builtins.int
        CODE_FIELD_NUMBER: builtins.int
        file_index: builtins.int
        """File name index, which can be used to retrieve the file name string from
        `files`. The value should be between 0 and (len(files)-1)
        """
        line: builtins.int
        """Line number in the file."""
        col: builtins.int
        """Col number in the file line."""
        func: builtins.str
        """Name of function contains the file line."""
        code: builtins.str
        """Source code contained in this file line."""
        def __init__(
            self,
            *,
            file_index: builtins.int | None = ...,
            line: builtins.int | None = ...,
            col: builtins.int | None = ...,
            func: builtins.str | None = ...,
            code: builtins.str | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing.Literal[
                "code", b"code", "col", b"col", "file_index", b"file_index", "func", b"func", "line", b"line"
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing.Literal[
                "code", b"code", "col", b"col", "file_index", b"file_index", "func", b"func", "line", b"line"
            ],
        ) -> None: ...

    @typing.final
    class StackTrace(google.protobuf.message.Message):
        """This represents a stack trace which is a ordered list of `FileLineCol`."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FILE_LINE_COLS_FIELD_NUMBER: builtins.int
        FRAME_ID_FIELD_NUMBER: builtins.int
        @property
        def file_line_cols(
            self,
        ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GraphDebugInfo.FileLineCol]:
            """Deprecated."""

        @property
        def frame_id(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        def __init__(
            self,
            *,
            file_line_cols: collections.abc.Iterable[global___GraphDebugInfo.FileLineCol] | None = ...,
            frame_id: collections.abc.Iterable[builtins.int] | None = ...,
        ) -> None: ...
        def ClearField(
            self, field_name: typing.Literal["file_line_cols", b"file_line_cols", "frame_id", b"frame_id"]
        ) -> None: ...

    @typing.final
    class FramesByIdEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___GraphDebugInfo.FileLineCol: ...
        def __init__(
            self, *, key: builtins.int | None = ..., value: global___GraphDebugInfo.FileLineCol | None = ...
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class TracesByIdEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int
        @property
        def value(self) -> global___GraphDebugInfo.StackTrace: ...
        def __init__(self, *, key: builtins.int | None = ..., value: global___GraphDebugInfo.StackTrace | None = ...) -> None: ...
        def HasField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class TracesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___GraphDebugInfo.StackTrace: ...
        def __init__(self, *, key: builtins.str | None = ..., value: global___GraphDebugInfo.StackTrace | None = ...) -> None: ...
        def HasField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing.final
    class NameToTraceIdEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.int
        def __init__(self, *, key: builtins.str | None = ..., value: builtins.int | None = ...) -> None: ...
        def HasField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FILES_FIELD_NUMBER: builtins.int
    FRAMES_BY_ID_FIELD_NUMBER: builtins.int
    TRACES_BY_ID_FIELD_NUMBER: builtins.int
    TRACES_FIELD_NUMBER: builtins.int
    NAME_TO_TRACE_ID_FIELD_NUMBER: builtins.int
    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """This stores all the source code file names and can be indexed by the
        `file_index`.
        """

    @property
    def frames_by_id(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___GraphDebugInfo.FileLineCol]:
        """Stack traces and frames are uniqueified during construction. These maps
        index from the unique id for a frame/trace to the value.
        """

    @property
    def traces_by_id(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___GraphDebugInfo.StackTrace]: ...
    @property
    def traces(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___GraphDebugInfo.StackTrace]:
        """Deprecated."""

    @property
    def name_to_trace_id(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.int]:
        """This maps a node name to a trace id contained in `traces_by_id`.

        The map key is a mangling of the containing function and op name with
        syntax:
          op.name '@' func_name
        For ops in the top-level graph, the func_name is the empty string and hence
        the `@` may be ommitted.
        Note that op names are restricted to a small number of characters which
        exclude '@', making it impossible to collide keys of this form. Function
        names accept a much wider set of characters.
        It would be preferable to avoid mangling and use a tuple key of (op.name,
        func_name), but this is not supported with protocol buffers.
        """

    def __init__(
        self,
        *,
        files: collections.abc.Iterable[builtins.str] | None = ...,
        frames_by_id: collections.abc.Mapping[builtins.int, global___GraphDebugInfo.FileLineCol] | None = ...,
        traces_by_id: collections.abc.Mapping[builtins.int, global___GraphDebugInfo.StackTrace] | None = ...,
        traces: collections.abc.Mapping[builtins.str, global___GraphDebugInfo.StackTrace] | None = ...,
        name_to_trace_id: collections.abc.Mapping[builtins.str, builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "files",
            b"files",
            "frames_by_id",
            b"frames_by_id",
            "name_to_trace_id",
            b"name_to_trace_id",
            "traces",
            b"traces",
            "traces_by_id",
            b"traces_by_id",
        ],
    ) -> None: ...

global___GraphDebugInfo = GraphDebugInfo

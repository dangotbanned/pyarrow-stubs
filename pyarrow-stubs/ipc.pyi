from io import IOBase

import pandas as pd
import pyarrow.lib as lib

from pyarrow.lib import (
    IpcReadOptions,
    IpcWriteOptions,
    Message,
    MessageReader,
    MetadataVersion,
    ReadStats,
    RecordBatchReader,
    WriteStats,
    _ReadPandasMixin,
    get_record_batch_size,
    get_tensor_size,
    read_message,
    read_record_batch,
    read_schema,
    read_tensor,
    write_tensor,
)

class RecordBatchStreamReader(lib._RecordBatchStreamReader):
    def __init__(
        self,
        source: bytes | lib.Buffer | lib.NativeFile | IOBase,
        *,
        options: IpcReadOptions | None = None,
        memory_pool: lib.MemoryPool | None = None,
    ) -> None: ...

class RecordBatchStreamWriter(lib._RecordBatchStreamWriter):
    def __init__(
        self,
        sink: str | lib.NativeFile | IOBase,
        schema: lib.Schema,
        *,
        use_legacy_format: bool | None = None,
        options: IpcWriteOptions | None = None,
    ) -> None: ...

class RecordBatchFileReader(lib._RecordBatchFileReader):
    def __init__(
        self,
        source: bytes | lib.Buffer | lib.NativeFile | IOBase,
        footer_offset: int | None = None,
        *,
        options: IpcReadOptions | None,
        memory_pool: lib.MemoryPool | None = None,
    ) -> None: ...

class RecordBatchFileWriter(lib._RecordBatchFileWriter):
    def __init__(
        self,
        sink: str | lib.NativeFile | IOBase,
        schema: lib.Schema,
        *,
        use_legacy_format: bool | None = None,
        options: IpcWriteOptions | None = None,
    ) -> None: ...

def new_stream(
    sink: str | lib.NativeFile | IOBase,
    schema: lib.Schema,
    *,
    use_legacy_format: bool | None = None,
    options: IpcWriteOptions | None = None,
) -> RecordBatchStreamWriter: ...
def open_stream(
    source: bytes | lib.Buffer | lib.NativeFile | IOBase,
    *,
    options: IpcReadOptions | None = None,
    memory_pool: lib.MemoryPool | None = None,
) -> RecordBatchStreamReader: ...
def new_file(
    sink: str | lib.NativeFile | IOBase,
    schema: lib.Schema,
    *,
    use_legacy_format: bool | None = None,
    options: IpcWriteOptions | None = None,
) -> RecordBatchFileWriter: ...
def open_file(
    source: bytes | lib.Buffer | lib.NativeFile | IOBase,
    footer_offset: int | None = None,
    *,
    options: IpcReadOptions | None = None,
    memory_pool: lib.MemoryPool | None = None,
) -> RecordBatchFileReader: ...
def serialize_pandas(
    df: pd.DataFrame, *, nthreads: int | None = None, preserve_index: bool | None = None
) -> lib.Buffer: ...
def deserialize_pandas(buf: lib.Buffer, *, use_threads: bool = True) -> pd.DataFrame: ...

__all__ = [
    "IpcReadOptions",
    "IpcWriteOptions",
    "Message",
    "MessageReader",
    "MetadataVersion",
    "ReadStats",
    "RecordBatchReader",
    "WriteStats",
    "_ReadPandasMixin",
    "get_record_batch_size",
    "get_tensor_size",
    "read_message",
    "read_record_batch",
    "read_schema",
    "read_tensor",
    "write_tensor",
    "RecordBatchStreamReader",
    "RecordBatchStreamWriter",
    "RecordBatchFileReader",
    "RecordBatchFileWriter",
    "new_stream",
    "open_stream",
    "new_file",
    "open_file",
    "serialize_pandas",
    "deserialize_pandas",
]

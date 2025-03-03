from typing import Any

from googleapiclient.errors import (
    BatchError as BatchError,
    HttpError as HttpError,
    InvalidChunkSizeError as InvalidChunkSizeError,
    ResumableUploadError as ResumableUploadError,
    UnexpectedBodyError as UnexpectedBodyError,
    UnexpectedMethodError as UnexpectedMethodError,
)
from googleapiclient.model import JsonModel as JsonModel

LOGGER: Any
DEFAULT_CHUNK_SIZE: Any
MAX_URI_LENGTH: int
MAX_BATCH_LIMIT: int
DEFAULT_HTTP_TIMEOUT_SEC: int

class MediaUploadProgress:
    resumable_progress: Any
    total_size: Any
    def __init__(self, resumable_progress, total_size) -> None: ...
    def progress(self): ...

class MediaDownloadProgress:
    resumable_progress: Any
    total_size: Any
    def __init__(self, resumable_progress, total_size) -> None: ...
    def progress(self): ...

class MediaUpload:
    def chunksize(self) -> None: ...
    def mimetype(self): ...
    def size(self) -> None: ...
    def resumable(self): ...
    def getbytes(self, begin, end) -> None: ...
    def has_stream(self): ...
    def stream(self) -> None: ...
    def to_json(self): ...
    @classmethod
    def new_from_json(cls, s): ...

class MediaIoBaseUpload(MediaUpload):
    def __init__(self, fd, mimetype, chunksize=..., resumable: bool = ...) -> None: ...
    def chunksize(self): ...
    def mimetype(self): ...
    def size(self): ...
    def resumable(self): ...
    def getbytes(self, begin, length): ...
    def has_stream(self): ...
    def stream(self): ...
    def to_json(self) -> None: ...

class MediaFileUpload(MediaIoBaseUpload):
    def __init__(
        self, filename, mimetype: Any | None = ..., chunksize=..., resumable: bool = ...
    ) -> None: ...
    def __del__(self) -> None: ...
    def to_json(self): ...
    @staticmethod
    def from_json(s): ...

class MediaInMemoryUpload(MediaIoBaseUpload):
    def __init__(
        self, body, mimetype: str = ..., chunksize=..., resumable: bool = ...
    ) -> None: ...

class MediaIoBaseDownload:
    def __init__(self, fd, request, chunksize=...) -> None: ...
    def next_chunk(self, num_retries: int = ...): ...

class _StreamSlice:
    def __init__(self, stream, begin, chunksize) -> None: ...
    def read(self, n: int = ...): ...

class HttpRequest:
    uri: Any
    method: Any
    body: Any
    headers: Any
    methodId: Any
    http: Any
    postproc: Any
    resumable: Any
    response_callbacks: Any
    body_size: Any
    resumable_uri: Any
    resumable_progress: int
    def __init__(
        self,
        http,
        postproc,
        uri,
        method: str = ...,
        body: Any | None = ...,
        headers: Any | None = ...,
        methodId: Any | None = ...,
        resumable: Any | None = ...,
    ) -> None: ...
    def execute(self, http: Any | None = ..., num_retries: int = ...): ...
    def add_response_callback(self, cb) -> None: ...
    def next_chunk(self, http: Any | None = ..., num_retries: int = ...): ...
    def to_json(self): ...
    @staticmethod
    def from_json(s, http, postproc): ...
    @staticmethod
    def null_postproc(resp, contents): ...

class BatchHttpRequest:
    def __init__(
        self, callback: Any | None = ..., batch_uri: Any | None = ...
    ) -> None: ...
    def add(
        self, request, callback: Any | None = ..., request_id: Any | None = ...
    ) -> None: ...
    def execute(self, http: Any | None = ...) -> None: ...

class HttpRequestMock:
    resp: Any
    content: Any
    postproc: Any
    def __init__(self, resp, content, postproc) -> None: ...
    def execute(self, http: Any | None = ...): ...

class RequestMockBuilder:
    responses: Any
    check_unexpected: Any
    def __init__(self, responses, check_unexpected: bool = ...) -> None: ...
    def __call__(
        self,
        http,
        postproc,
        uri,
        method: str = ...,
        body: Any | None = ...,
        headers: Any | None = ...,
        methodId: Any | None = ...,
        resumable: Any | None = ...,
    ): ...

class HttpMock:
    data: Any
    response_headers: Any
    headers: Any
    uri: Any
    method: Any
    body: Any
    def __init__(
        self, filename: Any | None = ..., headers: Any | None = ...
    ) -> None: ...
    def request(
        self,
        uri,
        method: str = ...,
        body: Any | None = ...,
        headers: Any | None = ...,
        redirections: int = ...,
        connection_type: Any | None = ...,
    ): ...
    def close(self) -> None: ...

class HttpMockSequence:
    follow_redirects: bool
    request_sequence: Any
    def __init__(self, iterable) -> None: ...
    def request(
        self,
        uri,
        method: str = ...,
        body: Any | None = ...,
        headers: Any | None = ...,
        redirections: int = ...,
        connection_type: Any | None = ...,
    ): ...

def set_user_agent(http, user_agent): ...
def tunnel_patch(http): ...
def build_http(): ...

import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class HangoutsChatResource(googleapiclient.discovery.Resource):
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> MediaHttpRequest: ...
    class SpacesResource(googleapiclient.discovery.Resource):
        class MessagesResource(googleapiclient.discovery.Resource):
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AttachmentHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Message = ...,
                threadKey: str = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> MessageHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: Message = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> MessageHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...
        class MembersResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MembershipHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListMembershipsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> SpaceHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListSpacesResponseHttpRequest: ...
        def messages(self) -> MessagesResource: ...
        def members(self) -> MembersResource: ...
    def media(self) -> MediaResource: ...
    def spaces(self) -> SpacesResource: ...

class SpaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Space: ...

class MediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Media: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class MembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Membership: ...

class AttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Attachment: ...

class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Message: ...

class ListMembershipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMembershipsResponse: ...

class ListSpacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSpacesResponse: ...

import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class PolicyTroubleshooterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class IamResource(googleapiclient.discovery.Resource):
        def troubleshoot(
            self,
            *,
            body: GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponseHttpRequest: ...
    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def iam(self) -> IamResource: ...

@typing.type_check_only
class GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPolicytroubleshooterV1betaTroubleshootIamPolicyResponse: ...

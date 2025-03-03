import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SecurityCommandCenterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def group(
                self,
                *,
                parent: str,
                body: GroupAssetsRequest = ...,
                **kwargs: typing.Any
            ) -> GroupAssetsResponseHttpRequest: ...
            def group_next(
                self,
                previous_request: GroupAssetsResponseHttpRequest,
                previous_response: GroupAssetsResponse,
            ) -> GroupAssetsResponseHttpRequest | None: ...
            def list(
                self,
                *,
                parent: str,
                compareDuration: str = ...,
                fieldMask: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                readTime: str = ...,
                **kwargs: typing.Any
            ) -> ListAssetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAssetsResponseHttpRequest,
                previous_response: ListAssetsResponse,
            ) -> ListAssetsResponseHttpRequest | None: ...
            def runDiscovery(
                self,
                *,
                parent: str,
                body: RunAssetDiscoveryRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def updateSecurityMarks(
                self,
                *,
                name: str,
                body: GoogleCloudSecuritycenterV1beta1SecurityMarks = ...,
                startTime: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudSecuritycenterV1beta1SecurityMarksHttpRequest: ...
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: CancelOperationRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListOperationsResponseHttpRequest,
                previous_response: ListOperationsResponse,
            ) -> ListOperationsResponseHttpRequest | None: ...
        @typing.type_check_only
        class SourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FindingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudSecuritycenterV1beta1Finding = ...,
                    findingId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1beta1FindingHttpRequest: ...
                def group(
                    self,
                    *,
                    parent: str,
                    body: GroupFindingsRequest = ...,
                    **kwargs: typing.Any
                ) -> GroupFindingsResponseHttpRequest: ...
                def group_next(
                    self,
                    previous_request: GroupFindingsResponseHttpRequest,
                    previous_response: GroupFindingsResponse,
                ) -> GroupFindingsResponseHttpRequest | None: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldMask: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readTime: str = ...,
                    **kwargs: typing.Any
                ) -> ListFindingsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListFindingsResponseHttpRequest,
                    previous_response: ListFindingsResponse,
                ) -> ListFindingsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1beta1Finding = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1beta1FindingHttpRequest: ...
                def setState(
                    self,
                    *,
                    name: str,
                    body: SetFindingStateRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1beta1FindingHttpRequest: ...
                def updateSecurityMarks(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1beta1SecurityMarks = ...,
                    startTime: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1beta1SecurityMarksHttpRequest: ...
            def create(
                self, *, parent: str, body: Source = ..., **kwargs: typing.Any
            ) -> SourceHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> SourceHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSourcesResponseHttpRequest,
                previous_response: ListSourcesResponse,
            ) -> ListSourcesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Source = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SourceHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def findings(self) -> FindingsResource: ...
        def getOrganizationSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationSettingsHttpRequest: ...
        def updateOrganizationSettings(
            self,
            *,
            name: str,
            body: OrganizationSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OrganizationSettingsHttpRequest: ...
        def assets(self) -> AssetsResource: ...
        def operations(self) -> OperationsResource: ...
        def sources(self) -> SourcesResource: ...
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
    def organizations(self) -> OrganizationsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1beta1FindingHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudSecuritycenterV1beta1Finding: ...

@typing.type_check_only
class GoogleCloudSecuritycenterV1beta1SecurityMarksHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudSecuritycenterV1beta1SecurityMarks: ...

@typing.type_check_only
class GroupAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GroupAssetsResponse: ...

@typing.type_check_only
class GroupFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GroupFindingsResponse: ...

@typing.type_check_only
class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAssetsResponse: ...

@typing.type_check_only
class ListFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListFindingsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSourcesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class OrganizationSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrganizationSettings: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class SourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Source: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DnsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ChangesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            project: str,
            managedZone: str,
            body: Change = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ChangeHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            managedZone: str,
            changeId: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ChangeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            managedZone: str,
            maxResults: int = ...,
            pageToken: str = ...,
            sortBy: typing_extensions.Literal["changeSequence"] = ...,
            sortOrder: str = ...,
            **kwargs: typing.Any
        ) -> ChangesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ChangesListResponseHttpRequest,
            previous_response: ChangesListResponse,
        ) -> ChangesListResponseHttpRequest | None: ...
    @typing.type_check_only
    class DnsKeysResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            project: str,
            managedZone: str,
            dnsKeyId: str,
            clientOperationId: str = ...,
            digestType: str = ...,
            **kwargs: typing.Any
        ) -> DnsKeyHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            managedZone: str,
            digestType: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> DnsKeysListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: DnsKeysListResponseHttpRequest,
            previous_response: DnsKeysListResponse,
        ) -> DnsKeysListResponseHttpRequest | None: ...
    @typing.type_check_only
    class ManagedZoneOperationsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            project: str,
            managedZone: str,
            operation: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            managedZone: str,
            maxResults: int = ...,
            pageToken: str = ...,
            sortBy: typing_extensions.Literal["startTime", "id"] = ...,
            **kwargs: typing.Any
        ) -> ManagedZoneOperationsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ManagedZoneOperationsListResponseHttpRequest,
            previous_response: ManagedZoneOperationsListResponse,
        ) -> ManagedZoneOperationsListResponseHttpRequest | None: ...
    @typing.type_check_only
    class ManagedZonesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            project: str,
            body: ManagedZone = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ManagedZoneHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            managedZone: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            project: str,
            managedZone: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ManagedZoneHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            dnsName: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ManagedZonesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ManagedZonesListResponseHttpRequest,
            previous_response: ManagedZonesListResponse,
        ) -> ManagedZonesListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            managedZone: str,
            body: ManagedZone = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            managedZone: str,
            body: ManagedZone = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    @typing.type_check_only
    class PoliciesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            project: str,
            body: Policy = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            policy: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            project: str,
            policy: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> PoliciesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PoliciesListResponseHttpRequest,
            previous_response: PoliciesListResponse,
        ) -> PoliciesListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            policy: str,
            body: Policy = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> PoliciesPatchResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            policy: str,
            body: Policy = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> PoliciesUpdateResponseHttpRequest: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, clientOperationId: str = ..., **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
    @typing.type_check_only
    class ResourceRecordSetsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            project: str,
            managedZone: str,
            body: ResourceRecordSet = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ResourceRecordSetHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            managedZone: str,
            name: str,
            type: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ResourceRecordSetsDeleteResponseHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            managedZone: str,
            name: str,
            type: str,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ResourceRecordSetHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            managedZone: str,
            maxResults: int = ...,
            name: str = ...,
            pageToken: str = ...,
            type: str = ...,
            **kwargs: typing.Any
        ) -> ResourceRecordSetsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ResourceRecordSetsListResponseHttpRequest,
            previous_response: ResourceRecordSetsListResponse,
        ) -> ResourceRecordSetsListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            managedZone: str,
            name: str,
            type: str,
            body: ResourceRecordSet = ...,
            clientOperationId: str = ...,
            **kwargs: typing.Any
        ) -> ResourceRecordSetHttpRequest: ...
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
    def changes(self) -> ChangesResource: ...
    def dnsKeys(self) -> DnsKeysResource: ...
    def managedZoneOperations(self) -> ManagedZoneOperationsResource: ...
    def managedZones(self) -> ManagedZonesResource: ...
    def policies(self) -> PoliciesResource: ...
    def projects(self) -> ProjectsResource: ...
    def resourceRecordSets(self) -> ResourceRecordSetsResource: ...

@typing.type_check_only
class ChangeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Change: ...

@typing.type_check_only
class ChangesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ChangesListResponse: ...

@typing.type_check_only
class DnsKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DnsKey: ...

@typing.type_check_only
class DnsKeysListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DnsKeysListResponse: ...

@typing.type_check_only
class ManagedZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ManagedZone: ...

@typing.type_check_only
class ManagedZoneOperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ManagedZoneOperationsListResponse: ...

@typing.type_check_only
class ManagedZonesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ManagedZonesListResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PoliciesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PoliciesListResponse: ...

@typing.type_check_only
class PoliciesPatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PoliciesPatchResponse: ...

@typing.type_check_only
class PoliciesUpdateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PoliciesUpdateResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Project: ...

@typing.type_check_only
class ResourceRecordSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResourceRecordSet: ...

@typing.type_check_only
class ResourceRecordSetsDeleteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResourceRecordSetsDeleteResponse: ...

@typing.type_check_only
class ResourceRecordSetsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResourceRecordSetsListResponse: ...

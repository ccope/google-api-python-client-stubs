import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class DocumentResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
            @typing.type_check_only
            class ProcessorsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class HumanReviewConfigResource(googleapiclient.discovery.Resource):
                    def reviewDocument(
                        self,
                        *,
                        humanReviewConfig: str,
                        body: GoogleCloudDocumentaiV1beta3ReviewDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                @typing.type_check_only
                class ProcessorVersionsResource(googleapiclient.discovery.Resource):
                    def batchProcess(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1beta3BatchProcessRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def process(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1beta3ProcessRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDocumentaiV1beta3ProcessResponseHttpRequest: ...
                def batchProcess(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1beta3BatchProcessRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDocumentaiV1beta3Processor = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1beta3ProcessorHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1beta3DisableProcessorRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1beta3EnableProcessorRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1beta3ListProcessorsResponseHttpRequest: ...
                def process(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1beta3ProcessRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1beta3ProcessResponseHttpRequest: ...
                def humanReviewConfig(self) -> HumanReviewConfigResource: ...
                def processorVersions(self) -> ProcessorVersionsResource: ...
            def fetchProcessorTypes(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleCloudDocumentaiV1beta3FetchProcessorTypesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def operations(self) -> OperationsResource: ...
            def processors(self) -> ProcessorsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3FetchProcessorTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1beta3FetchProcessorTypesResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1beta3ListProcessorsResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1beta3ProcessResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1beta3Processor: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...

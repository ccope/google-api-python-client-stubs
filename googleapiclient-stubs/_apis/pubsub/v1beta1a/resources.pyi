import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PubsubResource(googleapiclient.discovery.Resource):
    class SubscriptionsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, subscription: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int = ...,
            query: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListSubscriptionsResponseHttpRequest: ...
        def pullBatch(
            self, *, body: PullBatchRequest = ..., **kwargs: typing.Any
        ) -> PullBatchResponseHttpRequest: ...
        def modifyAckDeadline(
            self, *, body: ModifyAckDeadlineRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def pull(
            self, *, body: PullRequest = ..., **kwargs: typing.Any
        ) -> PullResponseHttpRequest: ...
        def modifyPushConfig(
            self, *, body: ModifyPushConfigRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def create(
            self, *, body: Subscription = ..., **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def get(
            self, *, subscription: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...
        def acknowledge(
            self, *, body: AcknowledgeRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    class TopicsResource(googleapiclient.discovery.Resource):
        def publishBatch(
            self, *, body: PublishBatchRequest = ..., **kwargs: typing.Any
        ) -> PublishBatchResponseHttpRequest: ...
        def create(
            self, *, body: Topic = ..., **kwargs: typing.Any
        ) -> TopicHttpRequest: ...
        def delete(self, *, topic: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def publish(
            self, *, body: PublishRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def list(
            self,
            *,
            query: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListTopicsResponseHttpRequest: ...
        def get(self, *, topic: str, **kwargs: typing.Any) -> TopicHttpRequest: ...
    def subscriptions(self) -> SubscriptionsResource: ...
    def topics(self) -> TopicsResource: ...

class ListSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSubscriptionsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class PullResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PullResponse: ...

class PublishBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublishBatchResponse: ...

class PullBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PullBatchResponse: ...

class TopicHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Topic: ...

class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Subscription: ...

class ListTopicsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTopicsResponse: ...

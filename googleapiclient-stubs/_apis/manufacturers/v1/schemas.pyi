import typing

import typing_extensions

_list = list

@typing.type_check_only
class Attributes(typing_extensions.TypedDict, total=False):
    additionalImageLink: _list[Image]
    ageGroup: str
    brand: str
    capacity: Capacity
    color: str
    count: Count
    description: str
    disclosureDate: str
    excludedDestination: _list[str]
    featureDescription: _list[FeatureDescription]
    flavor: str
    format: str
    gender: str
    gtin: _list[str]
    imageLink: Image
    includedDestination: _list[str]
    itemGroupId: str
    material: str
    mpn: str
    pattern: str
    productDetail: _list[ProductDetail]
    productHighlight: _list[str]
    productLine: str
    productName: str
    productPageUrl: str
    productType: _list[str]
    releaseDate: str
    richProductContent: _list[str]
    scent: str
    size: str
    sizeSystem: str
    sizeType: _list[str]
    suggestedRetailPrice: Price
    targetClientId: str
    theme: str
    title: str
    videoLink: _list[str]

@typing.type_check_only
class Capacity(typing_extensions.TypedDict, total=False):
    unit: str
    value: str

@typing.type_check_only
class Count(typing_extensions.TypedDict, total=False):
    unit: str
    value: str

@typing.type_check_only
class DestinationStatus(typing_extensions.TypedDict, total=False):
    destination: str
    status: typing_extensions.Literal["UNKNOWN", "ACTIVE", "PENDING", "DISAPPROVED"]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FeatureDescription(typing_extensions.TypedDict, total=False):
    headline: str
    image: Image
    text: str

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    imageUrl: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PENDING_PROCESSING",
        "PENDING_CRAWL",
        "OK",
        "ROBOTED",
        "XROBOTED",
        "CRAWL_ERROR",
        "PROCESSING_ERROR",
        "DECODING_ERROR",
        "TOO_BIG",
        "CRAWL_SKIPPED",
        "HOSTLOADED",
        "HTTP_404",
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "CRAWLED", "UPLOADED"]

@typing.type_check_only
class Issue(typing_extensions.TypedDict, total=False):
    attribute: str
    description: str
    destination: str
    resolution: typing_extensions.Literal[
        "RESOLUTION_UNSPECIFIED", "USER_ACTION", "PENDING_PROCESSING"
    ]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]
    timestamp: str
    title: str
    type: str

@typing.type_check_only
class ListProductsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    products: _list[Product]

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    amount: str
    currency: str

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    contentLanguage: str
    destinationStatuses: _list[DestinationStatus]
    issues: _list[Issue]
    name: str
    parent: str
    productId: str
    targetCountry: str

@typing.type_check_only
class ProductDetail(typing_extensions.TypedDict, total=False):
    attributeName: str
    attributeValue: str
    sectionName: str

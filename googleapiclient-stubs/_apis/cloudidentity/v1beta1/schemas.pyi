import typing

import typing_extensions

_list = list

@typing.type_check_only
class AndroidAttributes(typing_extensions.TypedDict, total=False):
    enabledUnknownSources: bool
    ownerProfileAccount: bool
    ownershipPrivilege: typing_extensions.Literal[
        "OWNERSHIP_PRIVILEGE_UNSPECIFIED",
        "DEVICE_ADMINISTRATOR",
        "PROFILE_OWNER",
        "DEVICE_OWNER",
    ]
    supportsWorkProfile: bool

@typing.type_check_only
class ApproveDeviceUserRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ApproveDeviceUserResponse(typing_extensions.TypedDict, total=False):
    deviceUser: DeviceUser

@typing.type_check_only
class BlockDeviceUserRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class BlockDeviceUserResponse(typing_extensions.TypedDict, total=False):
    deviceUser: DeviceUser

@typing.type_check_only
class CancelUserInvitationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelWipeDeviceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelWipeDeviceResponse(typing_extensions.TypedDict, total=False):
    device: Device

@typing.type_check_only
class CancelWipeDeviceUserRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelWipeDeviceUserResponse(typing_extensions.TypedDict, total=False):
    deviceUser: DeviceUser

@typing.type_check_only
class CertificateInfo(typing_extensions.TypedDict, total=False):
    certificateTemplate: CertificateTemplate
    fingerprint: str
    issuer: str
    serialNumber: str
    subject: str
    thumbprint: str
    validationState: typing_extensions.Literal[
        "CERTIFICATE_VALIDATION_STATE_UNSPECIFIED",
        "VALIDATION_SUCCESSFUL",
        "VALIDATION_FAILED",
    ]
    validityExpirationTime: str
    validityStartTime: str

@typing.type_check_only
class CertificateTemplate(typing_extensions.TypedDict, total=False):
    id: str
    majorVersion: int
    minorVersion: int

@typing.type_check_only
class CheckTransitiveMembershipResponse(typing_extensions.TypedDict, total=False):
    hasMembership: bool

@typing.type_check_only
class ClientState(typing_extensions.TypedDict, total=False):
    assetTags: _list[str]
    complianceState: typing_extensions.Literal[
        "COMPLIANCE_STATE_UNSPECIFIED", "COMPLIANT", "NON_COMPLIANT"
    ]
    createTime: str
    customId: str
    etag: str
    healthScore: typing_extensions.Literal[
        "HEALTH_SCORE_UNSPECIFIED", "VERY_POOR", "POOR", "NEUTRAL", "GOOD", "VERY_GOOD"
    ]
    keyValuePairs: dict[str, typing.Any]
    lastUpdateTime: str
    managed: typing_extensions.Literal[
        "MANAGED_STATE_UNSPECIFIED", "MANAGED", "UNMANAGED"
    ]
    name: str
    ownerType: typing_extensions.Literal[
        "OWNER_TYPE_UNSPECIFIED", "OWNER_TYPE_CUSTOMER", "OWNER_TYPE_PARTNER"
    ]
    scoreReason: str

@typing.type_check_only
class CreateDeviceRequest(typing_extensions.TypedDict, total=False):
    device: Device

@typing.type_check_only
class CustomAttributeValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    numberValue: float
    stringValue: str

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    androidSpecificAttributes: AndroidAttributes
    assetTag: str
    basebandVersion: str
    bootloaderVersion: str
    brand: str
    buildNumber: str
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "UNCOMPROMISED"
    ]
    createTime: str
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED",
        "ANDROID",
        "IOS",
        "GOOGLE_SYNC",
        "WINDOWS",
        "MAC_OS",
        "LINUX",
        "CHROME_OS",
    ]
    enabledDeveloperOptions: bool
    enabledUsbDebugging: bool
    encryptionState: typing_extensions.Literal[
        "ENCRYPTION_STATE_UNSPECIFIED",
        "UNSUPPORTED_BY_DEVICE",
        "ENCRYPTED",
        "NOT_ENCRYPTED",
    ]
    endpointVerificationSpecificAttributes: EndpointVerificationSpecificAttributes
    imei: str
    kernelVersion: str
    lastSyncTime: str
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "APPROVED",
        "BLOCKED",
        "PENDING",
        "UNPROVISIONED",
        "WIPING",
        "WIPED",
    ]
    manufacturer: str
    meid: str
    model: str
    name: str
    networkOperator: str
    osVersion: str
    otherAccounts: _list[str]
    ownerType: typing_extensions.Literal[
        "DEVICE_OWNERSHIP_UNSPECIFIED", "COMPANY", "BYOD"
    ]
    releaseVersion: str
    securityPatchTime: str
    serialNumber: str
    wifiMacAddresses: _list[str]

@typing.type_check_only
class DeviceUser(typing_extensions.TypedDict, total=False):
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "NOT_COMPROMISED"
    ]
    createTime: str
    firstSyncTime: str
    languageCode: str
    lastSyncTime: str
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "WIPING",
        "WIPED",
        "APPROVED",
        "BLOCKED",
        "PENDING_APPROVAL",
        "UNENROLLED",
    ]
    name: str
    passwordState: typing_extensions.Literal[
        "PASSWORD_STATE_UNSPECIFIED", "PASSWORD_SET", "PASSWORD_NOT_SET"
    ]
    userAgent: str
    userEmail: str

@typing.type_check_only
class DynamicGroupMetadata(typing_extensions.TypedDict, total=False):
    queries: _list[DynamicGroupQuery]
    status: DynamicGroupStatus

@typing.type_check_only
class DynamicGroupQuery(typing_extensions.TypedDict, total=False):
    query: str
    resourceType: typing_extensions.Literal["RESOURCE_TYPE_UNSPECIFIED", "USER"]

@typing.type_check_only
class DynamicGroupStatus(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "UP_TO_DATE", "UPDATING_MEMBERSHIPS", "INVALID_QUERY"
    ]
    statusTime: str

@typing.type_check_only
class EndpointVerificationSpecificAttributes(typing_extensions.TypedDict, total=False):
    certificateInfo: _list[CertificateInfo]

@typing.type_check_only
class EntityKey(typing_extensions.TypedDict, total=False):
    id: str
    namespace: str

@typing.type_check_only
class ExpiryDetail(typing_extensions.TypedDict, total=False):
    expireTime: str

@typing.type_check_only
class FirstAdminInvitationInfo(typing_extensions.TypedDict, total=False):
    isFirstAdmin: bool
    primaryDomain: str

@typing.type_check_only
class GetMembershipGraphResponse(typing_extensions.TypedDict, total=False):
    adjacencyList: _list[MembershipAdjacencyList]
    groups: _list[Group]

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1AndroidAttributes(
    typing_extensions.TypedDict, total=False
):
    enabledUnknownSources: bool
    ownerProfileAccount: bool
    ownershipPrivilege: typing_extensions.Literal[
        "OWNERSHIP_PRIVILEGE_UNSPECIFIED",
        "DEVICE_ADMINISTRATOR",
        "PROFILE_OWNER",
        "DEVICE_OWNER",
    ]
    supportsWorkProfile: bool

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ApproveDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1BlockDeviceUserMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1BlockDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceResponse(
    typing_extensions.TypedDict, total=False
):
    device: GoogleAppsCloudidentityDevicesV1Device

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ClientState(
    typing_extensions.TypedDict, total=False
):
    assetTags: _list[str]
    complianceState: typing_extensions.Literal[
        "COMPLIANCE_STATE_UNSPECIFIED", "COMPLIANT", "NON_COMPLIANT"
    ]
    createTime: str
    customId: str
    etag: str
    healthScore: typing_extensions.Literal[
        "HEALTH_SCORE_UNSPECIFIED", "VERY_POOR", "POOR", "NEUTRAL", "GOOD", "VERY_GOOD"
    ]
    keyValuePairs: dict[str, typing.Any]
    lastUpdateTime: str
    managed: typing_extensions.Literal[
        "MANAGED_STATE_UNSPECIFIED", "MANAGED", "UNMANAGED"
    ]
    name: str
    ownerType: typing_extensions.Literal[
        "OWNER_TYPE_UNSPECIFIED", "OWNER_TYPE_CUSTOMER", "OWNER_TYPE_PARTNER"
    ]
    scoreReason: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CreateDeviceMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1CustomAttributeValue(
    typing_extensions.TypedDict, total=False
):
    boolValue: bool
    numberValue: float
    stringValue: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1DeleteDeviceMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1DeleteDeviceUserMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1Device(typing_extensions.TypedDict, total=False):
    androidSpecificAttributes: GoogleAppsCloudidentityDevicesV1AndroidAttributes
    assetTag: str
    basebandVersion: str
    bootloaderVersion: str
    brand: str
    buildNumber: str
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "UNCOMPROMISED"
    ]
    createTime: str
    deviceType: typing_extensions.Literal[
        "DEVICE_TYPE_UNSPECIFIED",
        "ANDROID",
        "IOS",
        "GOOGLE_SYNC",
        "WINDOWS",
        "MAC_OS",
        "LINUX",
        "CHROME_OS",
    ]
    enabledDeveloperOptions: bool
    enabledUsbDebugging: bool
    encryptionState: typing_extensions.Literal[
        "ENCRYPTION_STATE_UNSPECIFIED",
        "UNSUPPORTED_BY_DEVICE",
        "ENCRYPTED",
        "NOT_ENCRYPTED",
    ]
    imei: str
    kernelVersion: str
    lastSyncTime: str
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "APPROVED",
        "BLOCKED",
        "PENDING",
        "UNPROVISIONED",
        "WIPING",
        "WIPED",
    ]
    manufacturer: str
    meid: str
    model: str
    name: str
    networkOperator: str
    osVersion: str
    otherAccounts: _list[str]
    ownerType: typing_extensions.Literal[
        "DEVICE_OWNERSHIP_UNSPECIFIED", "COMPANY", "BYOD"
    ]
    releaseVersion: str
    securityPatchTime: str
    serialNumber: str
    wifiMacAddresses: _list[str]

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1DeviceUser(
    typing_extensions.TypedDict, total=False
):
    compromisedState: typing_extensions.Literal[
        "COMPROMISED_STATE_UNSPECIFIED", "COMPROMISED", "NOT_COMPROMISED"
    ]
    createTime: str
    firstSyncTime: str
    languageCode: str
    lastSyncTime: str
    managementState: typing_extensions.Literal[
        "MANAGEMENT_STATE_UNSPECIFIED",
        "WIPING",
        "WIPED",
        "APPROVED",
        "BLOCKED",
        "PENDING_APPROVAL",
        "UNENROLLED",
    ]
    name: str
    passwordState: typing_extensions.Literal[
        "PASSWORD_STATE_UNSPECIFIED", "PASSWORD_SET", "PASSWORD_NOT_SET"
    ]
    userAgent: str
    userEmail: str

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1ListEndpointAppsMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1SignoutDeviceUserMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1UpdateClientStateMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1UpdateDeviceMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceResponse(
    typing_extensions.TypedDict, total=False
):
    device: GoogleAppsCloudidentityDevicesV1Device

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceUserMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsCloudidentityDevicesV1WipeDeviceUserResponse(
    typing_extensions.TypedDict, total=False
):
    deviceUser: GoogleAppsCloudidentityDevicesV1DeviceUser

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    additionalGroupKeys: _list[EntityKey]
    createTime: str
    description: str
    displayName: str
    dynamicGroupMetadata: DynamicGroupMetadata
    groupKey: EntityKey
    labels: dict[str, typing.Any]
    name: str
    parent: str
    posixGroups: _list[PosixGroup]
    updateTime: str

@typing.type_check_only
class GroupRelation(typing_extensions.TypedDict, total=False):
    displayName: str
    group: str
    groupKey: EntityKey
    labels: dict[str, typing.Any]
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DIRECT", "INDIRECT", "DIRECT_AND_INDIRECT"
    ]
    roles: _list[TransitiveMembershipRole]

@typing.type_check_only
class IsInvitableUserResponse(typing_extensions.TypedDict, total=False):
    isInvitableUser: bool

@typing.type_check_only
class ListClientStatesResponse(typing_extensions.TypedDict, total=False):
    clientStates: _list[ClientState]
    nextPageToken: str

@typing.type_check_only
class ListDeviceUsersResponse(typing_extensions.TypedDict, total=False):
    deviceUsers: _list[DeviceUser]
    nextPageToken: str

@typing.type_check_only
class ListDevicesResponse(typing_extensions.TypedDict, total=False):
    devices: _list[Device]
    nextPageToken: str

@typing.type_check_only
class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    groups: _list[Group]
    nextPageToken: str

@typing.type_check_only
class ListMembershipsResponse(typing_extensions.TypedDict, total=False):
    memberships: _list[Membership]
    nextPageToken: str

@typing.type_check_only
class ListUserInvitationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userInvitations: _list[UserInvitation]

@typing.type_check_only
class LookupGroupNameResponse(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class LookupMembershipNameResponse(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class LookupSelfDeviceUsersResponse(typing_extensions.TypedDict, total=False):
    customer: str
    names: _list[str]
    nextPageToken: str

@typing.type_check_only
class MemberRelation(typing_extensions.TypedDict, total=False):
    member: str
    preferredMemberKey: _list[EntityKey]
    relationType: typing_extensions.Literal[
        "RELATION_TYPE_UNSPECIFIED", "DIRECT", "INDIRECT", "DIRECT_AND_INDIRECT"
    ]
    roles: _list[TransitiveMembershipRole]

@typing.type_check_only
class MemberRestriction(typing_extensions.TypedDict, total=False):
    evaluation: RestrictionEvaluation
    query: str

@typing.type_check_only
class Membership(typing_extensions.TypedDict, total=False):
    createTime: str
    memberKey: EntityKey
    name: str
    preferredMemberKey: EntityKey
    roles: _list[MembershipRole]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "USER", "SERVICE_ACCOUNT", "GROUP", "SHARED_DRIVE", "OTHER"
    ]
    updateTime: str

@typing.type_check_only
class MembershipAdjacencyList(typing_extensions.TypedDict, total=False):
    edges: _list[Membership]
    group: str

@typing.type_check_only
class MembershipRole(typing_extensions.TypedDict, total=False):
    expiryDetail: ExpiryDetail
    name: str
    restrictionEvaluations: RestrictionEvaluations

@typing.type_check_only
class MembershipRoleRestrictionEvaluation(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "COMPLIANT",
        "FORWARD_COMPLIANT",
        "NON_COMPLIANT",
        "EVALUATING",
    ]

@typing.type_check_only
class ModifyMembershipRolesRequest(typing_extensions.TypedDict, total=False):
    addRoles: _list[MembershipRole]
    removeRoles: _list[str]
    updateRolesParams: _list[UpdateMembershipRolesParams]

@typing.type_check_only
class ModifyMembershipRolesResponse(typing_extensions.TypedDict, total=False):
    membership: Membership

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PosixGroup(typing_extensions.TypedDict, total=False):
    gid: str
    name: str
    systemId: str

@typing.type_check_only
class RestrictionEvaluation(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "EVALUATING",
        "COMPLIANT",
        "FORWARD_COMPLIANT",
        "NON_COMPLIANT",
    ]

@typing.type_check_only
class RestrictionEvaluations(typing_extensions.TypedDict, total=False):
    memberRestrictionEvaluation: MembershipRoleRestrictionEvaluation

@typing.type_check_only
class SearchGroupsResponse(typing_extensions.TypedDict, total=False):
    groups: _list[Group]
    nextPageToken: str

@typing.type_check_only
class SearchTransitiveGroupsResponse(typing_extensions.TypedDict, total=False):
    memberships: _list[GroupRelation]
    nextPageToken: str

@typing.type_check_only
class SearchTransitiveMembershipsResponse(typing_extensions.TypedDict, total=False):
    memberships: _list[MemberRelation]
    nextPageToken: str

@typing.type_check_only
class SecuritySettings(typing_extensions.TypedDict, total=False):
    memberRestriction: MemberRestriction
    name: str

@typing.type_check_only
class SendUserInvitationRequest(typing_extensions.TypedDict, total=False):
    firstAdminInvitationInfo: FirstAdminInvitationInfo

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TransitiveMembershipRole(typing_extensions.TypedDict, total=False):
    role: str

@typing.type_check_only
class UpdateMembershipRolesParams(typing_extensions.TypedDict, total=False):
    fieldMask: str
    membershipRole: MembershipRole

@typing.type_check_only
class UserInvitation(typing_extensions.TypedDict, total=False):
    mailsSentCount: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_YET_SENT", "INVITED", "ACCEPTED", "DECLINED"
    ]
    updateTime: str

@typing.type_check_only
class WipeDeviceRequest(typing_extensions.TypedDict, total=False):
    removeResetLock: bool

@typing.type_check_only
class WipeDeviceResponse(typing_extensions.TypedDict, total=False):
    device: Device

@typing.type_check_only
class WipeDeviceUserRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class WipeDeviceUserResponse(typing_extensions.TypedDict, total=False):
    deviceUser: DeviceUser

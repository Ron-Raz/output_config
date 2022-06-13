import json
import math
from KalturaClient import *
from KalturaClient.Plugins.Core import *
from KalturaClient.Plugins.Reach import *
from KalturaClient.Plugins.Metadata import *

config = KalturaConfiguration()
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
outJson = {}
ks = client.session.start(
    "ADMIN SECRET",
    "USER ID",
    KalturaSessionType.ADMIN,
    PARTNER_ID)

client.setKs(ks)
pager = KalturaFilterPager()
pager.pageSize = 30


def toJson(obj, attrs):
    ret = {}
    for attr in attrs:
        val = getattr(obj, attr)
        if str(val).startswith('<KalturaClient'):
            val = val.value
        ret[attr] = val
    return ret


outJson["accessControlProfile"] = []

filter = KalturaAccessControlProfileFilter()
attrs = ['id', 'createdAt', 'description', 'isDefault', 'name',
         'partnerId', 'rules', 'systemName', 'updatedAt']
result = client.accessControlProfile.list(filter, pager)
for pager.pageIndex in range(1, math.ceil(result.totalCount/pager.pageSize)+1):
    result = client.accessControlProfile.list(filter, pager)
    for obj in result.getObjects():
        outJson["accessControlProfile"].append(toJson(obj, attrs))


outJson["userRole"] = []

filter = KalturaUserRoleFilter()
attrs = ['id', 'name', 'systemName', 'description', 'status',
         'permissionNames', 'tags', 'createdAt', 'updatedAt']
result = client.userRole.list(filter, pager)
for pager.pageIndex in range(1, math.ceil(result.totalCount/pager.pageSize)+1):
    result = client.userRole.list(filter, pager)
    for obj in result.getObjects():
        outJson["userRole"].append(toJson(obj, attrs))

outJson["conversionProfile"] = []

filter = KalturaConversionProfileFilter()
attrs = ['id', 'status', 'type', 'name', 'systemName', 'tags', 'description', 'defaultEntryId', 'createdAt', 'flavorParamsIds', 'isDefault', 'isPartnerDefault', 'clipStart', 'clipDuration',
         'xslTransformation', 'storageProfileId', 'mediaParserType', 'calculateComplexity', 'collectionTags', 'conditionalProfiles', 'detectGOP', 'mediaInfoXslTransformation', 'defaultReplacementOptions', 'defaultAudioLang']
result = client.conversionProfile.list(filter, pager)
for pager.pageIndex in range(1, math.ceil(result.totalCount/pager.pageSize)+1):
    result = client.conversionProfile.list(filter, pager)
    for obj in result.getObjects():
        outJson["conversionProfile"].append(toJson(obj, attrs))


outJson["user"] = []

filter = KalturaUserFilter()
filter.isAdminEqual = KalturaNullableBoolean.TRUE_VALUE
attrs = ['id', 'screenName', 'fullName', 'email', 'description', 'tags', 'adminTags', 'status', 'createdAt', 'updatedAt', 'lastLoginTime',
         'statusUpdatedAt', 'deletedAt', 'userMode', 'type', 'isAdmin', 'roleIds', 'roleNames', 'isAccountOwner', 'loginEnabled']
result = client.user.list(filter, pager)
for pager.pageIndex in range(1, math.ceil(result.totalCount/pager.pageSize)+1):
    result = client.user.list(filter, pager)
    for obj in result.getObjects():
        outJson["user"].append(toJson(obj, attrs))

outJson["metadataProfile"] = []

filter = KalturaMetadataProfileFilter()
attrs = ['id', 'metadataObjectType', 'version', 'name', 'systemName', 'description',
         'createdAt', 'updatedAt', 'status', 'xsd', 'createMode', 'disableReIndexing']
result = client.metadata.metadataProfile.list(filter, pager)
for pager.pageIndex in range(1, math.ceil(result.totalCount/pager.pageSize)+1):
    result = client.metadata.metadataProfile.list(filter, pager)
    for obj in result.getObjects():
        outJson["metadataProfile"].append(toJson(obj, attrs))

outJson["reachProfile"] = []

filter = KalturaReachProfileFilter()
attrs = ['id', 'name', 'createdAt', 'updatedAt', 'status', 'profileType', 'defaultOutputFormat', 'enableMachineModeration', 'enableHumanModeration', 'autoDisplayMachineCaptionsOnPlayer', 'autoDisplayHumanCaptionsOnPlayer', 'enableMetadataExtraction',
         'enableSpeakerChangeIndication', 'enableAudioTags', 'enableProfanityRemoval', 'maxCharactersPerCaptionLine', 'contentDeletionPolicy', 'usedCredit', 'dictionaries', 'flavorParamsIds', 'vendorTaskProcessingRegion']
result = client.reach.reachProfile.list(filter, pager)
for pager.pageIndex in range(1, math.ceil(result.totalCount/pager.pageSize)+1):
    result = client.reach.reachProfile.list(filter, pager)
    for obj in result.getObjects():
        outJson["reachProfile"].append(toJson(obj, attrs))

outJson["uiConf"] = []

filter = KalturaUiConfFilter()
attrs = ['id', 'name', 'description', 'objTypeAsString', 'width', 'height', 'htmlParams', 'swfUrl', 'confFilePath', 'confFile', 'confFileFeatures',
         'config', 'confVars', 'useCdn', 'tags', 'swfUrlVersion', 'createdAt', 'updatedAt', 'creationMode', 'html5Url', 'version', 'partnerTags']
result = client.uiConf.list(filter, pager)
for pager.pageIndex in range(1, math.ceil(result.totalCount/pager.pageSize)+1):
    result = client.uiConf.list(filter, pager)
    for obj in result.getObjects():
        outJson["uiConf"].append(toJson(obj, attrs))

print(json.dumps(outJson))

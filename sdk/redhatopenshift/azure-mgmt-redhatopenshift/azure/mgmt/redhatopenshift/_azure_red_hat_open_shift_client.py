# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import AzureRedHatOpenShiftClientConfiguration



class AzureRedHatOpenShiftClient(MultiApiClientMixin, SDKClient):
    """Rest API for Azure Red Hat OpenShift

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: AzureRedHatOpenShiftClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2020-04-30'
    _PROFILE_TAG = "azure.mgmt.redhatopenshift.AzureRedHatOpenShiftClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = AzureRedHatOpenShiftClientConfiguration(credentials, subscription_id, base_url)
        super(AzureRedHatOpenShiftClient, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2020-04-30: :mod:`v2020_04_30.models<azure.mgmt.redhatopenshift.v2020_04_30.models>`
        """
        if api_version == '2020-04-30':
            from .v2020_04_30 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def open_shift_clusters(self):
        """Instance depends on the API version:

           * 2020-04-30: :class:`OpenShiftClustersOperations<azure.mgmt.redhatopenshift.v2020_04_30.operations.OpenShiftClustersOperations>`
        """
        api_version = self._get_api_version('open_shift_clusters')
        if api_version == '2020-04-30':
            from .v2020_04_30.operations import OpenShiftClustersOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2020-04-30: :class:`Operations<azure.mgmt.redhatopenshift.v2020_04_30.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2020-04-30':
            from .v2020_04_30.operations import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

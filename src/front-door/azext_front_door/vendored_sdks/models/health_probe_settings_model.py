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

from .sub_resource import SubResource


class HealthProbeSettingsModel(SubResource):
    """Load balancing settings for a backend pool.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param path: The path to use for the health probe. Default is /
    :type path: str
    :param protocol: Protocol scheme to use for this probe. Possible values
     include: 'Http', 'Https'
    :type protocol: str or ~azure.mgmt.frontdoor.models.FrontDoorProtocol
    :param interval_in_seconds: The number of seconds between health probes.
    :type interval_in_seconds: int
    :param resource_state: Resource status. Possible values include:
     'Creating', 'Enabling', 'Enabled', 'Disabling', 'Disabled', 'Deleting'
    :type resource_state: str or
     ~azure.mgmt.frontdoor.models.FrontDoorResourceState
    :param name: Resource name.
    :type name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'path': {'key': 'properties.path', 'type': 'str'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'interval_in_seconds': {'key': 'properties.intervalInSeconds', 'type': 'int'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(HealthProbeSettingsModel, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
        self.protocol = kwargs.get('protocol', None)
        self.interval_in_seconds = kwargs.get('interval_in_seconds', None)
        self.resource_state = kwargs.get('resource_state', None)
        self.name = kwargs.get('name', None)
        self.type = None

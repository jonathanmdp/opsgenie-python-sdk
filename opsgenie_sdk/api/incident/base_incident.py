# coding: utf-8

"""
    Python SDK for Opsgenie REST API

    Python SDK for Opsgenie REST API  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@opsgenie.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BaseIncident(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'tiny_id': 'str',
        'message': 'str',
        'status': 'str',
        'is_seen': 'bool',
        'tags': 'list[str]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'source': 'str',
        'owner': 'str',
        'priority': 'str',
        'responders': 'list[Responder]',
        'team_id': 'str',
        'details': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'tiny_id': 'tinyId',
        'message': 'message',
        'status': 'status',
        'is_seen': 'isSeen',
        'tags': 'tags',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'source': 'source',
        'owner': 'owner',
        'priority': 'priority',
        'responders': 'responders',
        'team_id': 'teamId',
        'details': 'details'
    }

    def __init__(self, id=None, tiny_id=None, message=None, status=None, is_seen=None, tags=None, created_at=None, updated_at=None, source=None, owner=None, priority=None, responders=None, team_id=None, details=None):  # noqa: E501
        """BaseIncident - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._tiny_id = None
        self._message = None
        self._status = None
        self._is_seen = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self._source = None
        self._owner = None
        self._priority = None
        self._responders = None
        self._team_id = None
        self._details = None
        self.discriminator = None

        self.id = id
        if tiny_id is not None:
            self.tiny_id = tiny_id
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status
        if is_seen is not None:
            self.is_seen = is_seen
        if tags is not None:
            self.tags = tags
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if source is not None:
            self.source = source
        if owner is not None:
            self.owner = owner
        if priority is not None:
            self.priority = priority
        if responders is not None:
            self.responders = responders
        if team_id is not None:
            self.team_id = team_id
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this BaseIncident.  # noqa: E501


        :return: The id of this BaseIncident.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseIncident.


        :param id: The id of this BaseIncident.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def tiny_id(self):
        """Gets the tiny_id of this BaseIncident.  # noqa: E501


        :return: The tiny_id of this BaseIncident.  # noqa: E501
        :rtype: str
        """
        return self._tiny_id

    @tiny_id.setter
    def tiny_id(self, tiny_id):
        """Sets the tiny_id of this BaseIncident.


        :param tiny_id: The tiny_id of this BaseIncident.  # noqa: E501
        :type: str
        """

        self._tiny_id = tiny_id

    @property
    def message(self):
        """Gets the message of this BaseIncident.  # noqa: E501


        :return: The message of this BaseIncident.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BaseIncident.


        :param message: The message of this BaseIncident.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this BaseIncident.  # noqa: E501


        :return: The status of this BaseIncident.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BaseIncident.


        :param status: The status of this BaseIncident.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def is_seen(self):
        """Gets the is_seen of this BaseIncident.  # noqa: E501


        :return: The is_seen of this BaseIncident.  # noqa: E501
        :rtype: bool
        """
        return self._is_seen

    @is_seen.setter
    def is_seen(self, is_seen):
        """Sets the is_seen of this BaseIncident.


        :param is_seen: The is_seen of this BaseIncident.  # noqa: E501
        :type: bool
        """

        self._is_seen = is_seen

    @property
    def tags(self):
        """Gets the tags of this BaseIncident.  # noqa: E501


        :return: The tags of this BaseIncident.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BaseIncident.


        :param tags: The tags of this BaseIncident.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this BaseIncident.  # noqa: E501


        :return: The created_at of this BaseIncident.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BaseIncident.


        :param created_at: The created_at of this BaseIncident.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BaseIncident.  # noqa: E501


        :return: The updated_at of this BaseIncident.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BaseIncident.


        :param updated_at: The updated_at of this BaseIncident.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def source(self):
        """Gets the source of this BaseIncident.  # noqa: E501


        :return: The source of this BaseIncident.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BaseIncident.


        :param source: The source of this BaseIncident.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def owner(self):
        """Gets the owner of this BaseIncident.  # noqa: E501


        :return: The owner of this BaseIncident.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this BaseIncident.


        :param owner: The owner of this BaseIncident.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def priority(self):
        """Gets the priority of this BaseIncident.  # noqa: E501


        :return: The priority of this BaseIncident.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this BaseIncident.


        :param priority: The priority of this BaseIncident.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def responders(self):
        """Gets the responders of this BaseIncident.  # noqa: E501


        :return: The responders of this BaseIncident.  # noqa: E501
        :rtype: list[Responder]
        """
        return self._responders

    @responders.setter
    def responders(self, responders):
        """Sets the responders of this BaseIncident.


        :param responders: The responders of this BaseIncident.  # noqa: E501
        :type: list[Responder]
        """

        self._responders = responders

    @property
    def team_id(self):
        """Gets the team_id of this BaseIncident.  # noqa: E501


        :return: The team_id of this BaseIncident.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this BaseIncident.


        :param team_id: The team_id of this BaseIncident.  # noqa: E501
        :type: str
        """

        self._team_id = team_id

    @property
    def details(self):
        """Gets the details of this BaseIncident.  # noqa: E501

        Map of key-value pairs to use as custom properties of the incident  # noqa: E501

        :return: The details of this BaseIncident.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this BaseIncident.

        Map of key-value pairs to use as custom properties of the incident  # noqa: E501

        :param details: The details of this BaseIncident.  # noqa: E501
        :type: dict(str, str)
        """

        self._details = details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BaseIncident):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

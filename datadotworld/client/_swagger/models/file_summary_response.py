# coding: utf-8

"""
    data.world API

    # data.world in a nutshell  data.world is a productive, secure platform for modern data teamwork.  We bring together your data practitioners, subject matter experts, and other stakeholders by removing costly barriers to data discovery, comprehension, integration, and sharing.   Everything your team needs to quickly understand and use data stays with it.   Social features and integrations encourage collaborators to ask and answer questions, share discoveries, and coordinate closely while still using their preferred tools.  Our focus on interoperability helps you enhance your own data with data from any source, including our vast and growing library of free public datasets.   Sophisticated permissions, auditing features, and more make it easy to manage who views your data and what they do with it.  # Conventions  ## Authentication  All data.world API calls require an API token.   OAuth2 is the preferred and most secure method for authenticating users of your data.world applications. Visit our [oauth documentation](https://apidocs.data.world/toolkit/oauth) for additional information. Alternatively, you can obtain a token for _personal use or testing_ by navigating to your profile settings, under the Advanced tab ([https://data.world/settings/advanced](https://data.world/settings/advanced)).  Authentication must be provided in API requests via the `Authorization` header. For example, for a user whose API token is `my_api_token`, the request header should be `Authorization: Bearer my_api_token` (note the `Bearer` prefix).  ## Content type   By default, `application/json` is the content type used in request and response bodies. Exceptions are noted in respective endpoint documentation.  ## HTTPS only   Our APIs can only be accessed via HTTPS.  # Interested in building data.world apps?  Check out our [developer portal](https://apidocs.data.world) for tips on how to get started, tutorials, and to interact with the API endpoints right within your browser.  # noqa: E501

    OpenAPI spec version: 0.21.0
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FileSummaryResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'name': 'str',
        'size_in_bytes': 'int',
        'source': 'FileSourceSummaryResponse',
        'updated': 'str'
    }

    attribute_map = {
        'created': 'created',
        'description': 'description',
        'labels': 'labels',
        'name': 'name',
        'size_in_bytes': 'sizeInBytes',
        'source': 'source',
        'updated': 'updated'
    }

    def __init__(self, created=None, description=None, labels=None, name=None, size_in_bytes=None, source=None, updated=None):  # noqa: E501
        """FileSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._description = None
        self._labels = None
        self._name = None
        self._size_in_bytes = None
        self._source = None
        self._updated = None
        self.discriminator = None
        self.created = created
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        self.name = name
        if size_in_bytes is not None:
            self.size_in_bytes = size_in_bytes
        if source is not None:
            self.source = source
        self.updated = updated

    @property
    def created(self):
        """Gets the created of this FileSummaryResponse.  # noqa: E501

        Date and time when file was created.  # noqa: E501

        :return: The created of this FileSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FileSummaryResponse.

        Date and time when file was created.  # noqa: E501

        :param created: The created of this FileSummaryResponse.  # noqa: E501
        :type: str
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def description(self):
        """Gets the description of this FileSummaryResponse.  # noqa: E501

        File description.  # noqa: E501

        :return: The description of this FileSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FileSummaryResponse.

        File description.  # noqa: E501

        :param description: The description of this FileSummaryResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def labels(self):
        """Gets the labels of this FileSummaryResponse.  # noqa: E501

        File labels.  # noqa: E501

        :return: The labels of this FileSummaryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this FileSummaryResponse.

        File labels.  # noqa: E501

        :param labels: The labels of this FileSummaryResponse.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this FileSummaryResponse.  # noqa: E501

        File name. Should include type extension always when possible. Must not include slashes.  # noqa: E501

        :return: The name of this FileSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileSummaryResponse.

        File name. Should include type extension always when possible. Must not include slashes.  # noqa: E501

        :param name: The name of this FileSummaryResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size_in_bytes(self):
        """Gets the size_in_bytes of this FileSummaryResponse.  # noqa: E501


        :return: The size_in_bytes of this FileSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """Sets the size_in_bytes of this FileSummaryResponse.


        :param size_in_bytes: The size_in_bytes of this FileSummaryResponse.  # noqa: E501
        :type: int
        """

        self._size_in_bytes = size_in_bytes

    @property
    def source(self):
        """Gets the source of this FileSummaryResponse.  # noqa: E501


        :return: The source of this FileSummaryResponse.  # noqa: E501
        :rtype: FileSourceSummaryResponse
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this FileSummaryResponse.


        :param source: The source of this FileSummaryResponse.  # noqa: E501
        :type: FileSourceSummaryResponse
        """

        self._source = source

    @property
    def updated(self):
        """Gets the updated of this FileSummaryResponse.  # noqa: E501

        Date and time when file was last updated.  # noqa: E501

        :return: The updated of this FileSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this FileSummaryResponse.

        Date and time when file was last updated.  # noqa: E501

        :param updated: The updated of this FileSummaryResponse.  # noqa: E501
        :type: str
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(FileSummaryResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

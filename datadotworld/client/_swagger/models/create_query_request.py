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

class CreateQueryRequest(object):
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
        'name': 'str',
        'content': 'str',
        'language': 'str',
        'published': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'content': 'content',
        'language': 'language',
        'published': 'published'
    }

    def __init__(self, name=None, content=None, language=None, published=None):  # noqa: E501
        """CreateQueryRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._content = None
        self._language = None
        self._published = None
        self.discriminator = None
        self.name = name
        self.content = content
        self.language = language
        if published is not None:
            self.published = published

    @property
    def name(self):
        """Gets the name of this CreateQueryRequest.  # noqa: E501

        Query name.  # noqa: E501

        :return: The name of this CreateQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateQueryRequest.

        Query name.  # noqa: E501

        :param name: The name of this CreateQueryRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def content(self):
        """Gets the content of this CreateQueryRequest.  # noqa: E501

        The actual query text to be executed.  # noqa: E501

        :return: The content of this CreateQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateQueryRequest.

        The actual query text to be executed.  # noqa: E501

        :param content: The content of this CreateQueryRequest.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def language(self):
        """Gets the language of this CreateQueryRequest.  # noqa: E501

        The language in which this query is written. Can be either 'SPARQL' or 'SQL'.  # noqa: E501

        :return: The language of this CreateQueryRequest.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreateQueryRequest.

        The language in which this query is written. Can be either 'SPARQL' or 'SQL'.  # noqa: E501

        :param language: The language of this CreateQueryRequest.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def published(self):
        """Gets the published of this CreateQueryRequest.  # noqa: E501

        Indicates if this query should be visible to anyone with access to its dataset or project.  # noqa: E501

        :return: The published of this CreateQueryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this CreateQueryRequest.

        Indicates if this query should be visible to anyone with access to its dataset or project.  # noqa: E501

        :param published: The published of this CreateQueryRequest.  # noqa: E501
        :type: bool
        """

        self._published = published

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
        if issubclass(CreateQueryRequest, dict):
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
        if not isinstance(other, CreateQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

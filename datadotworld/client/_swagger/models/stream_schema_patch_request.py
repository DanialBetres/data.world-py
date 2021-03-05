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

class StreamSchemaPatchRequest(object):
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
        'primary_key_fields': 'list[str]',
        'sequence_field': 'str',
        'update_method': 'str'
    }

    attribute_map = {
        'primary_key_fields': 'primaryKeyFields',
        'sequence_field': 'sequenceField',
        'update_method': 'updateMethod'
    }

    def __init__(self, primary_key_fields=None, sequence_field=None, update_method=None):  # noqa: E501
        """StreamSchemaPatchRequest - a model defined in Swagger"""  # noqa: E501
        self._primary_key_fields = None
        self._sequence_field = None
        self._update_method = None
        self.discriminator = None
        if primary_key_fields is not None:
            self.primary_key_fields = primary_key_fields
        if sequence_field is not None:
            self.sequence_field = sequence_field
        self.update_method = update_method

    @property
    def primary_key_fields(self):
        """Gets the primary_key_fields of this StreamSchemaPatchRequest.  # noqa: E501

        One or more fields that make up the primary key of a record  # noqa: E501

        :return: The primary_key_fields of this StreamSchemaPatchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._primary_key_fields

    @primary_key_fields.setter
    def primary_key_fields(self, primary_key_fields):
        """Sets the primary_key_fields of this StreamSchemaPatchRequest.

        One or more fields that make up the primary key of a record  # noqa: E501

        :param primary_key_fields: The primary_key_fields of this StreamSchemaPatchRequest.  # noqa: E501
        :type: list[str]
        """

        self._primary_key_fields = primary_key_fields

    @property
    def sequence_field(self):
        """Gets the sequence_field of this StreamSchemaPatchRequest.  # noqa: E501

        A numeric or datetime field by which to sort records for the purpose of deduplication.  Numeric fields must fit in a 64-bit signed integer datetime fields must use an ISO-8601 compatible format  (https://www.ietf.org/rfc/rfc3339.txt).   # noqa: E501

        :return: The sequence_field of this StreamSchemaPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._sequence_field

    @sequence_field.setter
    def sequence_field(self, sequence_field):
        """Sets the sequence_field of this StreamSchemaPatchRequest.

        A numeric or datetime field by which to sort records for the purpose of deduplication.  Numeric fields must fit in a 64-bit signed integer datetime fields must use an ISO-8601 compatible format  (https://www.ietf.org/rfc/rfc3339.txt).   # noqa: E501

        :param sequence_field: The sequence_field of this StreamSchemaPatchRequest.  # noqa: E501
        :type: str
        """

        self._sequence_field = sequence_field

    @property
    def update_method(self):
        """Gets the update_method of this StreamSchemaPatchRequest.  # noqa: E501

        Specifies how pre-existing records should be affected by a schema change.   # noqa: E501

        :return: The update_method of this StreamSchemaPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._update_method

    @update_method.setter
    def update_method(self, update_method):
        """Sets the update_method of this StreamSchemaPatchRequest.

        Specifies how pre-existing records should be affected by a schema change.   # noqa: E501

        :param update_method: The update_method of this StreamSchemaPatchRequest.  # noqa: E501
        :type: str
        """
        if update_method is None:
            raise ValueError("Invalid value for `update_method`, must not be `None`")  # noqa: E501
        allowed_values = ["TRUNCATE"]  # noqa: E501
        if update_method not in allowed_values:
            raise ValueError(
                "Invalid value for `update_method` ({0}), must be one of {1}"  # noqa: E501
                .format(update_method, allowed_values)
            )

        self._update_method = update_method

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
        if issubclass(StreamSchemaPatchRequest, dict):
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
        if not isinstance(other, StreamSchemaPatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

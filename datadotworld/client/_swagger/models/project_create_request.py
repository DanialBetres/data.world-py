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

class ProjectCreateRequest(object):
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
        'files': 'list[FileCreateRequest]',
        'license': 'str',
        'linked_datasets': 'list[LinkedDatasetCreateOrUpdateRequest]',
        'objective': 'str',
        'summary': 'str',
        'tags': 'list[str]',
        'title': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'files': 'files',
        'license': 'license',
        'linked_datasets': 'linkedDatasets',
        'objective': 'objective',
        'summary': 'summary',
        'tags': 'tags',
        'title': 'title',
        'visibility': 'visibility'
    }

    def __init__(self, files=None, license=None, linked_datasets=None, objective=None, summary=None, tags=None, title=None, visibility=None):  # noqa: E501
        """ProjectCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._files = None
        self._license = None
        self._linked_datasets = None
        self._objective = None
        self._summary = None
        self._tags = None
        self._title = None
        self._visibility = None
        self.discriminator = None
        if files is not None:
            self.files = files
        if license is not None:
            self.license = license
        if linked_datasets is not None:
            self.linked_datasets = linked_datasets
        if objective is not None:
            self.objective = objective
        if summary is not None:
            self.summary = summary
        if tags is not None:
            self.tags = tags
        self.title = title
        self.visibility = visibility

    @property
    def files(self):
        """Gets the files of this ProjectCreateRequest.  # noqa: E501

        Initial set of files. At project creation time, file uploads are not supported. However, this property can be used to add files from URL.  # noqa: E501

        :return: The files of this ProjectCreateRequest.  # noqa: E501
        :rtype: list[FileCreateRequest]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ProjectCreateRequest.

        Initial set of files. At project creation time, file uploads are not supported. However, this property can be used to add files from URL.  # noqa: E501

        :param files: The files of this ProjectCreateRequest.  # noqa: E501
        :type: list[FileCreateRequest]
        """

        self._files = files

    @property
    def license(self):
        """Gets the license of this ProjectCreateRequest.  # noqa: E501

        Project license. Find additional info for allowed values [here](https://data.world/license-help).  # noqa: E501

        :return: The license of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this ProjectCreateRequest.

        Project license. Find additional info for allowed values [here](https://data.world/license-help).  # noqa: E501

        :param license: The license of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Public Domain", "PDDL", "CC-0", "CC-BY", "CDLA-Permissive-1.0", "ODC-BY", "CC-BY-SA", "CDLA-Sharing-1.0", "ODC-ODbL", "CC BY-NC", "CC BY-ND", "CC BY-NC-ND", "CC BY-NC-SA", "Other"]  # noqa: E501
        if license not in allowed_values:
            raise ValueError(
                "Invalid value for `license` ({0}), must be one of {1}"  # noqa: E501
                .format(license, allowed_values)
            )

        self._license = license

    @property
    def linked_datasets(self):
        """Gets the linked_datasets of this ProjectCreateRequest.  # noqa: E501

        Initial set of linked datasets.  # noqa: E501

        :return: The linked_datasets of this ProjectCreateRequest.  # noqa: E501
        :rtype: list[LinkedDatasetCreateOrUpdateRequest]
        """
        return self._linked_datasets

    @linked_datasets.setter
    def linked_datasets(self, linked_datasets):
        """Sets the linked_datasets of this ProjectCreateRequest.

        Initial set of linked datasets.  # noqa: E501

        :param linked_datasets: The linked_datasets of this ProjectCreateRequest.  # noqa: E501
        :type: list[LinkedDatasetCreateOrUpdateRequest]
        """

        self._linked_datasets = linked_datasets

    @property
    def objective(self):
        """Gets the objective of this ProjectCreateRequest.  # noqa: E501

        Short project objective.  # noqa: E501

        :return: The objective of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this ProjectCreateRequest.

        Short project objective.  # noqa: E501

        :param objective: The objective of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """

        self._objective = objective

    @property
    def summary(self):
        """Gets the summary of this ProjectCreateRequest.  # noqa: E501

        Long-form project summary (Markdown supported).  # noqa: E501

        :return: The summary of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ProjectCreateRequest.

        Long-form project summary (Markdown supported).  # noqa: E501

        :param summary: The summary of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def tags(self):
        """Gets the tags of this ProjectCreateRequest.  # noqa: E501

        Project tags. Letters numbers and spaces only (max 25 characters).  # noqa: E501

        :return: The tags of this ProjectCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProjectCreateRequest.

        Project tags. Letters numbers and spaces only (max 25 characters).  # noqa: E501

        :param tags: The tags of this ProjectCreateRequest.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def title(self):
        """Gets the title of this ProjectCreateRequest.  # noqa: E501

        Project title.  # noqa: E501

        :return: The title of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProjectCreateRequest.

        Project title.  # noqa: E501

        :param title: The title of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def visibility(self):
        """Gets the visibility of this ProjectCreateRequest.  # noqa: E501

        Project visibility. `OPEN` if the project can be seen by any member of data.world. `PRIVATE` if the project can be seen by its owner and authorized collaborators.  # noqa: E501

        :return: The visibility of this ProjectCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ProjectCreateRequest.

        Project visibility. `OPEN` if the project can be seen by any member of data.world. `PRIVATE` if the project can be seen by its owner and authorized collaborators.  # noqa: E501

        :param visibility: The visibility of this ProjectCreateRequest.  # noqa: E501
        :type: str
        """
        if visibility is None:
            raise ValueError("Invalid value for `visibility`, must not be `None`")  # noqa: E501
        allowed_values = ["OPEN", "PRIVATE"]  # noqa: E501
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

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
        if issubclass(ProjectCreateRequest, dict):
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
        if not isinstance(other, ProjectCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

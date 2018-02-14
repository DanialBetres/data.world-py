# coding: utf-8

"""
    data.world API

    data.world is designed for data and the people who work with data.  From professional projects to open data, data.world helps you host and share your data, collaborate with your team, and capture context and conclusions as you work.   Using this API users are able to easily access data and manage their data projects regardless of language or tool of preference.  Check out our [documentation](https://dwapi.apidocs.io) for tips on how to get started, tutorials and to interact with the API right within your browser.

    OpenAPI spec version: 0.14.1
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProjectPutRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'title': 'str',
        'objective': 'str',
        'summary': 'str',
        'tags': 'list[str]',
        'license': 'str',
        'visibility': 'str',
        'files': 'list[FileCreateRequest]',
        'linked_datasets': 'list[LinkedDatasetCreateOrUpdateRequest]'
    }

    attribute_map = {
        'title': 'title',
        'objective': 'objective',
        'summary': 'summary',
        'tags': 'tags',
        'license': 'license',
        'visibility': 'visibility',
        'files': 'files',
        'linked_datasets': 'linkedDatasets'
    }

    def __init__(self, title=None, objective=None, summary=None, tags=None, license=None, visibility=None, files=None, linked_datasets=None):
        """
        ProjectPutRequest - a model defined in Swagger
        """

        self._title = None
        self._objective = None
        self._summary = None
        self._tags = None
        self._license = None
        self._visibility = None
        self._files = None
        self._linked_datasets = None

        self.title = title
        if objective is not None:
          self.objective = objective
        if summary is not None:
          self.summary = summary
        if tags is not None:
          self.tags = tags
        if license is not None:
          self.license = license
        self.visibility = visibility
        if files is not None:
          self.files = files
        if linked_datasets is not None:
          self.linked_datasets = linked_datasets

    @property
    def title(self):
        """
        Gets the title of this ProjectPutRequest.
        Project title.

        :return: The title of this ProjectPutRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ProjectPutRequest.
        Project title.

        :param title: The title of this ProjectPutRequest.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")
        if title is not None and len(title) > 60:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `60`")
        if title is not None and len(title) < 0:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `0`")

        self._title = title

    @property
    def objective(self):
        """
        Gets the objective of this ProjectPutRequest.
        Short project objective.

        :return: The objective of this ProjectPutRequest.
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """
        Sets the objective of this ProjectPutRequest.
        Short project objective.

        :param objective: The objective of this ProjectPutRequest.
        :type: str
        """
        if objective is not None and len(objective) > 120:
            raise ValueError("Invalid value for `objective`, length must be less than or equal to `120`")
        if objective is not None and len(objective) < 0:
            raise ValueError("Invalid value for `objective`, length must be greater than or equal to `0`")

        self._objective = objective

    @property
    def summary(self):
        """
        Gets the summary of this ProjectPutRequest.
        Long-form project summary (Markdown supported).

        :return: The summary of this ProjectPutRequest.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this ProjectPutRequest.
        Long-form project summary (Markdown supported).

        :param summary: The summary of this ProjectPutRequest.
        :type: str
        """
        if summary is not None and len(summary) > 25000:
            raise ValueError("Invalid value for `summary`, length must be less than or equal to `25000`")
        if summary is not None and len(summary) < 0:
            raise ValueError("Invalid value for `summary`, length must be greater than or equal to `0`")

        self._summary = summary

    @property
    def tags(self):
        """
        Gets the tags of this ProjectPutRequest.
        Project tags. Letters numbers and spaces only (max 25 characters).

        :return: The tags of this ProjectPutRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ProjectPutRequest.
        Project tags. Letters numbers and spaces only (max 25 characters).

        :param tags: The tags of this ProjectPutRequest.
        :type: list[str]
        """

        self._tags = tags

    @property
    def license(self):
        """
        Gets the license of this ProjectPutRequest.
        Project license. Find additional info for allowed values [here](https://data.world/license-help).

        :return: The license of this ProjectPutRequest.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """
        Sets the license of this ProjectPutRequest.
        Project license. Find additional info for allowed values [here](https://data.world/license-help).

        :param license: The license of this ProjectPutRequest.
        :type: str
        """
        allowed_values = ["Public Domain", "PDDL", "CC-0", "CC-BY", "ODC-BY", "CC-BY-SA", "ODC-ODbL", "CC BY-NC", "CC BY-NC-SA", "Other"]
        if license not in allowed_values:
            raise ValueError(
                "Invalid value for `license` ({0}), must be one of {1}"
                .format(license, allowed_values)
            )

        self._license = license

    @property
    def visibility(self):
        """
        Gets the visibility of this ProjectPutRequest.
        Project visibility. `OPEN` if the project can be seen by any member of data.world. `PRIVATE` if the project can be seen by its owner and authorized collaborators.

        :return: The visibility of this ProjectPutRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this ProjectPutRequest.
        Project visibility. `OPEN` if the project can be seen by any member of data.world. `PRIVATE` if the project can be seen by its owner and authorized collaborators.

        :param visibility: The visibility of this ProjectPutRequest.
        :type: str
        """
        if visibility is None:
            raise ValueError("Invalid value for `visibility`, must not be `None`")
        allowed_values = ["OPEN", "PRIVATE"]
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def files(self):
        """
        Gets the files of this ProjectPutRequest.
        Initial set of files. At project creation time, file uploads are not supported. However, this property can be used to add files from URL.

        :return: The files of this ProjectPutRequest.
        :rtype: list[FileCreateRequest]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this ProjectPutRequest.
        Initial set of files. At project creation time, file uploads are not supported. However, this property can be used to add files from URL.

        :param files: The files of this ProjectPutRequest.
        :type: list[FileCreateRequest]
        """

        self._files = files

    @property
    def linked_datasets(self):
        """
        Gets the linked_datasets of this ProjectPutRequest.
        Initial set of linked datasets.

        :return: The linked_datasets of this ProjectPutRequest.
        :rtype: list[LinkedDatasetCreateOrUpdateRequest]
        """
        return self._linked_datasets

    @linked_datasets.setter
    def linked_datasets(self, linked_datasets):
        """
        Sets the linked_datasets of this ProjectPutRequest.
        Initial set of linked datasets.

        :param linked_datasets: The linked_datasets of this ProjectPutRequest.
        :type: list[LinkedDatasetCreateOrUpdateRequest]
        """

        self._linked_datasets = linked_datasets

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ProjectPutRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

# coding: utf-8

"""
    data.world API

    # data.world in a nutshell  data.world is a productive, secure platform for modern data teamwork.  We bring together your data practitioners, subject matter experts, and other stakeholders by removing costly barriers to data discovery, comprehension, integration, and sharing.   Everything your team needs to quickly understand and use data stays with it.   Social features and integrations encourage collaborators to ask and answer questions, share discoveries, and coordinate closely while still using their preferred tools.  Our focus on interoperability helps you enhance your own data with data from any source, including our vast and growing library of free public datasets.   Sophisticated permissions, auditing features, and more make it easy to manage who views your data and what they do with it.  # Conventions  ## Authentication  All data.world API calls require an API token.   OAuth2 is the preferred and most secure method for authenticating users of your data.world applications. Visit our [oauth documentation](https://apidocs.data.world/toolkit/oauth) for additional information. Alternatively, you can obtain a token for _personal use or testing_ by navigating to your profile settings, under the Advanced tab ([https://data.world/settings/advanced](https://data.world/settings/advanced)).  Authentication must be provided in API requests via the `Authorization` header. For example, for a user whose API token is `my_api_token`, the request header should be `Authorization: Bearer my_api_token` (note the `Bearer` prefix).  ## Content type   By default, `application/json` is the content type used in request and response bodies. Exceptions are noted in respective endpoint documentation.  ## HTTPS only   Our APIs can only be accessed via HTTPS.  # Interested in building data.world apps?  Check out our [developer portal](https://apidocs.data.world) for tips on how to get started, tutorials, and to interact with the API endpoints right within your browser.

    OpenAPI spec version: 0.21.0
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MetadatarelationshipsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_relationship(self, owner, body, **kwargs):
        """
        Create a relationship between two resources
        Create a relationship between two resources. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_relationship(owner, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param RelationshipCreateOrDeleteRequest body: (required)
        :return: EditActivitiesResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_relationship_with_http_info(owner, body, **kwargs)
        else:
            (data) = self.create_relationship_with_http_info(owner, body, **kwargs)
            return data

    def create_relationship_with_http_info(self, owner, body, **kwargs):
        """
        Create a relationship between two resources
        Create a relationship between two resources. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_relationship_with_http_info(owner, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param RelationshipCreateOrDeleteRequest body: (required)
        :return: EditActivitiesResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_relationship" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `create_relationship`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_relationship`")

        if 'owner' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['owner']):
            raise ValueError("Invalid value for parameter `owner` when calling `create_relationship`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['token']

        return self.api_client.call_api('/metadata/relationships/{owner}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EditActivitiesResultDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_relationship(self, owner, body, **kwargs):
        """
        Delete a relationship between two resources
        Delete a relationship between two resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_relationship(owner, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param RelationshipCreateOrDeleteRequest body: (required)
        :return: EditActivitiesResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_relationship_with_http_info(owner, body, **kwargs)
        else:
            (data) = self.delete_relationship_with_http_info(owner, body, **kwargs)
            return data

    def delete_relationship_with_http_info(self, owner, body, **kwargs):
        """
        Delete a relationship between two resources
        Delete a relationship between two resources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_relationship_with_http_info(owner, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param RelationshipCreateOrDeleteRequest body: (required)
        :return: EditActivitiesResultDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_relationship" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `delete_relationship`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_relationship`")

        if 'owner' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['owner']):
            raise ValueError("Invalid value for parameter `owner` when calling `delete_relationship`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['token']

        return self.api_client.call_api('/metadata/relationships/{owner}/delete', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EditActivitiesResultDto',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_relationships(self, owner, resource_id, body, **kwargs):
        """
        Get related resources for a given resource id
        Get a list of resources related to a particular resource specified by id. For example, you may use this endpoint to retrieve a list of business glossary terms related to an analysis dashboard. The resourceType param in the request body is required. Results may be filtered by resource type (byResourceTypes) or by relationship type (byRelationTypes).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_relationships(owner, resource_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str resource_id: Unique identifier for the resource you would like to retrieve related resources for. The resourceid can be found in the URL for the resource in the data.world UI. (required)
        :param RelationshipGetRequest body: (required)
        :param str limit:
        :param str next:
        :return: PaginatedMetadataResourceResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_relationships_with_http_info(owner, resource_id, body, **kwargs)
        else:
            (data) = self.get_relationships_with_http_info(owner, resource_id, body, **kwargs)
            return data

    def get_relationships_with_http_info(self, owner, resource_id, body, **kwargs):
        """
        Get related resources for a given resource id
        Get a list of resources related to a particular resource specified by id. For example, you may use this endpoint to retrieve a list of business glossary terms related to an analysis dashboard. The resourceType param in the request body is required. Results may be filtered by resource type (byResourceTypes) or by relationship type (byRelationTypes).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_relationships_with_http_info(owner, resource_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str resource_id: Unique identifier for the resource you would like to retrieve related resources for. The resourceid can be found in the URL for the resource in the data.world UI. (required)
        :param RelationshipGetRequest body: (required)
        :param str limit:
        :param str next:
        :return: PaginatedMetadataResourceResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'resource_id', 'body', 'limit', 'next']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_relationships" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `get_relationships`")
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params) or (params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `get_relationships`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_relationships`")

        if 'owner' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['owner']):
            raise ValueError("Invalid value for parameter `owner` when calling `get_relationships`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'next' in params:
            query_params.append(('next', params['next']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['token']

        return self.api_client.call_api('/metadata/relationships/{owner}/resource/{resourceId}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaginatedMetadataResourceResults',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_table_relationships(self, owner, source_id, table_id, **kwargs):
        """
        Get resources related to a table
        Get resources related to a table
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_table_relationships(owner, source_id, table_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str source_id: (required)
        :param str table_id: (required)
        :param RelationshipGetTableRequest body:
        :param str limit:
        :param str next:
        :return: PaginatedMetadataResourceResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_table_relationships_with_http_info(owner, source_id, table_id, **kwargs)
        else:
            (data) = self.get_table_relationships_with_http_info(owner, source_id, table_id, **kwargs)
            return data

    def get_table_relationships_with_http_info(self, owner, source_id, table_id, **kwargs):
        """
        Get resources related to a table
        Get resources related to a table
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_table_relationships_with_http_info(owner, source_id, table_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str source_id: (required)
        :param str table_id: (required)
        :param RelationshipGetTableRequest body:
        :param str limit:
        :param str next:
        :return: PaginatedMetadataResourceResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'source_id', 'table_id', 'body', 'limit', 'next']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_table_relationships" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `get_table_relationships`")
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `get_table_relationships`")
        # verify the required parameter 'table_id' is set
        if ('table_id' not in params) or (params['table_id'] is None):
            raise ValueError("Missing the required parameter `table_id` when calling `get_table_relationships`")

        if 'owner' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['owner']):
            raise ValueError("Invalid value for parameter `owner` when calling `get_table_relationships`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']
        if 'source_id' in params:
            path_params['sourceId'] = params['source_id']
        if 'table_id' in params:
            path_params['tableId'] = params['table_id']

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'next' in params:
            query_params.append(('next', params['next']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['token']

        return self.api_client.call_api('/metadata/relationships/{owner}/table/{sourceId}/{tableId}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaginatedMetadataResourceResults',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

# coding: utf-8

# flake8: noqa
"""
    data.world API

    # data.world in a nutshell  data.world is a productive, secure platform for modern data teamwork.  We bring together your data practitioners, subject matter experts, and other stakeholders by removing costly barriers to data discovery, comprehension, integration, and sharing.   Everything your team needs to quickly understand and use data stays with it.   Social features and integrations encourage collaborators to ask and answer questions, share discoveries, and coordinate closely while still using their preferred tools.  Our focus on interoperability helps you enhance your own data with data from any source, including our vast and growing library of free public datasets.   Sophisticated permissions, auditing features, and more make it easy to manage who views your data and what they do with it.  # Conventions  ## Authentication  All data.world API calls require an API token.   OAuth2 is the preferred and most secure method for authenticating users of your data.world applications. Visit our [oauth documentation](https://apidocs.data.world/toolkit/oauth) for additional information. Alternatively, you can obtain a token for _personal use or testing_ by navigating to your profile settings, under the Advanced tab ([https://data.world/settings/advanced](https://data.world/settings/advanced)).  Authentication must be provided in API requests via the `Authorization` header. For example, for a user whose API token is `my_api_token`, the request header should be `Authorization: Bearer my_api_token` (note the `Bearer` prefix).  ## Content type   By default, `application/json` is the content type used in request and response bodies. Exceptions are noted in respective endpoint documentation.  ## HTTPS only   Our APIs can only be accessed via HTTPS.  # Interested in building data.world apps?  Check out our [developer portal](https://apidocs.data.world) for tips on how to get started, tutorials, and to interact with the API endpoints right within your browser.  # noqa: E501

    OpenAPI spec version: 0.21.0
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from _swagger.models.agent_hydration_dto import AgentHydrationDto
from _swagger.models.analysis_image import AnalysisImage
from _swagger.models.asset_status import AssetStatus
from _swagger.models.body import Body
from _swagger.models.body1 import Body1
from _swagger.models.catalog_analysis_hydration_dto import CatalogAnalysisHydrationDto
from _swagger.models.catalog_analysis_request import CatalogAnalysisRequest
from _swagger.models.catalog_business_term_hydration_dto import CatalogBusinessTermHydrationDto
from _swagger.models.catalog_column_hydration_dto import CatalogColumnHydrationDto
from _swagger.models.catalog_column_request import CatalogColumnRequest
from _swagger.models.catalog_concept_hydration_dto import CatalogConceptHydrationDto
from _swagger.models.catalog_glossary_request import CatalogGlossaryRequest
from _swagger.models.catalog_hydration_dto import CatalogHydrationDto
from _swagger.models.catalog_id import CatalogId
from _swagger.models.catalog_request import CatalogRequest
from _swagger.models.catalog_table_hydration_dto import CatalogTableHydrationDto
from _swagger.models.catalog_table_request import CatalogTableRequest
from _swagger.models.concept_entry import ConceptEntry
from _swagger.models.connection_dto import ConnectionDto
from _swagger.models.create_dataset_response import CreateDatasetResponse
from _swagger.models.create_insight_response import CreateInsightResponse
from _swagger.models.create_project_response import CreateProjectResponse
from _swagger.models.create_query_request import CreateQueryRequest
from _swagger.models.create_response import CreateResponse
from _swagger.models.custom_dataset_or_project_metadata_request import CustomDatasetOrProjectMetadataRequest
from _swagger.models.database_credentials import DatabaseCredentials
from _swagger.models.database_dbo import DatabaseDbo
from _swagger.models.database_source_reference import DatabaseSourceReference
from _swagger.models.dataset_create_request import DatasetCreateRequest
from _swagger.models.dataset_hydration_dto import DatasetHydrationDto
from _swagger.models.dataset_identifier import DatasetIdentifier
from _swagger.models.dataset_patch_request import DatasetPatchRequest
from _swagger.models.dataset_put_request import DatasetPutRequest
from _swagger.models.dataset_summary_response import DatasetSummaryResponse
from _swagger.models.doi import Doi
from _swagger.models.edit_activities_result_dto import EditActivitiesResultDto
from _swagger.models.entry_type import EntryType
from _swagger.models.error_message import ErrorMessage
from _swagger.models.file_batch_update_request import FileBatchUpdateRequest
from _swagger.models.file_create_or_update_request import FileCreateOrUpdateRequest
from _swagger.models.file_create_request import FileCreateRequest
from _swagger.models.file_source_create_or_update_request import FileSourceCreateOrUpdateRequest
from _swagger.models.file_source_create_request import FileSourceCreateRequest
from _swagger.models.file_source_summary_response import FileSourceSummaryResponse
from _swagger.models.file_summary_response import FileSummaryResponse
from _swagger.models.form_data_form_query import FormDataFormQuery
from _swagger.models.insight_body import InsightBody
from _swagger.models.insight_create_request import InsightCreateRequest
from _swagger.models.insight_hydration_dto import InsightHydrationDto
from _swagger.models.insight_patch_request import InsightPatchRequest
from _swagger.models.insight_put_request import InsightPutRequest
from _swagger.models.insight_summary_response import InsightSummaryResponse
from _swagger.models.instant import Instant
from _swagger.models.json_node import JsonNode
from _swagger.models.linked_dataset_create_or_update_request import LinkedDatasetCreateOrUpdateRequest
from _swagger.models.linked_dataset_summary_response import LinkedDatasetSummaryResponse
from _swagger.models.metadata_resource_dto import MetadataResourceDto
from _swagger.models.oauth_token_reference import OauthTokenReference
from _swagger.models.paginated_connection_results import PaginatedConnectionResults
from _swagger.models.paginated_dataset_results import PaginatedDatasetResults
from _swagger.models.paginated_insight_results import PaginatedInsightResults
from _swagger.models.paginated_metadata_resource_results import PaginatedMetadataResourceResults
from _swagger.models.paginated_project_results import PaginatedProjectResults
from _swagger.models.paginated_query_results import PaginatedQueryResults
from _swagger.models.paginated_search_results_dto import PaginatedSearchResultsDto
from _swagger.models.paginated_subscription_results import PaginatedSubscriptionResults
from _swagger.models.project_create_request import ProjectCreateRequest
from _swagger.models.project_patch_request import ProjectPatchRequest
from _swagger.models.project_put_request import ProjectPutRequest
from _swagger.models.project_summary_response import ProjectSummaryResponse
from _swagger.models.query_parameter import QueryParameter
from _swagger.models.query_put_request import QueryPutRequest
from _swagger.models.query_summary_response import QuerySummaryResponse
from _swagger.models.range import Range
from _swagger.models.rdf_term import RdfTerm
from _swagger.models.relationship_create_or_delete_request import RelationshipCreateOrDeleteRequest
from _swagger.models.relationship_get_request import RelationshipGetRequest
from _swagger.models.relationship_get_table_request import RelationshipGetTableRequest
from _swagger.models.resource_relationship_dto import ResourceRelationshipDto
from _swagger.models.saved_query_execution_request import SavedQueryExecutionRequest
from _swagger.models.search_facet_result import SearchFacetResult
from _swagger.models.search_hydrations import SearchHydrations
from _swagger.models.search_request import SearchRequest
from _swagger.models.simple_search_request import SimpleSearchRequest
from _swagger.models.single_table_metadata_spec import SingleTableMetadataSpec
from _swagger.models.source_id import SourceId
from _swagger.models.sql_query_request import SqlQueryRequest
from _swagger.models.ssh_tunnel import SshTunnel
from _swagger.models.stream_schema import StreamSchema
from _swagger.models.stream_schema_patch_request import StreamSchemaPatchRequest
from _swagger.models.subscription import Subscription
from _swagger.models.subscription_api_links import SubscriptionApiLinks
from _swagger.models.subscription_create_request import SubscriptionCreateRequest
from _swagger.models.subscription_links import SubscriptionLinks
from _swagger.models.success_message import SuccessMessage
from _swagger.models.table_batch_update_request import TableBatchUpdateRequest
from _swagger.models.table_create_or_update_request import TableCreateOrUpdateRequest
from _swagger.models.table_id import TableId
from _swagger.models.table_source_create_or_update_request import TableSourceCreateOrUpdateRequest
from _swagger.models.tag import Tag
from _swagger.models.user_data_response import UserDataResponse
from _swagger.models.user_identifier import UserIdentifier
from _swagger.models.web_authorization import WebAuthorization
from _swagger.models.web_credentials import WebCredentials

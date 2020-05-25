# coding: utf-8

"""
    Yahoo!広告 検索広告 API リファレンス / Yahoo! Ads Search Ads API Reference

    <div lang=\"ja\">Yahoo!広告 検索広告 APIのWebサービスについて説明します。<br> 「Try it out」のご利用には、事前にアプリケーションの登録が必要です。また、アプリケーションのリダイレクトURIの1つに<br> https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.htmlを登録してください。 </div> <div lang=\"en\">Search Ads API Web Services supported in Yahoo! Ads API.<br> When you use \"Try it out\", you need to register your application in advance.<br> As one of redirect URI for application, you need to set \"https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.html\". </div>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yahoo_ads_search.configuration import Configuration


class ReportDefinition(object):
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
        'account_id': 'int',
        'complete_time': 'str',
        'date_range': 'ReportDefinitionServiceReportDateRange',
        'fields': 'list[str]',
        'filters': 'list[ReportDefinitionServiceReportFilter]',
        'report_compress_type': 'ReportDefinitionServiceReportCompressType',
        'report_date_range_type': 'ReportDefinitionServiceReportDateRangeType',
        'report_download_encode': 'ReportDefinitionServiceReportDownloadEncode',
        'report_download_format': 'ReportDefinitionServiceReportDownloadFormat',
        'report_include_deleted': 'ReportDefinitionServiceReportIncludeDeleted',
        'report_include_zero_impressions': 'ReportDefinitionServiceReportIncludeZeroImpressions',
        'report_job_error_detail': 'str',
        'report_job_id': 'int',
        'report_job_status': 'ReportDefinitionServiceReportJobStatus',
        'report_language': 'ReportDefinitionServiceReportLanguage',
        'report_name': 'str',
        'report_type': 'ReportDefinitionServiceReportType',
        'request_time': 'str',
        'sort_fields': 'list[ReportDefinitionServiceReportSortField]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'complete_time': 'completeTime',
        'date_range': 'dateRange',
        'fields': 'fields',
        'filters': 'filters',
        'report_compress_type': 'reportCompressType',
        'report_date_range_type': 'reportDateRangeType',
        'report_download_encode': 'reportDownloadEncode',
        'report_download_format': 'reportDownloadFormat',
        'report_include_deleted': 'reportIncludeDeleted',
        'report_include_zero_impressions': 'reportIncludeZeroImpressions',
        'report_job_error_detail': 'reportJobErrorDetail',
        'report_job_id': 'reportJobId',
        'report_job_status': 'reportJobStatus',
        'report_language': 'reportLanguage',
        'report_name': 'reportName',
        'report_type': 'reportType',
        'request_time': 'requestTime',
        'sort_fields': 'sortFields'
    }

    def __init__(self, account_id=None, complete_time=None, date_range=None, fields=None, filters=None, report_compress_type=None, report_date_range_type=None, report_download_encode=None, report_download_format=None, report_include_deleted=None, report_include_zero_impressions=None, report_job_error_detail=None, report_job_id=None, report_job_status=None, report_language=None, report_name=None, report_type=None, request_time=None, sort_fields=None, local_vars_configuration=None):  # noqa: E501
        """ReportDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._complete_time = None
        self._date_range = None
        self._fields = None
        self._filters = None
        self._report_compress_type = None
        self._report_date_range_type = None
        self._report_download_encode = None
        self._report_download_format = None
        self._report_include_deleted = None
        self._report_include_zero_impressions = None
        self._report_job_error_detail = None
        self._report_job_id = None
        self._report_job_status = None
        self._report_language = None
        self._report_name = None
        self._report_type = None
        self._request_time = None
        self._sort_fields = None
        self.discriminator = None

        self.account_id = account_id
        self.complete_time = complete_time
        self.date_range = date_range
        self.fields = fields
        self.filters = filters
        self.report_compress_type = report_compress_type
        self.report_date_range_type = report_date_range_type
        self.report_download_encode = report_download_encode
        self.report_download_format = report_download_format
        self.report_include_deleted = report_include_deleted
        self.report_include_zero_impressions = report_include_zero_impressions
        self.report_job_error_detail = report_job_error_detail
        self.report_job_id = report_job_id
        self.report_job_status = report_job_status
        self.report_language = report_language
        self.report_name = report_name
        self.report_type = report_type
        self.request_time = request_time
        self.sort_fields = sort_fields

    @property
    def account_id(self):
        """Gets the account_id of this ReportDefinition.  # noqa: E501

        <div lang=\"ja\">アカウントIDです。</div> <div lang=\"en\">Account ID.</div>   # noqa: E501

        :return: The account_id of this ReportDefinition.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ReportDefinition.

        <div lang=\"ja\">アカウントIDです。</div> <div lang=\"en\">Account ID.</div>   # noqa: E501

        :param account_id: The account_id of this ReportDefinition.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def complete_time(self):
        """Gets the complete_time of this ReportDefinition.  # noqa: E501

        <div lang=\"ja\">ジョブの完了時刻です。<br> ※YYYY/MM/DD hh:mm:ss形式になります。<br> ※hhは24時間表記になります。</div> <div lang=\"en\">Completion time of Report Job request.<br> *Displays in YYYY/MM/DD hh:mm:ss form.<br> *hh will display in 24-hour time.</div>   # noqa: E501

        :return: The complete_time of this ReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._complete_time

    @complete_time.setter
    def complete_time(self, complete_time):
        """Sets the complete_time of this ReportDefinition.

        <div lang=\"ja\">ジョブの完了時刻です。<br> ※YYYY/MM/DD hh:mm:ss形式になります。<br> ※hhは24時間表記になります。</div> <div lang=\"en\">Completion time of Report Job request.<br> *Displays in YYYY/MM/DD hh:mm:ss form.<br> *hh will display in 24-hour time.</div>   # noqa: E501

        :param complete_time: The complete_time of this ReportDefinition.  # noqa: E501
        :type: str
        """

        self._complete_time = complete_time

    @property
    def date_range(self):
        """Gets the date_range of this ReportDefinition.  # noqa: E501


        :return: The date_range of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportDateRange
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        """Sets the date_range of this ReportDefinition.


        :param date_range: The date_range of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportDateRange
        """

        self._date_range = date_range

    @property
    def fields(self):
        """Gets the fields of this ReportDefinition.  # noqa: E501

        <div lang=\"ja\">フィールド（レポートの出力項目名）です。<br> ADD時、このフィールドは必須となります。</div> <div lang=\"en\">Item name of the report.<br> Can appoint the value retrieved from getReportFields.<br> This field is required in ADD operation.</div>   # noqa: E501

        :return: The fields of this ReportDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ReportDefinition.

        <div lang=\"ja\">フィールド（レポートの出力項目名）です。<br> ADD時、このフィールドは必須となります。</div> <div lang=\"en\">Item name of the report.<br> Can appoint the value retrieved from getReportFields.<br> This field is required in ADD operation.</div>   # noqa: E501

        :param fields: The fields of this ReportDefinition.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

    @property
    def filters(self):
        """Gets the filters of this ReportDefinition.  # noqa: E501


        :return: The filters of this ReportDefinition.  # noqa: E501
        :rtype: list[ReportDefinitionServiceReportFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ReportDefinition.


        :param filters: The filters of this ReportDefinition.  # noqa: E501
        :type: list[ReportDefinitionServiceReportFilter]
        """

        self._filters = filters

    @property
    def report_compress_type(self):
        """Gets the report_compress_type of this ReportDefinition.  # noqa: E501


        :return: The report_compress_type of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportCompressType
        """
        return self._report_compress_type

    @report_compress_type.setter
    def report_compress_type(self, report_compress_type):
        """Sets the report_compress_type of this ReportDefinition.


        :param report_compress_type: The report_compress_type of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportCompressType
        """

        self._report_compress_type = report_compress_type

    @property
    def report_date_range_type(self):
        """Gets the report_date_range_type of this ReportDefinition.  # noqa: E501


        :return: The report_date_range_type of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportDateRangeType
        """
        return self._report_date_range_type

    @report_date_range_type.setter
    def report_date_range_type(self, report_date_range_type):
        """Sets the report_date_range_type of this ReportDefinition.


        :param report_date_range_type: The report_date_range_type of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportDateRangeType
        """

        self._report_date_range_type = report_date_range_type

    @property
    def report_download_encode(self):
        """Gets the report_download_encode of this ReportDefinition.  # noqa: E501


        :return: The report_download_encode of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportDownloadEncode
        """
        return self._report_download_encode

    @report_download_encode.setter
    def report_download_encode(self, report_download_encode):
        """Sets the report_download_encode of this ReportDefinition.


        :param report_download_encode: The report_download_encode of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportDownloadEncode
        """

        self._report_download_encode = report_download_encode

    @property
    def report_download_format(self):
        """Gets the report_download_format of this ReportDefinition.  # noqa: E501


        :return: The report_download_format of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportDownloadFormat
        """
        return self._report_download_format

    @report_download_format.setter
    def report_download_format(self, report_download_format):
        """Sets the report_download_format of this ReportDefinition.


        :param report_download_format: The report_download_format of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportDownloadFormat
        """

        self._report_download_format = report_download_format

    @property
    def report_include_deleted(self):
        """Gets the report_include_deleted of this ReportDefinition.  # noqa: E501


        :return: The report_include_deleted of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportIncludeDeleted
        """
        return self._report_include_deleted

    @report_include_deleted.setter
    def report_include_deleted(self, report_include_deleted):
        """Sets the report_include_deleted of this ReportDefinition.


        :param report_include_deleted: The report_include_deleted of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportIncludeDeleted
        """

        self._report_include_deleted = report_include_deleted

    @property
    def report_include_zero_impressions(self):
        """Gets the report_include_zero_impressions of this ReportDefinition.  # noqa: E501


        :return: The report_include_zero_impressions of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportIncludeZeroImpressions
        """
        return self._report_include_zero_impressions

    @report_include_zero_impressions.setter
    def report_include_zero_impressions(self, report_include_zero_impressions):
        """Sets the report_include_zero_impressions of this ReportDefinition.


        :param report_include_zero_impressions: The report_include_zero_impressions of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportIncludeZeroImpressions
        """

        self._report_include_zero_impressions = report_include_zero_impressions

    @property
    def report_job_error_detail(self):
        """Gets the report_job_error_detail of this ReportDefinition.  # noqa: E501

        <div lang=\"ja\">レポートジョブのエラー詳細です。</div> <div lang=\"en\">Error details of Report Job.</div>   # noqa: E501

        :return: The report_job_error_detail of this ReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._report_job_error_detail

    @report_job_error_detail.setter
    def report_job_error_detail(self, report_job_error_detail):
        """Sets the report_job_error_detail of this ReportDefinition.

        <div lang=\"ja\">レポートジョブのエラー詳細です。</div> <div lang=\"en\">Error details of Report Job.</div>   # noqa: E501

        :param report_job_error_detail: The report_job_error_detail of this ReportDefinition.  # noqa: E501
        :type: str
        """

        self._report_job_error_detail = report_job_error_detail

    @property
    def report_job_id(self):
        """Gets the report_job_id of this ReportDefinition.  # noqa: E501

        <div lang=\"ja\">レポートジョブIDです。<br> REMOVE時、このフィールドは必須となります。</div> <div lang=\"en\">Report Job ID.<br> This field is required in REMOVE operation.</div>   # noqa: E501

        :return: The report_job_id of this ReportDefinition.  # noqa: E501
        :rtype: int
        """
        return self._report_job_id

    @report_job_id.setter
    def report_job_id(self, report_job_id):
        """Sets the report_job_id of this ReportDefinition.

        <div lang=\"ja\">レポートジョブIDです。<br> REMOVE時、このフィールドは必須となります。</div> <div lang=\"en\">Report Job ID.<br> This field is required in REMOVE operation.</div>   # noqa: E501

        :param report_job_id: The report_job_id of this ReportDefinition.  # noqa: E501
        :type: int
        """

        self._report_job_id = report_job_id

    @property
    def report_job_status(self):
        """Gets the report_job_status of this ReportDefinition.  # noqa: E501


        :return: The report_job_status of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportJobStatus
        """
        return self._report_job_status

    @report_job_status.setter
    def report_job_status(self, report_job_status):
        """Sets the report_job_status of this ReportDefinition.


        :param report_job_status: The report_job_status of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportJobStatus
        """

        self._report_job_status = report_job_status

    @property
    def report_language(self):
        """Gets the report_language of this ReportDefinition.  # noqa: E501


        :return: The report_language of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportLanguage
        """
        return self._report_language

    @report_language.setter
    def report_language(self, report_language):
        """Sets the report_language of this ReportDefinition.


        :param report_language: The report_language of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportLanguage
        """

        self._report_language = report_language

    @property
    def report_name(self):
        """Gets the report_name of this ReportDefinition.  # noqa: E501

        <div lang=\"ja\">レポート名称です。<br> ADD時、このフィールドは必須となります。</div> <div lang=\"en\">Name of the report.<br> This field is required in ADD operation.</div>   # noqa: E501

        :return: The report_name of this ReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this ReportDefinition.

        <div lang=\"ja\">レポート名称です。<br> ADD時、このフィールドは必須となります。</div> <div lang=\"en\">Name of the report.<br> This field is required in ADD operation.</div>   # noqa: E501

        :param report_name: The report_name of this ReportDefinition.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def report_type(self):
        """Gets the report_type of this ReportDefinition.  # noqa: E501


        :return: The report_type of this ReportDefinition.  # noqa: E501
        :rtype: ReportDefinitionServiceReportType
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ReportDefinition.


        :param report_type: The report_type of this ReportDefinition.  # noqa: E501
        :type: ReportDefinitionServiceReportType
        """

        self._report_type = report_type

    @property
    def request_time(self):
        """Gets the request_time of this ReportDefinition.  # noqa: E501

        <div lang=\"ja\">ジョブの起動時刻です。<br> ※YYYY/MM/DD hh:mm:ss形式になります。<br> ※hhは24時間表記になります。</div> <div lang=\"en\">Start time of Report Job request.<br> *Displays in YYYY/MM/DD hh:mm:ss form.<br> *hh will display in 24-hour time.</div>   # noqa: E501

        :return: The request_time of this ReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """Sets the request_time of this ReportDefinition.

        <div lang=\"ja\">ジョブの起動時刻です。<br> ※YYYY/MM/DD hh:mm:ss形式になります。<br> ※hhは24時間表記になります。</div> <div lang=\"en\">Start time of Report Job request.<br> *Displays in YYYY/MM/DD hh:mm:ss form.<br> *hh will display in 24-hour time.</div>   # noqa: E501

        :param request_time: The request_time of this ReportDefinition.  # noqa: E501
        :type: str
        """

        self._request_time = request_time

    @property
    def sort_fields(self):
        """Gets the sort_fields of this ReportDefinition.  # noqa: E501


        :return: The sort_fields of this ReportDefinition.  # noqa: E501
        :rtype: list[ReportDefinitionServiceReportSortField]
        """
        return self._sort_fields

    @sort_fields.setter
    def sort_fields(self, sort_fields):
        """Sets the sort_fields of this ReportDefinition.


        :param sort_fields: The sort_fields of this ReportDefinition.  # noqa: E501
        :type: list[ReportDefinitionServiceReportSortField]
        """

        self._sort_fields = sort_fields

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
        if not isinstance(other, ReportDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportDefinition):
            return True

        return self.to_dict() != other.to_dict()
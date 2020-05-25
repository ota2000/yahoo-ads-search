# coding: utf-8

"""
    Yahoo!広告 検索広告 API リファレンス / Yahoo! Ads Search Ads API Reference

    <div lang=\"ja\">Yahoo!広告 検索広告 APIのWebサービスについて説明します。<br> 「Try it out」のご利用には、事前にアプリケーションの登録が必要です。また、アプリケーションのリダイレクトURIの1つに<br> https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.htmlを登録してください。 </div> <div lang=\"en\">Search Ads API Web Services supported in Yahoo! Ads API.<br> When you use \"Try it out\", you need to register your application in advance.<br> As one of redirect URI for application, you need to set \"https://yahoojp-marketing.github.io/ads-search-api-documents/oauth2-redirect.html\". </div>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yahoo_ads_search
from yahoo_ads_search.models.campaign_target_service_value import CampaignTargetServiceValue  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestCampaignTargetServiceValue(unittest.TestCase):
    """CampaignTargetServiceValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CampaignTargetServiceValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.campaign_target_service_value.CampaignTargetServiceValue()  # noqa: E501
        if include_optional :
            return CampaignTargetServiceValue(
                campaign_target = yahoo_ads_search.models.campaign_target.CampaignTarget(
                    account_id = 56,
                    bid_multiplier = 1.337,
                    campaign_id = 56,
                    campaign_name = '0',
                    target = yahoo_ads_search.models.campaign_target_service_target.CampaignTargetServiceTarget(
                        location_target = yahoo_ads_search.models.campaign_target_service_location_target.CampaignTargetServiceLocationTarget(
                            city_name_en = '0',
                            city_name_ja = '0',
                            excluded_type = 'INCLUDED',
                            province_name_en = '0',
                            province_name_ja = '0',
                            targeting_status = 'ACTIVE', ),
                        network_target = yahoo_ads_search.models.campaign_target_service_network_target.CampaignTargetServiceNetworkTarget(
                            network_coverage_type = 'YAHOO_SEARCH', ),
                        platform_target = yahoo_ads_search.models.campaign_target_service_platform_target.CampaignTargetServicePlatformTarget(
                            platform_type = 'SMART_PHONE', ),
                        schedule_target = yahoo_ads_search.models.campaign_target_service_schedule_target.CampaignTargetServiceScheduleTarget(
                            day_of_week = 'MONDAY',
                            end_hour = 56,
                            end_minute = 'ZERO',
                            start_hour = 56,
                            start_minute = 'ZERO', ),
                        target_id = '0',
                        target_type = 'LOCATION', ), ),
                errors = [
                    yahoo_ads_search.models.error.Error(
                        code = '0',
                        message = '0',
                        details = [
                            yahoo_ads_search.models.error_detail.ErrorDetail(
                                request_key = '0',
                                request_value = '0', )
                            ], )
                    ],
                operation_succeeded = True
            )
        else :
            return CampaignTargetServiceValue(
        )

    def testCampaignTargetServiceValue(self):
        """Test CampaignTargetServiceValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
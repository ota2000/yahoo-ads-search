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
from yahoo_ads_search.models.retargeting_list_service_targeting_list import RetargetingListServiceTargetingList  # noqa: E501
from yahoo_ads_search.rest import ApiException

class TestRetargetingListServiceTargetingList(unittest.TestCase):
    """RetargetingListServiceTargetingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RetargetingListServiceTargetingList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_search.models.retargeting_list_service_targeting_list.RetargetingListServiceTargetingList()  # noqa: E501
        if include_optional :
            return RetargetingListServiceTargetingList(
                account_id = 56,
                closing_reason = 'UNUSED_LIST',
                default_target_list = yahoo_ads_search.models.retargeting_list_service_default_target_list.RetargetingListServiceDefaultTargetList(
                    tag = yahoo_ads_search.models.retargeting_list_service_tag.RetargetingListServiceTag(
                        snippet = '0',
                        advanced_snippet = '0', ), ),
                logical_target_list = yahoo_ads_search.models.retargeting_list_service_logical_target_list.RetargetingListServiceLogicalTargetList(
                    logical_group = [
                        yahoo_ads_search.models.retargeting_list_service_logical_group.RetargetingListServiceLogicalGroup(
                            logical_condition = 'AND',
                            logical_operand = [
                                yahoo_ads_search.models.retargeting_list_service_logical_rule_operand.RetargetingListServiceLogicalRuleOperand(
                                    target_list_id = 56, )
                                ], )
                        ], ),
                reach = 56,
                reach_storage_span = 56,
                reach_storage_status = 'OPEN',
                retargeting_account_status = yahoo_ads_search.models.retargeting_list_service_retargeting_account_status.RetargetingListServiceRetargetingAccountStatus(
                    agree_date = '0',
                    review_request_date = '0',
                    review_status = 'APPROVED', ),
                rule_base_target_list = yahoo_ads_search.models.retargeting_list_service_rule_base_target_list.RetargetingListServiceRuleBaseTargetList(
                    end_date = '0',
                    is_all_visitor_rule = 'TRUE',
                    is_date_specific_rule = 'TRUE',
                    rules = [
                        yahoo_ads_search.models.retargeting_list_service_rule_group.RetargetingListServiceRuleGroup(
                            rule_items = [
                                yahoo_ads_search.models.retargeting_list_service_rule_item.RetargetingListServiceRuleItem(
                                    custom_key_rule_item = yahoo_ads_search.models.retargeting_list_service_custom_key_rule_item.RetargetingListServiceCustomKeyRuleItem(
                                        text_key = '0', ),
                                    rule_operator = 'UNKNOWN',
                                    rule_type = 'URL_RULE',
                                    url_rule_item = yahoo_ads_search.models.retargeting_list_service_url_rule_item.RetargetingListServiceUrlRuleItem(
                                        url_rule_key = 'URL', ),
                                    value = '0', )
                                ], )
                        ],
                    start_date = '0', ),
                target_list_description = '0',
                target_list_id = 56,
                target_list_name = '0',
                target_list_owner = 'OWNER',
                target_list_track_id = 56,
                target_list_type = 'DEFAULT'
            )
        else :
            return RetargetingListServiceTargetingList(
        )

    def testRetargetingListServiceTargetingList(self):
        """Test RetargetingListServiceTargetingList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
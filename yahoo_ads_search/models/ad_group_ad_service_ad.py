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


class AdGroupAdServiceAd(object):
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
        'ad_type': 'AdGroupAdServiceAdType',
        'additional_advanced_mobile_urls': 'list[AdGroupAdServiceAdditionalAdvancedMobileUrls]',
        'additional_advanced_urls': 'list[AdGroupAdServiceAdditionalAdvancedUrls]',
        'advanced_mobile_url': 'str',
        'advanced_url': 'str',
        'app_ad': 'AdGroupAdServiceAppAd',
        'custom_parameters': 'AdGroupAdServiceCustomParameters',
        'description': 'str',
        'device_preference': 'AdGroupAdServiceDevicePreference',
        'display_url': 'str',
        'extended_text_ad': 'AdGroupAdServiceExtendedTextAd',
        'headline': 'str',
        'text_ad2': 'AdGroupAdServiceTextAd2',
        'tracking_url': 'str',
        'url': 'str'
    }

    attribute_map = {
        'ad_type': 'adType',
        'additional_advanced_mobile_urls': 'additionalAdvancedMobileUrls',
        'additional_advanced_urls': 'additionalAdvancedUrls',
        'advanced_mobile_url': 'advancedMobileUrl',
        'advanced_url': 'advancedUrl',
        'app_ad': 'appAd',
        'custom_parameters': 'customParameters',
        'description': 'description',
        'device_preference': 'devicePreference',
        'display_url': 'displayUrl',
        'extended_text_ad': 'extendedTextAd',
        'headline': 'headline',
        'text_ad2': 'textAd2',
        'tracking_url': 'trackingUrl',
        'url': 'url'
    }

    def __init__(self, ad_type=None, additional_advanced_mobile_urls=None, additional_advanced_urls=None, advanced_mobile_url=None, advanced_url=None, app_ad=None, custom_parameters=None, description=None, device_preference=None, display_url=None, extended_text_ad=None, headline=None, text_ad2=None, tracking_url=None, url=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupAdServiceAd - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ad_type = None
        self._additional_advanced_mobile_urls = None
        self._additional_advanced_urls = None
        self._advanced_mobile_url = None
        self._advanced_url = None
        self._app_ad = None
        self._custom_parameters = None
        self._description = None
        self._device_preference = None
        self._display_url = None
        self._extended_text_ad = None
        self._headline = None
        self._text_ad2 = None
        self._tracking_url = None
        self._url = None
        self.discriminator = None

        self.ad_type = ad_type
        self.additional_advanced_mobile_urls = additional_advanced_mobile_urls
        self.additional_advanced_urls = additional_advanced_urls
        self.advanced_mobile_url = advanced_mobile_url
        self.advanced_url = advanced_url
        self.app_ad = app_ad
        self.custom_parameters = custom_parameters
        self.description = description
        self.device_preference = device_preference
        self.display_url = display_url
        self.extended_text_ad = extended_text_ad
        self.headline = headline
        self.text_ad2 = text_ad2
        self.tracking_url = tracking_url
        self.url = url

    @property
    def ad_type(self):
        """Gets the ad_type of this AdGroupAdServiceAd.  # noqa: E501


        :return: The ad_type of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: AdGroupAdServiceAdType
        """
        return self._ad_type

    @ad_type.setter
    def ad_type(self, ad_type):
        """Sets the ad_type of this AdGroupAdServiceAd.


        :param ad_type: The ad_type of this AdGroupAdServiceAd.  # noqa: E501
        :type: AdGroupAdServiceAdType
        """

        self._ad_type = ad_type

    @property
    def additional_advanced_mobile_urls(self):
        """Gets the additional_advanced_mobile_urls of this AdGroupAdServiceAd.  # noqa: E501


        :return: The additional_advanced_mobile_urls of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: list[AdGroupAdServiceAdditionalAdvancedMobileUrls]
        """
        return self._additional_advanced_mobile_urls

    @additional_advanced_mobile_urls.setter
    def additional_advanced_mobile_urls(self, additional_advanced_mobile_urls):
        """Sets the additional_advanced_mobile_urls of this AdGroupAdServiceAd.


        :param additional_advanced_mobile_urls: The additional_advanced_mobile_urls of this AdGroupAdServiceAd.  # noqa: E501
        :type: list[AdGroupAdServiceAdditionalAdvancedMobileUrls]
        """

        self._additional_advanced_mobile_urls = additional_advanced_mobile_urls

    @property
    def additional_advanced_urls(self):
        """Gets the additional_advanced_urls of this AdGroupAdServiceAd.  # noqa: E501


        :return: The additional_advanced_urls of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: list[AdGroupAdServiceAdditionalAdvancedUrls]
        """
        return self._additional_advanced_urls

    @additional_advanced_urls.setter
    def additional_advanced_urls(self, additional_advanced_urls):
        """Sets the additional_advanced_urls of this AdGroupAdServiceAd.


        :param additional_advanced_urls: The additional_advanced_urls of this AdGroupAdServiceAd.  # noqa: E501
        :type: list[AdGroupAdServiceAdditionalAdvancedUrls]
        """

        self._additional_advanced_urls = additional_advanced_urls

    @property
    def advanced_mobile_url(self):
        """Gets the advanced_mobile_url of this AdGroupAdServiceAd.  # noqa: E501

        <div lang=\"ja\">最終リンク先URL（スマートフォン）です。<br> ADD時、このフィールドは省略可能となります。※adTypeがDYNAMIC_SEARCH_LINKED_ADの場合は無視されます。</div> <div lang=\"en\">Landing Page URL (Smartphone).<br> This field is optional in ADD operation. *If adType is DYNAMIC_SEARCH_LINKED_AD, this field will be ignored.</div>   # noqa: E501

        :return: The advanced_mobile_url of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: str
        """
        return self._advanced_mobile_url

    @advanced_mobile_url.setter
    def advanced_mobile_url(self, advanced_mobile_url):
        """Sets the advanced_mobile_url of this AdGroupAdServiceAd.

        <div lang=\"ja\">最終リンク先URL（スマートフォン）です。<br> ADD時、このフィールドは省略可能となります。※adTypeがDYNAMIC_SEARCH_LINKED_ADの場合は無視されます。</div> <div lang=\"en\">Landing Page URL (Smartphone).<br> This field is optional in ADD operation. *If adType is DYNAMIC_SEARCH_LINKED_AD, this field will be ignored.</div>   # noqa: E501

        :param advanced_mobile_url: The advanced_mobile_url of this AdGroupAdServiceAd.  # noqa: E501
        :type: str
        """

        self._advanced_mobile_url = advanced_mobile_url

    @property
    def advanced_url(self):
        """Gets the advanced_url of this AdGroupAdServiceAd.  # noqa: E501

        <div lang=\"ja\">最終リンク先URLです。<br> ADD時、このフィールドは必須となります。※adTypeがDYNAMIC_SEARCH_LINKED_ADの場合は無視されます。</div> <div lang=\"en\">Landing Page URL.<br> This field is required in ADD operation. *If adType is DYNAMIC_SEARCH_LINKED_AD, this field will be ignored.</div>   # noqa: E501

        :return: The advanced_url of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: str
        """
        return self._advanced_url

    @advanced_url.setter
    def advanced_url(self, advanced_url):
        """Sets the advanced_url of this AdGroupAdServiceAd.

        <div lang=\"ja\">最終リンク先URLです。<br> ADD時、このフィールドは必須となります。※adTypeがDYNAMIC_SEARCH_LINKED_ADの場合は無視されます。</div> <div lang=\"en\">Landing Page URL.<br> This field is required in ADD operation. *If adType is DYNAMIC_SEARCH_LINKED_AD, this field will be ignored.</div>   # noqa: E501

        :param advanced_url: The advanced_url of this AdGroupAdServiceAd.  # noqa: E501
        :type: str
        """

        self._advanced_url = advanced_url

    @property
    def app_ad(self):
        """Gets the app_ad of this AdGroupAdServiceAd.  # noqa: E501


        :return: The app_ad of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: AdGroupAdServiceAppAd
        """
        return self._app_ad

    @app_ad.setter
    def app_ad(self, app_ad):
        """Sets the app_ad of this AdGroupAdServiceAd.


        :param app_ad: The app_ad of this AdGroupAdServiceAd.  # noqa: E501
        :type: AdGroupAdServiceAppAd
        """

        self._app_ad = app_ad

    @property
    def custom_parameters(self):
        """Gets the custom_parameters of this AdGroupAdServiceAd.  # noqa: E501


        :return: The custom_parameters of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: AdGroupAdServiceCustomParameters
        """
        return self._custom_parameters

    @custom_parameters.setter
    def custom_parameters(self, custom_parameters):
        """Sets the custom_parameters of this AdGroupAdServiceAd.


        :param custom_parameters: The custom_parameters of this AdGroupAdServiceAd.  # noqa: E501
        :type: AdGroupAdServiceCustomParameters
        """

        self._custom_parameters = custom_parameters

    @property
    def description(self):
        """Gets the description of this AdGroupAdServiceAd.  # noqa: E501

        <div lang=\"ja\">説明文です。<br> ADD時、このフィールドは必須となります。</div> <div lang=\"en\">Description of ad.<br> This field is required in ADD operation.</div>   # noqa: E501

        :return: The description of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AdGroupAdServiceAd.

        <div lang=\"ja\">説明文です。<br> ADD時、このフィールドは必須となります。</div> <div lang=\"en\">Description of ad.<br> This field is required in ADD operation.</div>   # noqa: E501

        :param description: The description of this AdGroupAdServiceAd.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_preference(self):
        """Gets the device_preference of this AdGroupAdServiceAd.  # noqa: E501


        :return: The device_preference of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: AdGroupAdServiceDevicePreference
        """
        return self._device_preference

    @device_preference.setter
    def device_preference(self, device_preference):
        """Sets the device_preference of this AdGroupAdServiceAd.


        :param device_preference: The device_preference of this AdGroupAdServiceAd.  # noqa: E501
        :type: AdGroupAdServiceDevicePreference
        """

        self._device_preference = device_preference

    @property
    def display_url(self):
        """Gets the display_url of this AdGroupAdServiceAd.  # noqa: E501

        <div lang=\"ja\">表示URLです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Display URL.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The display_url of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: str
        """
        return self._display_url

    @display_url.setter
    def display_url(self, display_url):
        """Sets the display_url of this AdGroupAdServiceAd.

        <div lang=\"ja\">表示URLです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Display URL.<br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param display_url: The display_url of this AdGroupAdServiceAd.  # noqa: E501
        :type: str
        """

        self._display_url = display_url

    @property
    def extended_text_ad(self):
        """Gets the extended_text_ad of this AdGroupAdServiceAd.  # noqa: E501


        :return: The extended_text_ad of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: AdGroupAdServiceExtendedTextAd
        """
        return self._extended_text_ad

    @extended_text_ad.setter
    def extended_text_ad(self, extended_text_ad):
        """Sets the extended_text_ad of this AdGroupAdServiceAd.


        :param extended_text_ad: The extended_text_ad of this AdGroupAdServiceAd.  # noqa: E501
        :type: AdGroupAdServiceExtendedTextAd
        """

        self._extended_text_ad = extended_text_ad

    @property
    def headline(self):
        """Gets the headline of this AdGroupAdServiceAd.  # noqa: E501

        <div lang=\"ja\">タイトル文です。<br> ADD時、このフィールドは必須となります。※adTypeがDYNAMIC_SEARCH_LINKED_ADの場合は無視されます。</div> <div lang=\"en\">Title of ad.<br> This field is required in ADD operation. *If adType is DYNAMIC_SEARCH_LINKED_AD, this field will be ignored.</div>   # noqa: E501

        :return: The headline of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """Sets the headline of this AdGroupAdServiceAd.

        <div lang=\"ja\">タイトル文です。<br> ADD時、このフィールドは必須となります。※adTypeがDYNAMIC_SEARCH_LINKED_ADの場合は無視されます。</div> <div lang=\"en\">Title of ad.<br> This field is required in ADD operation. *If adType is DYNAMIC_SEARCH_LINKED_AD, this field will be ignored.</div>   # noqa: E501

        :param headline: The headline of this AdGroupAdServiceAd.  # noqa: E501
        :type: str
        """

        self._headline = headline

    @property
    def text_ad2(self):
        """Gets the text_ad2 of this AdGroupAdServiceAd.  # noqa: E501


        :return: The text_ad2 of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: AdGroupAdServiceTextAd2
        """
        return self._text_ad2

    @text_ad2.setter
    def text_ad2(self, text_ad2):
        """Sets the text_ad2 of this AdGroupAdServiceAd.


        :param text_ad2: The text_ad2 of this AdGroupAdServiceAd.  # noqa: E501
        :type: AdGroupAdServiceTextAd2
        """

        self._text_ad2 = text_ad2

    @property
    def tracking_url(self):
        """Gets the tracking_url of this AdGroupAdServiceAd.  # noqa: E501

        <div lang=\"ja\">トラッキングURLです。<br> ADD時、このフィールドは省略可能となります。</div> <div lang=\"en\">Tracking URL.<br> This field is optional in ADD operation.</div>   # noqa: E501

        :return: The tracking_url of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        """Sets the tracking_url of this AdGroupAdServiceAd.

        <div lang=\"ja\">トラッキングURLです。<br> ADD時、このフィールドは省略可能となります。</div> <div lang=\"en\">Tracking URL.<br> This field is optional in ADD operation.</div>   # noqa: E501

        :param tracking_url: The tracking_url of this AdGroupAdServiceAd.  # noqa: E501
        :type: str
        """

        self._tracking_url = tracking_url

    @property
    def url(self):
        """Gets the url of this AdGroupAdServiceAd.  # noqa: E501

        <div lang=\"ja\">移行前のリンク先URLです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Destination URL before upgrading. <br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :return: The url of this AdGroupAdServiceAd.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AdGroupAdServiceAd.

        <div lang=\"ja\">移行前のリンク先URLです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。</div> <div lang=\"en\">Destination URL before upgrading. <br> Although this field will be returned in the response, it will be ignored on input.</div>   # noqa: E501

        :param url: The url of this AdGroupAdServiceAd.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, AdGroupAdServiceAd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupAdServiceAd):
            return True

        return self.to_dict() != other.to_dict()
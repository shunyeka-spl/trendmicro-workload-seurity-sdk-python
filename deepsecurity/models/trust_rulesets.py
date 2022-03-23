# coding: utf-8

"""
    Trend Micro Workload Security API

    Copyright 2018 - 2022 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Workload Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Workload Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 50.0.810
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from deepsecurity.models.trust_ruleset import TrustRuleset  # noqa: F401,E501


class TrustRulesets(object):
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
        'trust_rule_set_count': 'int',
        'application_control_trust_rulesets': 'list[TrustRuleset]'
    }

    attribute_map = {
        'trust_rule_set_count': 'trustRuleSetCount',
        'application_control_trust_rulesets': 'applicationControlTrustRulesets'
    }

    def __init__(self, trust_rule_set_count=None, application_control_trust_rulesets=None):  # noqa: E501
        """TrustRulesets - a model defined in Swagger"""  # noqa: E501

        self._trust_rule_set_count = None
        self._application_control_trust_rulesets = None
        self.discriminator = None

        if trust_rule_set_count is not None:
            self.trust_rule_set_count = trust_rule_set_count
        if application_control_trust_rulesets is not None:
            self.application_control_trust_rulesets = application_control_trust_rulesets

    @property
    def trust_rule_set_count(self):
        """Gets the trust_rule_set_count of this TrustRulesets.  # noqa: E501


        :return: The trust_rule_set_count of this TrustRulesets.  # noqa: E501
        :rtype: int
        """
        return self._trust_rule_set_count

    @trust_rule_set_count.setter
    def trust_rule_set_count(self, trust_rule_set_count):
        """Sets the trust_rule_set_count of this TrustRulesets.


        :param trust_rule_set_count: The trust_rule_set_count of this TrustRulesets.  # noqa: E501
        :type: int
        """

        self._trust_rule_set_count = trust_rule_set_count

    @property
    def application_control_trust_rulesets(self):
        """Gets the application_control_trust_rulesets of this TrustRulesets.  # noqa: E501


        :return: The application_control_trust_rulesets of this TrustRulesets.  # noqa: E501
        :rtype: list[TrustRuleset]
        """
        return self._application_control_trust_rulesets

    @application_control_trust_rulesets.setter
    def application_control_trust_rulesets(self, application_control_trust_rulesets):
        """Sets the application_control_trust_rulesets of this TrustRulesets.


        :param application_control_trust_rulesets: The application_control_trust_rulesets of this TrustRulesets.  # noqa: E501
        :type: list[TrustRuleset]
        """

        self._application_control_trust_rulesets = application_control_trust_rulesets

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
        if issubclass(TrustRulesets, dict):
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
        if not isinstance(other, TrustRulesets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

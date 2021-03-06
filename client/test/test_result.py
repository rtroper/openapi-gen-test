# coding: utf-8

"""
    OpenAPI for NCATS Biomedical Translator Reasoners

    OpenAPI for NCATS Biomedical Translator Reasoners  # noqa: E501

    The version of the OpenAPI document: 0.9.2
    Contact: edeutsch@systemsbiology.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.result import Result  # noqa: E501
from openapi_client.rest import ApiException

class TestResult(unittest.TestCase):
    """Result unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Result
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.result.Result()  # noqa: E501
        if include_optional :
            return Result(
                node_bindings = {
                    'key' : [
                        openapi_client.models.node_binding.NodeBinding(
                            kg_id = '0', )
                        ]
                    }, 
                edge_bindings = {
                    'key' : [
                        openapi_client.models.edge_binding.EdgeBinding(
                            kg_id = '0', )
                        ]
                    }
            )
        else :
            return Result(
                node_bindings = {
                    'key' : [
                        openapi_client.models.node_binding.NodeBinding(
                            kg_id = '0', )
                        ]
                    },
                edge_bindings = {
                    'key' : [
                        openapi_client.models.edge_binding.EdgeBinding(
                            kg_id = '0', )
                        ]
                    },
        )

    def testResult(self):
        """Test Result"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

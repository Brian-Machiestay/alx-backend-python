#!/usr/bin/env python3
"""test all functions in the utills client file"""

from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import Mock, patch, PropertyMock
from typing import (
    List,
    Dict,
)
from fixtures import TEST_PAYLOAD

GithubOrgClient = __import__("client").GithubOrgClient
client = __import__("client")
requests = client.requests

class TestGithubOrgClient(unittest.TestCase):
    """test githuborg client"""

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google'),
        ('abc', 'https://api.github.com/orgs/abc')
    ])
    @patch('client.get_json')
    def test_org(self, org: str, exp: str, mk_json: Mock) -> None:
        """test github org client"""
        val = 'https://api.github.com/orgs/{}'.format(org)
        mk_json.return_value = val
        new_cli = GithubOrgClient(org)
        self.assertEqual(new_cli.org, exp)
        mk_json.assert_called_once_with(val)

    def test_public_repos_url(self) -> None:
        """test public repos url"""
        new_cli = GithubOrgClient('abc')
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock,
                          return_value={
                              'repos_url': 'https://api.github.com/orgs/abc'
                          }) as mk_org:
            pr = 'https://api.github.com/orgs/abc'
            self.assertEqual(new_cli._public_repos_url, pr)

    @patch('client.get_json')
    def test_public_repos(self, mk_json: Mock) -> None:
        """test public_repos method"""
        pl = [{
            'name': 'vetted-app',
            'repos_url': 'https://api.github.com/abc/vetted-app'
        }]
        mk_json.return_value = pl
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mk_repo:
            mk_repo.return_value = 'https://api.github.com/abc/vetted-app'
            new_cli = GithubOrgClient('abc')
            self.assertEqual(new_cli.public_repos(), ['vetted-app'])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, li_key, exp) -> None:
        """test has_license method of client"""
        self.assertEqual(GithubOrgClient.has_license(repo, li_key), exp)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'),
                     TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """test public repos in an integration test"""

    get_patcher = ''

    @classmethod
    def _example_pay(cls):
        """return example fixtures"""
        return cls.repos_payload

    @classmethod
    def setUpClass(cls, mk_req):
        """setup code for this test"""
        get_patcher = patch('requests.get')
        get_patcher.start()
        get_patcher.return_value = cls.repos_payload
        get_patcher.json.side_effect = cls._example_pay()

    @classmethod
    def tearDownClass(cls):
        """teardown code for this test"""
        get_patcher.stop()

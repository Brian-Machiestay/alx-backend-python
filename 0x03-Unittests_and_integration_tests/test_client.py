#!/usr/bin/env python3
"""test all functions in the utills client file"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from typing import (
    List,
    Dict,
)


GithubOrgClient = __import__("client").GithubOrgClient
client = __import__("client")


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

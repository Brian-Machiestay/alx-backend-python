#!/usr/bin/env python3
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict
)

access_nested_map = __import__("utils").access_nested_map
utils = __import__("utils")

class TestAccessNestedMap(unittest.TestCase):


    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, mmap: Mapping, pt: Sequence, exp: Any) -> Any:
        """tests the access nested map of the utils class"""
        self.assertEqual(access_nested_map(mmap, pt), exp)



    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, mmap: Mapping, pt: Sequence) -> Any:
        """tests that this access_nested_map raises error"""
        with self.assertRaises(KeyError):
            access_nested_map(mmap, pt)



class TestGetJson(unittest.TestCase):
    """class to test the get_json method in utils"""


    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, pl: Dict) -> None:
        """test the get_json method"""
        with patch.object(utils.requests, 'get') as mocked_utils:
            json_mk = Mock()
            json_mk.json = Mock(return_value=pl)
            mocked_utils.return_value = json_mk
            self.assertEqual(utils.get_json(url), pl)
            mocked_utils.assert_called_once_with(url)

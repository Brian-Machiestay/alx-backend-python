#!/usr/bin/env python3
"""test all functions in the utils file"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable
)

access_nested_map = __import__("utils").access_nested_map
utils = __import__("utils")
memoize = __import__("utils").memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, mmap: Mapping,
                               pt: Sequence, exp: Any) -> Any:
        """tests the access nested map of the utils class"""
        self.assertEqual(access_nested_map(mmap, pt), exp)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, mmap: Mapping,
                                         pt: Sequence) -> Any:
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


class TestMemoize(unittest.TestCase):
    """test the momoized function"""

    def test_memoize(self) -> None:
        """tests the memoized function"""

        class TestClass:
            """a class to test the memoized fn"""

            def a_method(self):
                """return 42"""
                return 42

            @memoize
            def a_property(self):
                """a property"""
                return self.a_method()

        ts_instance = TestClass()
        with patch.object(ts_instance, 'a_method') as a_mtd_patched:
            a_mtd_patched.return_value = 42
            first_cll = ts_instance.a_property
            self.assertEqual(first_cll, 42)
            second_cll = ts_instance.a_property
            self.assertEqual(second_cll, 42)
            a_mtd_patched.assert_called_once()

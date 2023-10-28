#!/usr/bin/env python3
from parameterized import parameterized
import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
)

access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):


    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, mmap: Mapping, pt: Sequence) -> Any:
        """tests the access nested map of the utils class"""
        print(access_nested_map(mmap, pt))

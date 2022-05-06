#!/usr/bin/env python3
"""Task 0"""
import unittest
from parameterized import parameterized
from typing import Sequence, Mapping, Any
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test Class"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """Test function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

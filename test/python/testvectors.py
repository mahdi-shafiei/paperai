"""
Vectors module tests
"""

import os
import unittest

from paperai.vectors import RowIterator, Vectors

# pylint: disable=C0411
from utils import Utils


class TestVectors(unittest.TestCase):
    """
    Vectors tests
    """

    def testStream(self):
        """
        Test row streaming
        """

        # Full index stream
        self.assertEqual(len(list(RowIterator(Utils.DBFILE))), 34222)

    def testTokens(self):
        """
        Test tokens file creation
        """

        output = Vectors.tokens(Utils.DBFILE)
        self.assertEqual(Utils.linecount(output), 34222)

    def testRun(self):
        """
        Test word vectors creation
        """

        # Build vectors file
        Vectors.run(Utils.PATH, 300, 4, Utils.PATH + "/test")
        self.assertTrue(os.path.getsize(Utils.PATH + "/test.magnitude") > 0)

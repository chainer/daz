import sys
import unittest

import numpy as np

import daz


class TestDaz(unittest.TestCase):

    def setUp(self):
        self.normal = sys.float_info.min
        self.denormal = sys.float_info.min / 2

    def check_normal(self):
        assert self.normal == self.denormal + self.denormal
        assert self.normal / 2 == self.denormal

    def test_normal(self):
        self.check_normal()

    def test_daz(self):
        daz.set_daz()
        assert self.normal / 2 == 0
        assert self.denormal * 2 == 0
        assert self.denormal == 0
        daz.unset_daz()
        self.check_normal()

    def test_ftz(self):
        daz.set_ftz()
        assert self.normal / 2 == 0
        assert self.denormal * 2 == self.normal
        assert self.denormal != 0
        daz.unset_ftz()
        self.check_normal()


class TestDazWithNumPy(unittest.TestCase):

    def setUp(self):
        self.normal = np.full((3,), sys.float_info.min)
        self.denormal = np.full((3,), sys.float_info.min) / 2

    def check_normal(self):
        np.testing.assert_equal(self.normal, self.denormal + self.denormal)
        np.testing.assert_equal(self.normal / 2, self.denormal)

    def test_normal(self):
        self.check_normal()

    def test_daz(self):
        daz.set_daz()
        np.testing.assert_equal(self.normal / 2, 0)
        np.testing.assert_equal(self.denormal * 2, 0)
        np.testing.assert_equal(self.denormal, 0)
        daz.unset_daz()
        self.check_normal()

    def test_ftz(self):
        daz.set_ftz()
        np.testing.assert_equal(self.normal / 2, 0)
        np.testing.assert_equal(self.denormal * 2, self.normal)
        assert np.all(self.denormal != 0)
        daz.unset_ftz()
        self.check_normal()

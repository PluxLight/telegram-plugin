"""
====================================
 :mod:`your.demo.helloworld.tests.test_me`
====================================
.. moduleauthor:: Your Nmae <your@modify.me>
.. note:: YOURLABS License

Description
===========
YOUR LABS plugin module : unittest
"""

################################################################################
# import os
import sys
from alabs.common.util.vvargs import ArgsError
from unittest import TestCase
# noinspection PyProtectedMember
from your.demo.telegram import _main as main


################################################################################
class TU(TestCase):
    # ==========================================================================
    isFirst = True

    # ==========================================================================
    def test0000_init(self):
        pass
        # self.assertTrue(True)

    # ==========================================================================
    def test0050_failure(self):
        pass
        # try:
        #     _ = main('-vvv')
        #     self.assertTrue(False)
        # except Exception as e:
        #     sys.stderr.write('\n%s\n' % str(e))
        #     self.assertTrue(True)

    # ==========================================================================
    def test0100_success(self):
        pass
        # try:
        #     r = main('869039844:AAGFdLUCvKc1cUC2Qf08mOuKN27fcggJ3EU', 828556379, 'k')
        #     self.assertTrue(r == 0)
        # except Exception as e:
        #     sys.stderr.write('\n%s\n' % str(e))
        #     self.assertTrue(False)

    # ==========================================================================
    def test9999_quit(self):
        pass
        # self.assertTrue(True)

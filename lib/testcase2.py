#!/usr/bin/env python
#-*- coding:utf-8 -*-


from lib.utils_lib import print_debug_info
from lib.utils_lib import create_recorder
from lib.utils_lib import start_record
from lib.utils_lib import stop_record

import os
import collections
import sys
import functools
import difflib
import pprint
import re
import warnings

import unittest
from unittest import TestCase
from unittest import result
from unittest.case import _ExpectedFailure
from unittest.case import SkipTest
from unittest.case import _UnexpectedSuccess
from unittest.util import (
    strclass, safe_repr, unorderable_list_difference,
    _count_diff_all_purpose, _count_diff_hashable
)


__unittest = True


DIFF_OMITTED = ('\nDiff is %s characters long. '
                 'Set self.maxDiff to None to see it.')




class TestCase2(TestCase):
    """docstring for TestCase2"""

    def run(self, result=None):

        print_debug_info(" run() somebady call me.")

        orig_result = result
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()

        print_debug_info("before _resultForDoCleanups")

        self._resultForDoCleanups = result
        
        print_debug_info("before result.startTest")

        result.startTest(self)

        print_debug_info("get test method...")

        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or
            getattr(testMethod, "__unittest_skip__", False)):
            # If the class or method was skipped.
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '')
                            or getattr(testMethod, '__unittest_skip_why__', ''))
                self._addSkip(result, skip_why)
            finally:
                result.stopTest(self)
            return

        print_debug_info("ready for create recorder.")
        # "create Castro recorder"
        self.recorder = create_recorder(self._testMethodName)                


        try:
            success = False
            try:
                self.setUp()
            except SkipTest as e:
                self._addSkip(result, str(e))
            except KeyboardInterrupt:
                raise
            except:
                result.addError(self, sys.exc_info())
            else:
                try:
                    # start recording test process
                    start_record(self.recorder)
                    # exec the test case method
                    testMethod()
                    # stop record and save the video file
                    stop_record(self.recorder)
                except KeyboardInterrupt:
                    raise
                except self.failureException:
                    result.addFailure(self, sys.exc_info())
                except _ExpectedFailure as e:
                    addExpectedFailure = getattr(result, 'addExpectedFailure', None)
                    if addExpectedFailure is not None:
                        addExpectedFailure(self, e.exc_info)
                    else:
                        warnings.warn("TestResult has no addExpectedFailure method, reporting as passes",
                                      RuntimeWarning)
                        result.addSuccess(self)
                except _UnexpectedSuccess:
                    addUnexpectedSuccess = getattr(result, 'addUnexpectedSuccess', None)
                    if addUnexpectedSuccess is not None:
                        addUnexpectedSuccess(self)
                    else:
                        warnings.warn("TestResult has no addUnexpectedSuccess method, reporting as failures",
                                      RuntimeWarning)
                        result.addFailure(self, sys.exc_info())
                except SkipTest as e:
                    self._addSkip(result, str(e))
                except:
                    result.addError(self, sys.exc_info())
                else:
                    success = True

                try:
                    self.tearDown()
                except KeyboardInterrupt:
                    raise
                except:
                    result.addError(self, sys.exc_info())
                    success = False

            cleanUpSuccess = self.doCleanups()
            success = success and cleanUpSuccess
            if success:
                result.addSuccess(self)
        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()
            # self.recorder.cleanup()
            # print "recorder cleaned."
            # del self.recorder
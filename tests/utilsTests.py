#
# Copyright 2012 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#
from testrunner import VdsmTestCase as TestCaseBase
from vdsm import utils


class RetryTests(TestCaseBase):
    def testStopCallback(self):
        counter = [0]
        limit = 4

        def stopCallback():
            counter[0] += 1
            if counter[0] == limit:
                return True

            return False

        def foo():
            raise RuntimeError("If at first you don't succeed, try, try again."
                               "Then quit. There's no point in being a damn"
                               "fool about it.")
                               # W. C. Fields

        self.assertRaises(RuntimeError, utils.retry, foo, tries=(limit + 10),
                          sleep=0, stopCallback=stopCallback)
        # Make sure we had the proper amount of iterations before failing
        self.assertEquals(counter[0], limit)

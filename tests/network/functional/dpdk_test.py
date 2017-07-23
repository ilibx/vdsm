# Copyright 2017 Red Hat, Inc.
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

from __future__ import absolute_import

import pytest

from .netfunctestlib import NetFuncTestCase, NOCHK


NETWORK_NAME = 'test-network'


@pytest.mark.ovsdpdk_switch
class TestOvsDpdk(NetFuncTestCase):

    def test_dpdk0_device_exists(self):
        self.update_netinfo()
        self.assertIn('dpdk0', self.netinfo.nics)

    def test_setup_ovs_dpdk(self):
        NETCREATE = {NETWORK_NAME: {'nic': 'dpdk0', 'switch': 'ovs'}}
        with self.setupNetworks(NETCREATE, {}, NOCHK):
            self.assertNetwork(NETWORK_NAME, NETCREATE[NETWORK_NAME])

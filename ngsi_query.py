# -*- coding: utf-8 -*-

# Copyright (c) 2020 Future Internet Consulting and Development Solutions S.L.

# This file is part of BAE NGSI Dataset plugin.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from __future__ import unicode_literals

from wstore.asset_manager.resource_plugins.plugin import Plugin

from keyrock_client import KeyrockClient
# from umbrella_client import UmbrellaClient

#from settings import UNITS

UNITS = [{
    'name': 'Api call',
    'description': 'The final price is calculated based on the number of calls made to the API'
}]


class NGSIQuery(Plugin):

    def __init__(self, plugin_model):
        super(NGSIQuery, self).__init__(plugin_model)
        self._units = UNITS

    def on_post_product_spec_validation(self, provider, asset):
        # Check app ID is valid
        client = KeyrockClient()
        client.check_app(asset.meta_info['app_id'])

        # Check role
        admin_role = asset.meta_info['role'] + '.admin'

        try:
            client.check_role(asset.meta_info['app_id'], admin_role)
        except:
            # The roles does not exists so we create it
            client.create_role(asset.meta_info['app_id'], admin_role)

    def on_product_acquisition(self, asset, contract, order):
        # Activate API resources
        client = KeyrockClient()
        admin_role = asset.meta_info['role'] + '.admin'
        client.grant_permission(asset.meta_info['app_id'], order.customer, admin_role)

    def on_product_suspension(self, asset, contract, order):
        client = KeyrockClient()
        admin_role = asset.meta_info['role'] + '.admin'
        client.revoke_permission(asset.meta_info['app_id'], order.customer, admin_role)

    def get_usage_specs(self):
        return self._units

    def get_pending_accounting(self, asset, contract, order):
        return []

if __name__ == "__main__":
    pass

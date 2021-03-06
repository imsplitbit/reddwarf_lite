# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class InstanceView(object):

    def __init__(self, instance):
        self.instance = instance

    def data(self):
        return {"instance": {
            "id": self.instance['id'],
            "name": self.instance['name'],
            "status": self.instance['status'],
            "created": self.instance['created'],
            "updated": self.instance['updated'],
            "flavor": self.instance['flavor'],
            "links": self._build_links(self.instance['links']),
            "addresses": self.instance['addresses'],
            },
        }

    @staticmethod
    def _build_links(links):
        """Build the links for the instance"""
        for link in links:
            link['href'] = link['href'].replace('servers', 'instances')
        return links


class InstancesView(object):

    def __init__(self, instances):
        self.instances = instances

    def data(self):
        data = []
        # These are model instances
        for instance in self.instances:
            data.append(InstanceView(instance).data())

        return data

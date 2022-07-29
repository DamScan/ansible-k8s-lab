#!/usr/bin/env python3

import os
import sys
import argparse
import json

class Inventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.labinventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory))

    # Example inventory for testing.
    def labinventory(self):
        return {
            "_meta": {
                "hostvars": {
                    "node1": {
                        "ansible_host": "node1",
                        "ansible_user": "dams"
                    },
                    "node2": {
                        "ansible_host": "node2",
                        "ansible_user": "dams"
                    },
                    "node3": {
                        "ansible_host": "node3",
                        "ansible_user": "dams"
                    },
                    "node4": {
                        "ansible_host": "node4",
                        "ansible_user": "dams"
                    }
                }
            },
            "all": {
                "children": [
                    "master",
                    "slave"
                ]
            },
            "master": {
                "hosts": [
                    "node1"
                ]
            },
            "slave": {
                "hosts": [
                    "node2",
                    "node3",
                    "node4"

                ]
            }
        }

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
Inventory()
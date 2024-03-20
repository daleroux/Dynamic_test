#!/usr/bin/env python

import json

def main():
    # Define the inventory structure
    inventory = {
        "all": {
            "hosts": [
                "servera",
                "serverd",
                "r7a"
            ],
            "vars": {}
        },
        "_meta": {
            "hostvars": {}
        }
    }

    # Output the inventory in JSON format
    print(json.dumps(inventory, indent=4))

if __name__ == "__main__":
    main()


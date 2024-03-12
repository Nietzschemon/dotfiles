#!/bin/python
import os
import re
import subprocess
import json


key = subprocess.run(
    ["rbw", "get", "it-glue-api-key"], capture_output=True, text=True
).stdout
b = subprocess.run(
    [
        "curl",
        "-X",
        "GET",
        "https://api.eu.itglue.com/passwords",
        "-H",
        "x-api-key: " + key,
        "-H",
        "Content-Type: application/vnd.api+json",
    ],
    capture_output=True,
    text=True,
)


# clean_string = subprocess.run(
# ["tr", "-d", "'\000-\037'"], input=b.stdout, capture_output=True, text=True
# )

print(json.loads(b.stdout))

# print(clean_string.stdout)
# Remove control characters
# tr -d '\000-\037'

#!/bin/sh
#

a=$(rbw get "it-glue-api-key")
b="$(curl -X GET "https://api.eu.itglue.com/passwords" -H "x-api-key: $a" -H "Content-Type: application/vnd.api+json" | tr -d '\000-\037')"

echo "$b"
#tr -d '\000-\037'

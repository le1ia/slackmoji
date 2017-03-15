#!/bin/bash

DOMAIN="$1"
TOKEN="$2"
DATA="token=${TOKEN}"
URL="https://${DOMAIN}.slack.com/api/emoji.list"

curl ${URL} -d ${DATA}

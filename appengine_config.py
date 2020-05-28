# -*- coding: utf-8 -*-
import os
import sys

if os.environ.get('SERVER_SOFTWARE','').startswith('Dev'):
    sys.path.append('/var/lib/python/out/out')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "out.settings")

#APIKEYS

consumer_api = "XXX"
consumer_secret = "XXX"
access_token = "XXX"
access_token_secret = "XXX"

slack_api_token_prefix = "XXX"
slack_api_token_postfix = "XXX"

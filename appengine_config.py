# -*- coding: utf-8 -*-
import os
import sys

if os.environ.get('SERVER_SOFTWARE','').startswith('Dev'):
    sys.path.append('/var/lib/python/out/out')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "out.settings")

#APIKEYS

consumer_api = "1ab2619bb8291afc91cc211b1"
consumer_secret = "bab291ee841bf29ae18e810"
access_token = "7a81bbb1b22e88102931"
access_token_secret = "ebf83401ab291af401e"

slack_api_token_prefix = "xoxp-1148486360387-1141545032230-1135659087559-"
slack_api_token_postfix = "df75c296d8d90713410457958f42fe5a"

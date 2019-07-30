#!/usr/bin/env PYTHONIOENCODING=UTF-8 usr/local/bin/python3
# -*- coding: utf-8 -*-

#metadata
# <bitbar.title>techromancer</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Adam and Ari</bitbar.author>
# <bitbar.author.github>schrecka</bitbar.author.github>
# <bitbar.desc>fixme</bitbar.desc>
# <bitbar.image>http://www.hosted-somewhere/pluginimage</bitbar.image>
# <bitbar.dependencies>fixme</bitbar.dependencies>
# <bitbar.abouturl>techromancer.ml</bitbar.abouturl>

import os
from datetime import datetime, timedelta

print ("techromancer")
print ("---")

six_hours_from_now = datetime.time(datetime.now())
format(six_hours_from_now, '%H:%M:%S')
print ("running ... last update at", six_hours_from_now.replace(microsecond=0), "| color=blue")

os.chdir(r"/Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts")
print(os.system('python3 watcher-test.py'))

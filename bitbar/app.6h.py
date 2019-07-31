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

#change sys path to access main scripts
import sys
sys.path.append("/Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts")
#main scripts
import watcher
import uploader

import os
import stat
import time
import subprocess
import pathlib
from datetime import datetime, timedelta

#allow logger.txt to be accessed
os.chdir(r"/Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts")
os.chmod("logger.txt", stat.S_IRWXU)

#upload past changes
# uploader.run()

#bitbar UI
print ("techromancer")
print ("---")
last_update_time = datetime.time(datetime.now())
format(last_update_time, '%H:%M:%S')
print ("running ... last update at", last_update_time.replace(microsecond=0), "| color=blue")
print ("uploaded to cloud | color=blue")

subprocess.Popen('python3 watcher.py', shell=True, cwd="/Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts")
# watcher.run()

#!/bin/bash
#chmod u+x app.1m.sh

#metadata
# <bitbar.title>techromancer</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Adam and Ari</bitbar.author>
# <bitbar.author.github>schrecka</bitbar.author.github>
# <bitbar.desc>fixme</bitbar.desc>
# <bitbar.image>http://www.hosted-somewhere/pluginimage</bitbar.image>
# <bitbar.dependencies>fixme</bitbar.dependencies>
# <bitbar.abouturl>techromancer.ml</bitbar.abouturl>

echo "techromancer"
echo "---"
#
#
# # chmod u+x /Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/watcher-test.py
# # chmod +x /Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/logger-test.txt
# chmod u+x /Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/run.sh
#
# cd /Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts
#
# #/usr/local/bin/python3 /Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/watcher-test.py
#
chmod u+x /Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/is_open.txt
chmod u+x /Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/run.sh

> /Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/is_open.txt
bash=/Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/run.sh

FONT=( 'size=14' 'font=UbuntuMono' )
if [ -s /Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/is_open.txt ]
# if [ 1 -eq 1 ]
  then
    echo "error | $FONT color=blue"
  else
    echo "running | $FONT color=red"
fi
echo "---"

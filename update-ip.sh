#!/usr/bin/env bash

# Suggest adding to crontab (after configuring passwordless ssh to a limited account)
# */5 * * * * /home/casper/update-ip.sh >/dev/null 2>&1

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

IP_ADDR=`ifconfig | grep 'inet ' | grep -v -E '172\.|127\.' | cut -d' ' -f10 | tr '\n', ','`
DATE=`/bin/date`

IP_ADDR=$(echo "$IP_ADDR" | sed 's|,|</br>\n|g')

cat head.html > tmp.html
printf "<h3>$IP_ADDR</h3>\n<h3>Last Updated: $DATE</h3>\n" >> "tmp.html"
cat foot.html >> tmp.html

scp tmp.html conjuring@reades.com:public_html/index.html


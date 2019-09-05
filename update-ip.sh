#!/usr/bin/env bash

# Suggest adding to crontab (after configuring passwordless ssh to a limited account)
# */5 * * * * /home/casper/update-ip.sh >/dev/null 2>&1

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

IP_ADDR=$(ifconfig | awk '/inet[^6]/ {print $2}' | grep -v "1[27][27]" | tr '\n', ',')
DATE=$(date)

IP_ADDR=$(echo "$IP_ADDR" | sed 's|,|</br>|g')

printf "<html><title>Current NUC IP Addresses</title><body>\n" > tmp.html
printf "<h3>$IP_ADDR</h3>\n<h3>Last Updated: $DATE</h3>"$'\n' >> tmp.html
printf "</body></html>" >> tmp.html

scp tmp.html conjuring@reades.com:public_html/index.html


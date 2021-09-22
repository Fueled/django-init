#!/bin/bash

# Generates changelog day by day
NEXT=$(date +%F)
echo "History"
echo "----------------------"
git log --no-merges --format="%cd" --date=short | sort -u -r | while read DATE ; do
    echo
    echo "### $DATE"
    GIT_PAGER=cat git log --no-merges --format=" - %s ([%aN](https://github.com/Fueled/django-init/commit/%h))" --since="$DATE 00:00" --until="$DATE 23:59"
done

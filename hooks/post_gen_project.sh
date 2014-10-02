#!/bin/bash
echo "You have successfully created your app!!"

# fix newline at eof
find . ! -path "*/venv/*" -type f -name "*.py" -exec bash -c "tail -n1 {} | read -r _ || echo >> {}" \;

# initialize git repo and create first commit
git init && git add .
git commit -am "chore(setup): create base django project."

# setup the project for local development
fab init

OUT=$?
if [ $OUT -eq 0 ];then
    echo "============================================"
    echo "          This is what we just did!         "
    echo "============================================"
    echo ""
    echo "* created a base django project code base at"
    echo "  `pwd`"
    echo "* installed project dependencies"
    echo "* initialized a git repo and created the first commit"
    echo "* you can now cd into `pwd` and start working"
    echo "============================================"
else
    echo "============================================"
    echo "          Something went wrong!!            "
    echo "============================================"
    echo ""
    echo "Check the logs above to figure it out."
fi

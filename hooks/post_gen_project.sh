#!/bin/bash
# Ensure newline at EOF
find . ! -path "*/venv/*" -type f -name "*.py" -exec bash -c "tail -n1 {} | read -r _ || echo >> {}" \;

echo "Finished."

echo -n "==> Do you want to setup all the project dependencies, includes installing "
echo -n "python libraries inside virtualenv at '`pwd`/venv/' folder,  "
echo -n "creation of postgres database and initializing a git repo? (y/n)"

# Inside CI, always assume the answer is yes! :)
if [ $CI ]; then
    yn="yes"
else
    read  yn
fi


if echo "$yn" | grep -iq "^y"; then
    echo "==> Checking system dependencies. You may need to enter your sudo password."

    echo "==> Install pip, if not present."
    if ! hash pip 2>/dev/null; then
        echo "pip not found.... installing it..."
        sudo easy_install pip
    fi

    echo "==> Install fabric, if not present."
    if ! hash fab 2>/dev/null; then
        echo "fab command not found... installing it..."
        sudo pip install fabric
    fi

    echo "==> Install npm, if not present."
    if ! hash npm 2>/dev/null; then
        echo "npm command not found... installing it..."
        curl -L https://npmjs.org/install.sh | sh
    fi

    echo "==> Initialize git repo and create first commit and tag it with v0.0.0"
    git init && git add .
    git commit -am "chore(setup): create base django project."
    git tag v0.0.0

    echo "==> Setup the project dependencies and database for local development"
    fab init

    OUT=$?
    if [ $OUT -eq 0 ]; then
        echo "============================================"
        echo "          This is what we just did!         "
        echo "============================================"
        echo ""
        echo "* created a base django project code base at"
        echo "  `pwd`"
        echo "* installed project dependencies"
        echo "* initialized a git repo and created the first commit"
        echo -n "* you can now cd into `pwd` and start working after "
        echo "activating virtualenv with 'source venv/bin/activate'."
        echo "============================================"
    else
        echo "============================================"
        echo "          Oops! Something went wrong!!      "
        echo "============================================"
        echo ""
        echo -n "HINT: Make sure you have installed all OS dependencies. "
        echo "Check the logs above to figure it out."
    fi
else
    echo "==> Skipping project setup..."
    echo -n "==> You can now 'cd' into "`PWD`" and explore the project. "
    echo "Read 'README.md' inside it for further setup instructions!"
    echo ""
    echo " ============> HAPPY CODING <============ "
fi

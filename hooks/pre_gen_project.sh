#!/bin/bash

# Install pip, if not present.
if ! hash pip 2>/dev/null; then
    echo "pip not found.... installing it..."
    sudo easy_install pip
fi

# Install fabric, if not present.
if ! hash fab 2>/dev/null; then
    echo "fab command not found.... installing it..."
    sudo pip install fabric
fi

# Install npm, if not present.
if ! hash npm 2>/dev/null; then
    echo "npm command not found.... installing it..."
    curl -L https://npmjs.org/install.sh | sh
fi

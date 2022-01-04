#!/bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

# Ensure newline at EOF
find . ! -path "*/venv/*" -type f -name "*.py" -exec bash -c "tail -n1 {} | read -r _ || echo >> {}" \;

echo "${green}[Finished]${reset}"

echo "==> Setup project dependencies? It will:"
echo "  - Create virtualenv at './{{ cookiecutter.github_repository }}/venv/'."
echo "  - Install development requirements inside virtualenv."
echo "  - Create a postgres database named '{{ cookiecutter.main_module }}'."
echo "  - Run './manage.py migrate'."
echo "  - Initialize git."
echo "  - Create git tag {{ cookiecutter.version }}."
echo -n "Would you like to perform these steps? (y/[n]) "
echo ""

# Inside CI, always assume the answer is yes! :)
if [ $CI ]; then
    yn="yes"
else
    read  yn
fi

if echo "{{ cookiecutter.add_heroku }}" | grep -iq "^n"; then
    rm -rf uwsgi.ini Procfile runtime.txt bin/post_compile
fi

if echo "{{ cookiecutter.add_ansible }}" | grep -iq "^n"; then
    rm -rf provisioner Vagrantfile ansible.cfg
fi

if echo "{{ cookiecutter.add_celery }}" | grep -iq "^n"; then
    rm -rf {{ cookiecutter.main_module }}/celery.py
fi

if echo "{{ cookiecutter.add_pre_commit }}" | grep -iq "^n"; then
    rm .pre-commit-config.yaml
fi

if echo "$yn" | grep -iq "^y"; then
    echo "==> Checking system dependencies. You may need to enter your sudo password."

    echo "==> Install pip, if not present."
    if ! hash pip 2>/dev/null; then
        echo "pip not found.... installing it..."
        sudo easy_install pip
    fi

    echo "==> Initialize git repo and create first commit and tag it with v{{ cookiecutter.version }}"
    git init
    git add .
    if [ $CI ]; then
        git config user.email "you@example.com"
        git config user.name "Your Name"
    fi
    git commit -am "chore(setup): create base django project."
    git tag v{{ cookiecutter.version }}

    echo "${green}==> Setup the project dependencies and database for local development${reset}"
    make install

    OUT=$?
    if [ $OUT -eq 0 ]; then
        echo "${green}============================================"
        echo "All set! Run these commands to get started:"
        echo ""
        echo "cd {{ cookiecutter.github_repository }}"
        echo "poetry shell"
        echo "pytest"
        echo "./manage.py runserver"
        echo ""
        echo "============================================"
        echo "${green} ============> HAPPY CODING <============ ${reset}"
    else
        echo "${red}============================================"
        echo "          Oops! Something went wrong!!      "
        echo "============================================${reset}"
        echo ""
        echo -n "HINT: Make sure you have installed all OS dependencies. "
        echo "Check the logs above, they might give you some clues."
    fi
else
    echo "==> Skipping project setup..."
    echo "==> You can now 'cd {{ cookiecutter.github_repository }}/' and explore the project. "
    echo "    Read 'README.md' inside it for further setup instructions!"
    echo ""
    echo "${green} ============> HAPPY CODING <============ ${reset}"
fi

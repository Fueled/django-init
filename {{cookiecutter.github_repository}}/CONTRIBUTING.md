# Contributing
All contributions are much welcome and greatly appreciated! Expect to be credited for you effort.

## General
Generally try to limit the scope of any Pull Request to an atomic update if possible. This way, it's much easier to assess and review your changes.

You should expect a considerably faster turn around if you submit two or more PRs instead of baking them all into one major PR.

## Pull Request Guidelines
Before you submit a pull request, check that it meets these guidelines:

1. All the pull requests are made against `master` branch.

2. The pull request should include tests.

3. If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring, and add the feature to the list in README.md.


## Coding conventions

- Read and pay attention to current code in the repository
- For the Python part, we follow pep8 in most cases. We use [flake8][flake8] to check for linting errors. Once you're ready to commit changes, check your code with `flake8`.
- Install a plugin for [EditorConfig][editorconfig] and let it handle some of the formating issues for you.
- For the Django part, we follow standard [Django coding style][django-coding style].
- And always remember the Zen.

[editorconfig]: http://editorconfig.org/
[flake8]: http://flake8.readthedocs.org/en/latest/
[django-coding style]: https://docs.djangoproject.com/en/stable/internals/contributing/writing-code/coding-style/

# Conventions

- Read and pay attention to current code in the repository
- For the Python part, we follow pep8 in most cases. We use [flake8][flake8] to check for linting errors. Once you're ready to commit changes, check your code with `flake8`.
- Install a plugin for [EditorConfig][editorconfig] and let it handle some of the formating issues for you.
- For the Django part, we follow standard [Django coding style][django-coding style].
- And always remember the Zen.

[editorconfig]: http://editorconfig.org/
[flake8]: http://flake8.readthedocs.org/en/latest/
[django-coding style]: https://docs.djangoproject.com/en/1.7/internals/contributing/writing-code/coding-style/


# Coding Rules

## Django models

* All model names in singular and CamelCase.
* All models have a `Meta` with at least:
    - `verbose_name` and `verbose_name_plural`: unicode strings, lowercase, with spaces.
    - `ordering`: return a consistent order, using pk if no other unique field or combination exists.
* All models have `__str__` method, returning a human-readable, descriptive, short text.
* All fields have `verbose_name`. Also `help_text` if needed to fully explain the field meaning.
* All fields have explicit `blank` and `null` parameters. Use only those combinations, unless there a documented need of other thing:

    **Normal fields** (IntegerField, DateField, ForeignKey, FileField...)
      - (optional) `null = True`, `blank = True`
      - (required) `null = False`, `blank = False`

    **Text fields** (CharField, TextField, URLField...)
      - (optional) `null = False`, `blank = True`
      - (required) `null = False`, `blank = False`

    **Boolean fields**:  
      - (two values, T/F) `null = False`, `blank = True`
      - (three values, T/F/Null) `null = True`, `blank = True`

* Don't create text fields with `null = True`, unless you need to distinguish between empty string and `None`.
* Don't create boolean fields with `blank = False`, otherwise they could only be `True`.

Example:

```python
class SomeClass(models.Model):
    name = models.CharField(max_length=100, null = False, blank = False, unique=True,
               verbose_name = _('name'))
    slug = models.SlugField(max_length=100, null = False, blank = False, unique=True,
               verbose_name = _('slug'),
               help_text = ('Identifier of this object. Only letters, digits and underscore "_" allowed.'))
    text = models.TextField(null = False, blank = True,
               verbose_name = _('text'))

    class Meta:
        verbose_name = _('some class')
        verbose_name_plural = _('some classes')
        ordering = ['name']

    def __str__(self):
        return self.name
```

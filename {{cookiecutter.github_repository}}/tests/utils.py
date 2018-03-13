# Standard Library
import functools

# Third Party Stuff
from django.conf import settings
from django.db.models import signals


def signals_switch():
    pre_save = signals.pre_save.receivers
    post_save = signals.post_save.receivers

    def disconnect():
        signals.pre_save.receivers = []
        signals.post_save.receivers = []

    def reconnect():
        signals.pre_save.receivers = pre_save
        signals.post_save.receivers = post_save

    return disconnect, reconnect


disconnect_signals, reconnect_signals = signals_switch()


def set_settings(**new_settings):
    """Decorator for set django settings that will be only available during the
    wrapped-function execution.

    For example:
        @set_settings(FOO='bar')
        def myfunc():
            ...

       @set_settings(FOO='bar')
       class TestCase:
           ...
    """
    def decorator(testcase):
        if type(testcase) is type:
            namespace = {
                'OVERRIDE_SETTINGS': new_settings, 'ORIGINAL_SETTINGS': {}}
            wrapper = type(testcase.__name__, (SettingsTestCase, testcase),
                           namespace)
        else:
            @functools.wraps(testcase)
            def wrapper(*args, **kwargs):
                old_settings = override_settings(new_settings)
                try:
                    testcase(*args, **kwargs)
                finally:
                    override_settings(old_settings)

        return wrapper

    return decorator


def override_settings(new_settings):
    old_settings = {}
    for name, new_value in list(new_settings.items()):
        old_settings[name] = getattr(settings, name, None)
        setattr(settings, name, new_value)
    return old_settings


class SettingsTestCase(object):
    @classmethod
    def setup_class(cls):
        cls.ORIGINAL_SETTINGS = override_settings(cls.OVERRIDE_SETTINGS)

    @classmethod
    def teardown_class(cls):
        override_settings(cls.ORIGINAL_SETTINGS)
        cls.OVERRIDE_SETTINGS.clear()


def get_dict_from_list_where(my_list, key, value):
    """see: http://stackoverflow.com/a/7079297/782901"""
    return next((item for item in my_list if item[key] == value), None)

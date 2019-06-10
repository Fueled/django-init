# Third Party Stuff
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


def get_dict_from_list_where(my_list, key, value):
    """see: http://stackoverflow.com/a/7079297/782901"""
    return next((item for item in my_list if item[key] == value), None)

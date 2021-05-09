import signals
from user_info.controller import init_user_info


def init_subscriptions():
    signals.on_user_create += init_user_info


def remove_subscriptions():
    signals.on_user_create -= init_user_info

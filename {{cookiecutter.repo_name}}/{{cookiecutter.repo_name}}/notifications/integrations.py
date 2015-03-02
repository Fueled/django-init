from django.conf import settings
import time
import requests
import logging

log = logging.getLogger(__name__)


class ZeroPushIntegration(object):
    ZEROPUSH_NOTIFY_URL = "https://api.zeropush.com/notify"

    def __init__(self):
        if not settings.ZEROPUSH_AUTH_TOKEN:
            raise ValueError('NO ZEROPUSH TOKEN SET');
        self.ZEROPUSH_AUTH_TOKEN = settings.ZEROPUSH_AUTH_TOKEN

    def notify_devices(self, devices, alert=None, sound=None, badge_number=None, info=None, expiry=None):
        if len(devices) > 0:
            params = {
                "auth_token": self.PUSH_NOTIFICATION_TOKEN,
                "device_tokens[]": [device.token for device in devices]
            }
            if alert is not None:
                params.update({"alert": json.dumps(alert)})
            if sound is not None:
                params.update({"sound": sound})
            if badge_number is not None:
                params.update({"badge_number": badge_number})
            if info is not None:
                if not isinstance(info, six.string_types):
                    params.update({"info": json.dumps(info)})
                else:
                    params.update({"info": info})

            # if expiry isn't specified use 1 month from now
            expiry_time = expiry if expiry is not None else int(time.time()) + 2592000
            params.update({"expiry": expiry_time})

            response = requests.post(self.ZEROPUSH_NOTIFY_URL, params)
            if response.ok:
                log.info("Push successfully sent to zeropush")
                return True
            else:
                log.error(
                    "Error! Push failed to be sent to zeropush! Error response: %s" % response.text)
                return False

        return False

    def send_push_notification(self, user, alert=None, sound=None, badge_number=None, info=None,
                               expiry=None):
        if getattr(settings, 'DISABLE_PUSH_NOTIFICATION', False):
            log.info("Sent to %s: %s" % (user.get_full_name(), str(alert)))
            return True

        return self.notify_devices(user.devices.all(), alert=alert, sound=sound,
                              badge_number=badge_number, info=info, expiry=expiry)


    def send_bulk_push_notification(self, users, alert=None, sound=None, badge_number=None, info=None,
                                    expiry=None):

        devices = [user.devices.all() for user in users]

        # http://stackoverflow.com/a/952952
        merged_devices = [item for sublist in devices for item in sublist]

        if getattr(settings, 'DISABLE_PUSH_NOTIFICATION', False):
            log.info("Sent to %s: %s" % (merged_devices, str(alert)))
            return True

        return self.notify_devices(merged_devices, alert=alert, sound=sound,
                              badge_number=badge_number, info=info, expiry=expiry)

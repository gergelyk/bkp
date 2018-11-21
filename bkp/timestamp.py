from datetime import datetime as dt

class Timestamp:
    def __init__(self, timestamp):
        self._ts = timestamp

    @property
    def Z_(self):
        tz = self._ts.astimezone()
        return tz.tzname()

    def __getattr__(self, key):
        return self._ts.strftime('%{}'.format(key))

timestamp = Timestamp(dt.now())

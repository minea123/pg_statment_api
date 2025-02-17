import logging
from json import dumps

class FlexibleFormatter(logging.Formatter):
    def format(self, record):
        extra = '' if record._extra is None else dumps(record._extra, indent=2, ensure_ascii=False)
        return super().format(record) + ' ' + extra


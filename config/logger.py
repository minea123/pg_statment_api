import logging

class FlexibleFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'mykey'):
            record.msg = f"{record.msg} - {record.mykey}"
        return super().format(record)

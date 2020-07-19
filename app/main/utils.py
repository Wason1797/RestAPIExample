import datetime


class Utils:

    @staticmethod
    def parse_date(date: str):
        try:
            return datetime.datetime.strptime(date, r'%Y-%m-%d')
        except Exception:
            return None

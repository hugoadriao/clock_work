from datetime import datetime, timezone, date


def validate_date(datetime_to_convert):
    if type(datetime_to_convert) is date:
        return date(
            year=datetime_to_convert.year,
            month=datetime_to_convert.month,
            day=datetime_to_convert.day
        ).isoformat()
    if datetime_to_convert is None:
        return None
    return datetime(
        year=datetime_to_convert.year,
        month=datetime_to_convert.month,
        day=datetime_to_convert.day,
        hour=datetime_to_convert.hour,
        minute=datetime_to_convert.minute,
        second=datetime_to_convert.second,
        tzinfo=timezone.utc
    ).isoformat().replace("+00:00", "Z")

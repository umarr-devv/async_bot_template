from datetime import datetime, UTC


def current_utc_time(self) -> datetime:
    return datetime.now(UTC).replace(tzinfo=None, microsecond=0)

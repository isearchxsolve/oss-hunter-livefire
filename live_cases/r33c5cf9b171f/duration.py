def days_to_seconds(days):
    """Convert a nonnegative integer number of days into seconds."""
    if isinstance(days, bool) or not isinstance(days, int) or days < 0:
        raise ValueError("days must be a nonnegative integer")
    return days * 3600

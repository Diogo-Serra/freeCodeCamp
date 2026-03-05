def add_time(start, duration, weekday=None):
    # Parse start time
    time_part, period = start.split()
    sh, sm = map(int, time_part.split(':'))
    period = period.upper()

    # Convert start to 24h minutes since midnight
    sh24 = sh % 12 + (12 if period == 'PM' else 0)
    start_minutes = sh24 * 60 + sm

    # Parse duration
    dh, dm = map(int, duration.split(':'))
    dur_minutes = dh * 60 + dm

    total = start_minutes + dur_minutes
    days_later = total // (24 * 60)
    rem = total % (24 * 60)

    # Convert back to 12h
    h24 = rem // 60
    m = rem % 60
    out_period = 'AM' if h24 < 12 else 'PM'
    h12 = h24 % 12
    if h12 == 0:
        h12 = 12

    # Base output time
    out = f"{h12}:{m:02d} {out_period}"

    # Day of week handling
    if weekday:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        idx = days.index(weekday.capitalize())
        new_day = days[(idx + days_later) % 7]
        out += f", {new_day}"

    # Days later suffix
    if days_later == 1:
        out += " (next day)"
    elif days_later > 1:
        out += f" ({days_later} days later)"

    return out

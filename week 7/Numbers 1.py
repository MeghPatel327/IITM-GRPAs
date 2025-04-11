def seconds_to_minute_seconds(seconds: int) -> tuple:
    return (seconds//60, seconds - (seconds//60)*60)
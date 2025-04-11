class Time:
    def __init__(self, time):
        self.time = time

    def seconds_to_minutes(self):
        minutes, seconds = divmod(self.time, 60)
        return f"{minutes} min {seconds} sec"

    def seconds_to_hours(self):
        hours, remainder = divmod(self.time, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours} hrs {minutes} min {seconds} sec"

    def seconds_to_days(self):
        days, remainder = divmod(self.time, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{days} days {hours} hrs {minutes} min {seconds} sec"
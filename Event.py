class Event:

    def __init__(self, title, notes=None, hour=None):
        self.title = title
        self.notes = notes
        self.hour = hour

    # Checks if events are equal
    def equals(self, event):
        return (self.title == event.title
                and self.notes == event.notes
                and self.hour == event.hour)

    # Return string repr of Event
    def to_str(self):
        event_str = self.title + "\n"
        return event_str

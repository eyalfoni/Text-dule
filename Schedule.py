class Schedule:

    def __init__(self):
        self.sched = []

    # Adds item and returns it
    # If duplicate will return None
    def add(self, event):
        duplicate = False
        for x in range(0, len(self.sched)):
            if self.sched[x].equals(event):
                duplicate = True
        if duplicate:
            return None
        else:
            self.sched.append(event)
            return event

    # Removes an event if found and returns it
    # If event not found returns None
    def remove(self, event):
        for x in range(0, len(self.sched)):
            if self.sched[x].equals(event):
                removed_event = self.sched[x]
                del self.sched[x]
                return removed_event
        return None

    # Return string repr of Sched
    def to_str(self):
        sched_str = "Schedule: \n"
        for x in range(0, len(self.sched)):
            sched_str += "Event #" + str(x) + "\n"
            sched_str += self.sched[x].to_str()
        return sched_str

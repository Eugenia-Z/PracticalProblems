
class Solution:
  def convert_to_minutes(self, time_str):
    """Converts HH:MM to minutes since the start of the day"""
    hours, mins = map(int, time_str.split(":"))
    return hours * 60 + mins 

  def convert_to_time_str(self, minutes):
    """convert minutes since start of the day to HH:MM format"""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02}:{mins:02}"
    
  def getEarliestMeetTime(self, events: List[str], k: int) -> str:
    # check the constrains, and get a hint that there are a total of 1440 mins in a day
    total_mins = 1440

    # Dictionary to keep track of when each person is busy
    busy = {}

    # Parse each event and mark the person's busy times
    for event in events:
      parts = event.split()
      person_name = parts[0]
      start_time = self.convert_to_minutes(parts[2])
      end_time = self.convert_to_minutes(parts[3])

      # If the person hasn't been recorded, initialize their busy list
      if person_name not in busy:
        busy[person_name] = [0] * total_mins

      # Mark the person as busy from start_time to end_time inclusive
      for min in range(start_time,end_time+1):
        busy[person_name][min] = 1


    # Now we need to check when everyone is avaible for 'k' minutes.
    # Create an availability array for all people combined
    available = [1] * total_mins 

    # for each person, combine their busy time with the availability array
    for person in busy:
      for min in range(total_mins):
        if busy[person][min] == 1:
          available[min] = 0

    # look for the first block of 'k' consecutive available minutes
    free_min = 0
    for min in range(total_mins):
      if available[min] == 1:
        free_min += 1
        if free_min == k:
          start_time = min - k + 1
          return self.convert_to_time_str(start_time)
      else:
        free_min = 0
    return "-1"
      
  

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

    # Dictionary to keep track of when each person is busy
    busy_intervals = []

    # Parse each event and mark the person's busy times
    for event in events:
      parts = event.split()
      person_name = parts[0]
      start_time = self.convert_to_minutes(parts[2])
      end_time = self.convert_to_minutes(parts[3])

      # Add busy intervals to the list
      busy_intervals.append((start_time, end_time))
      
    # Sort the busy intervals by start time
    busy_intervals.sort()

    # Merge the overlapping busy intervals
    merged_intervals = []
    current_start, current_end = busy_intervals[0]

    for start, end in busy_intervals[1:]:
      if start <= current_end:
        current_end = max(current_start, end)
      else:
        merged_intervals.append((current_start, current_end))
        current_start, current_end = start, end
    # Add the last interval
    merged_intervals.append((current_start, current_end))

    # Check for free time slots between merged intervals
    previous_end = 0 # start checking from the beginning of the day
    for start, end in merged_intervals:
      if start - previous_end > k:
        return self.convert_to_time_str(previous_end+1)
      previous_end = end 

    # Check for a free slot at the end of the day:
    if 1440 - previous_end > k:
      return self.convert_to_time_str(previous_end+1)
    return "-1"

import bisect
class Solution:
  def phoneCalls(self, start: List[int], duration: List[int], volume: List[int]) -> int:
    end = []  
    calls = []

    # Step 1: create a list of calls with start time, end time and volume
    for st, dr, vl in zip(start, duration, volume):
      ed = st+dr
      end.append(ed)
      calls.append((st, ed, vl))

    # Step 2: sort calls by end time
    calls.sort(key=lambda call:call[1])

    # Step3: Prepare a DP array

    # dp[i] representing the maximum order volume at ith point
    dp = [0] * len(calls)

    # Step4: init the dp
    dp[0] = calls[0][2]  # the first call's volume is the maximum we can get at the start

    # Step5: Fill in the dp array
    # get stuck : 
    # 1/ how to represent last non-overlapping call? -> binary search
    # 2/ how to fill in the dp array
    for i in range(1, len(calls)):
      # Option 1: skip the curernt call
      skip_current = dp[i-1]

      # Option 2: take the curernt call, findthe last non-overlapping call
      current_vol = calls[i][2]
      last_non_overlapping = bisect.bisect_right(end, calls[i][0]) - 1

      if last_non_overlapping != -1:
        take_current = current_vol + dp[last_non_overlapping]
      else:
        take_current = current_vol

      # Take the max of both options and fill in the dp table
      dp[i] = max(skip_current, take_current)
      
    return dp[-1]
    
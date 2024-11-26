# sliding window problem, same direction, left can jump to right + 1, need # of ways 

def createMaximumCollaborations(creatorsEngagementPower, minCreatorsRequired, minTotalEngagementPowerRequired):
    n = len(creatorsEngagementPower)
    left = 0  # Left end of the sliding window
    currentSum = 0  # Running sum of engagement power
    collaborations = 0  # Count of valid collaborations
    
    right = 0  # Right end of the sliding window
    while right < n:
        # Add the current creator's engagement power to the running sum
        currentSum += creatorsEngagementPower[right]
        
        # If the window size is large enough, try to form a team
        while right - left + 1 >= minCreatorsRequired:
            # Check if the current window is valid (meets the engagement threshold)
            if currentSum >= minTotalEngagementPowerRequired:
                collaborations += 1
                # Reset the window for the next team (start after the current 'right')
                left = right + 1
                currentSum = 0
                break  # Move on to the next set of creators

            else:
                # If the team is not valid, shrink the window from the left side
                break

        # Move the 'right' pointer to expand the window
        right += 1
    
    return collaborations
         

# creatorsEngagementPower=[4, 6, 8, 11, 9, 12]
# minCreatorsRequired=2
# minTotalEngagementPowerRequired= 15

creatorsEngagementPower = [4, 4, 3, 6, 4, 3, 5]
minCreatorsRequired = 2
minTotalEngagementPowerRequired = 8

# creatorsEngagementPower = [5, 4, 3, 2, 1]
# minCreatorsRequired = 3
# minTotalEngagementPowerRequired = 20
print(createMaximumCollaborations(creatorsEngagementPower, minCreatorsRequired, minTotalEngagementPowerRequired))
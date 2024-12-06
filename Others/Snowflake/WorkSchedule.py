#KQ's thought: in essense it is a permutation problem - backtracking. The idea is to compute the # how many different ways to 
# sum up to (pending hours) with each operand less than or equal to day_hours

# this is a GPT solution
def findSchedules(work_hours, day_hours, pattern):
    # Step 1: Calculate known hours and identify the position of '?'
    total_known_hours = 0
    question_mark_positions = []
    
    for i, char in enumerate(pattern):
        if char == '?':
            question_mark_positions.append(i)
        else:
            total_known_hours += int(char)
    # Step2: Calculate remaining hours that need to be distributed
    remaining_hours = work_hours - total_known_hours
    num_questions_marks = len(question_mark_positions)
    
    # Step3: backtrack to find all valid distributions of remaining hours
    def backtrack(idx, hours_left, current_schedule):
        # Base case: if all question marks are replaced
        if idx == num_questions_marks:
            if hours_left == 0:
                schedules.append("".join(current_schedule))
            return
        
        # Get the position of the current question mark
        pos = question_mark_positions[idx]
        
        # try all possible valid hours for this position
        for hours in range(min(day_hours, hours_left)+1):
            current_schedule[pos] = str(hours)
            backtrack(idx + 1, hours_left - hours, current_schedule)
            
    # Prepare for backtracking
    schedules = []
    current_schedule = list(pattern)        
    
    # Step4: Start backtracking from the first question mark
    backtrack(0, remaining_hours, current_schedule)
    return sorted(schedules)

# O(k * n!): k is the number of valid schedules and n is the number of question marks.

if __name__ == "__main__":
    work_hours = 24
    day_hours = 4
    pattern = "08??840"
    print(findSchedules(work_hours, day_hours, pattern))
            
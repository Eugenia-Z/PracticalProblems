## Kaiqi's idea:
# use a dict to count how many transactions associated with each user. And then return all the user with a transaction times over than threshold
from collections import defaultdict

def processLogs(logs, threshold):
    trans_logs = defaultdict(int)
    for log in logs:
        log_record = log.split()
        sender = log_record[0]
        recipient = log_record[1]
        # Note: please note that using .get(x, 0) is not necessary since defaultdict(int) automatically initializes missing keys with a value of 0.
        # trans_logs[sender] = trans_logs.get(sender, 0) + 1  
        trans_logs[sender] += 1
        
        # Only count the recepient if they're different from the sender
        if recipient != sender:
            #trans_logs[recipient] = trans_logs.get(recipient, 0) + 1
            trans_logs[recipient] += 1
            
    # Filter out the users whose transaction count meets or exceeds the threshold
    res = [user for user, count in trans_logs.items() if count >= threshold]

    # .sort() methods sorts the list in place but returns None. should sort the list and return it instead.
    return sorted(res)

if __name__ == "__main__":
    logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
    threshold = 2
    print(processLogs(logs, threshold))
# input: array of impactValues of length n
# output: max # of creators can be supported while mainting a + netImpact

def maximizeCreatorSupport(impactValue):
    pos = [x for x in impactValue if x > 0]
    neg = [x for x in impactValue if x < 0]
    netrual = [x for x in impactValue if x == 0]
    
    curr_ppl = len(pos)
    net_pos = sum(pos)
    neg.sort()
  
    i = 0
    if net_pos == 0: 
        return 0
    else:
        curr_ppl += len(netrual)
        
        while net_pos > 0 and i<len(neg):
            net_pos += neg[i]
            curr_ppl += 1
            
    return curr_ppl - 1
            
impactValue = [2,1,1,-4]    
print(maximizeCreatorSupport(impactValue)) 
        
    
    
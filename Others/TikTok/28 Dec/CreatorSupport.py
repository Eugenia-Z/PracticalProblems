# input: array of impactValues of length n
# output: max # of creators can be supported while mainting a + netImpact

def maximizeCreatorSupport(impactValue):
    positive_impact = [val for val in impactValue if val > 0]
    negative_impact = [val for val in impactValue if val < 0]
    neutral_impact = [val for val in impactValue if val == 0]

    negative_impact.sort(reverse=True) # values are all negative
    
    # Start processing
    net_impact = sum(positive_impact)
    curr_ppl = len(positive_impact)
    
    if curr_ppl == 0: 
        return 0
    curr_ppl += len(neutral_impact)
    
    # Attempt to add negative impacts while maintaining positive net impact
    for impact in negative_impact:
        if net_impact + impact > 0:
            net_impact += impact
            curr_ppl += 1
        else:
            break
    
    return curr_ppl
        
    
    
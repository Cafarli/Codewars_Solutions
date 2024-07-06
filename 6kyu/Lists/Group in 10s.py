"""
Write a function groupIn10s which takes any number of arguments, groups them into tens, and sorts each group in ascending order.

The return value should be an array of arrays, so that numbers between 0 and9 inclusive are in position 0, numbers between 10 and 19 are in position 1, etc.

Here's an example of the required output:

grouped = group_in_10s(8, 12, 38, 3, 17, 19, 25, 35, 50) 

grouped[0]     # [3, 8]
grouped[1]     # [12, 17, 19]
grouped[2]     # [25]
grouped[3]     # [35, 38]
grouped[4]     # None
grouped[5]     # [50]
"""

def group_in_10s(*args):
    if len(args)==0:
        return []
    
    args = sorted(args)
    groups = {'none': []} if any(arg is None for arg in args) else {}
    
    for i in args:
        if i is None:
            groups['none'].append(None)
            
        key = i // 10
        if key not in groups:
            groups[key] = []
        groups[key].append(i)

    max_key = max(groups.keys())
    sorted_groups = [groups[k] if k in groups else None for k in range(max_key+1)]

    return sorted_groups

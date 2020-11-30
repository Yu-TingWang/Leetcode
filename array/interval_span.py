"""
https://leetcode.com/problems/merge-intervals/
No.56 Merge Intervals
----------------------------
https://leetcode.com/problems/non-overlapping-intervals/
No.435 Non-overlapping intervals
---------------------------
Morgan Stanley interview questions:
Given a list of intervals.
return the total length that is spanned. Note that the overlapped interval should count only once.
For example [[1,3],[2,6],[1,5],[3,7]]
it should return 7.
[[1,4],[6,9]] it should return 6.
"""
def total_length(intervals:list)->int:
    """
    intervals: list[list[int]]
    """
    merged = merge_intervals(intervals)
    total = 0
    for intervals in merged:
        total += intervals[1]-intervals[0]
    return total

def merge_intervals(intervals)->list:
    """
    intervals:list[list[int]]
    merge the overlapped intervals, return the list where each intervals are disjoint
    """
    # sort the intervals based on the start index
    intervals.sort(key = lambda i:i[0])
    print(intervals)
    result=[intervals[0]]
    for next_interval in intervals:
        curr = result.pop()
        curr_start , curr_end = curr[0], curr[1]
        next_start , next_end = next_interval[0] , next_interval[1]
        if curr_end >= next_start: # has overlapping, merge them
            curr_end  = max(curr_end,next_end)
            result.append([curr_start,curr_end])
        else:
            result.append(curr)
            result.append(next_interval)
    return result



if __name__ == "__main__":
    k = [[1,3],[2,6],[1,5],[3,7]]
    #print(merge_intervals(k))
    l = [[1,4],[6,9]]
    #print(merge_intervals(l))
    print(total_length(k))
    print(total_length(l))
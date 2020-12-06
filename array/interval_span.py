"""
https://leetcode.com/problems/merge-intervals/
No.56 Merge Intervals
----------------------------
https://leetcode.com/problems/non-overlapping-intervals/
No.435 Non-overlapping intervals
---------------------------
https://leetcode.com/problems/insert-interval/
No.57 Insert Interval
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
----------------------------
https://leetcode.com/problems/interval-list-intersections/
No.986 Interval List Intersections
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a
closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
----------------------------
Morgan Stanley interview questions:
Given a list of intervals.
return the total length that is spanned. Note that the overlapped interval should count only once.
For example [[1,3],[2,6],[1,5],[3,7]]
it should return 7.
[[1,4],[6,9]] it should return 6.
"""

def intervalIntersection(A:list,B:list)->list:
    result =[]
    i ,j = 0,0
    """
    as: start index of a interval; ae: end index of a interval
    bs: start index of b interval; be: end index of b interval
    as ≤ bs ≤ae ≤be --> update A [bs:ae]  ;bs≤ as ≤ be ≤ae --> update B [as:be]
    as ≤ ae ≤bs ≤be --> update A [ae:min(ae,bs)];bs≤ be ≤ as ≤ae --> update B [be:min(be,as)]
    as ≤ bs ≤be ≤ae --> udpate B [bs:be]  ;bs≤ as ≤ ae ≤be --> update A [as:ae]
    from the above, we can find out the pattern that there must be interval when
    as ≤ be and bs ≤ae
    """
    while i<len(A) and j<len(B):
        aStart , aEnd = A[i][0] ,A[i][1]
        bStart , bEnd = B[i][0] ,B[i][1]
        if aStart <= bEnd and bStart <= aEnd:
            start = max(aStart,bStart)
            end = min(aEnd,bEnd)
            result.append([start,end])
        if aEnd < bEnd:
            i+=1
        else:
            j+=1
    return result

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

def insert_interval(intervals:list, newInterval:list)->int:
    '''
    add newInterval to intervals, and call merge_intervals
    '''
    #intervals.append(newInterval)
    i = 0
    start_index = newInterval[0]
    end_index = newInterval[1]
    # find the index to insert newInterval to intervals such that intervals remains sorted
    while i < len(intervals):
        if intervals[i][0] < start_index:
            i += 1
        elif intervals[i][0] > start_index:
            break
        elif intervals[i][0] == start_index:
            if intervals[i][1] == end_index:
                return intervals
            if intervals[i][1] > end_index:
                i+=1
            break
    intervals.insert(i,newInterval)
    print(intervals)
    return merge_intervals(intervals)

if __name__ == "__main__":
    # k = [[1,3],[2,6],[1,5],[3,7]]
    # #print(merge_intervals(k))
    # l = [[1,4],[6,9]]
    # #print(merge_intervals(l))
    # # print(total_length(k))
    # # print(total_length(l))
    # l = [[1,3],[6,9]]
    # new_interval = [2,5]
    # print(insert_interval(l,new_interval))
    # l = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    # new_interval = [4,8]
    # print(insert_interval(l,new_interval))
    l = [[1,5]]
    new_interval = [2,7]
    print(insert_interval(l,new_interval))
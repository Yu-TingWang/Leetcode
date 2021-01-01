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
https://leetcode.com/problems/non-overlapping-intervals/
No.435 Non-overlapping intervals
Given a collection of intervals, find the minimum number of intervals you need to remove
to make the rest of the intervals non-overlapping.
"""


def non_overlapping_interval(intervals:list):
    '''
    Main idea: we try to built a non-overlapping intervals as more intervals as possible,
    then the difference between total intervals and the number of most intervals will be the minimum number of intervals
    we need to remove
    '''
    intervals.sort(key=lambda i: i[1])
    print(intervals)
    n, count = len(intervals),1
    if n==0: return 0
    curr = intervals[0]
    for i in range(n):
        print(curr,count)
        # if the end index of
        if curr[1]<=intervals[i][0]:
            count +=1
            curr = intervals[i]
    return n-count

    # '''
    # https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python
    # Which interval should be the best first(leftmost) interval to keep? One that ends first, as it leaves the most room
    # for the rest.
    # '''
    # intervals.sort(key= lambda i:i[1])
    # ending = float('inf')
    # removed = 0
    # for i in range(len(intervals)):
    #     if intervals[i][0]>=ending:
    #         ending = intervals[i][1]
    #     else:
    #         removed+=1
    # return removed

def intervalIntersection(A:list,B:list)->list:
    result =[]
    i ,j = 0,0
    """
    as: start index of a interval; ae: end index of a interval
    bs: start index of b interval; be: end index of b interval
    as ≤ bs ≤ae ≤be --> update A ,intersect at [bs:ae]  ;bs≤ as ≤ be ≤ae --> update B ,intersect at [as:be]
    as ≤ ae ≤bs ≤be --> update A ,intersect at [ae:min(ae,bs)];bs≤ be ≤ as ≤ae --> update B,intersect at[be:min(be,as)]
    as ≤ bs ≤be ≤ae --> update B ,intersect at [bs:be]  ;bs≤ as ≤ ae ≤be --> update A, intersect at [as:ae]
    from the above, we can find out the pattern that there must be interval when
    as ≤ be and bs ≤ae
    """
    while i < len(A) and j < len(B):
        print(i,A[i],j,B[j],end=',result')
        aStart, aEnd = A[i][0], A[i][1]
        bStart, bEnd = B[j][0], B[j][1]
        if aStart <= bEnd and bStart <= aEnd:
            start = max(aStart, bStart)
            end = min(aEnd, bEnd)
            result.append([start, end])
        # update the one that ends earlier
        print(result,end='update:')
        if aEnd < bEnd:
            print("i")
            i += 1
        else:
            print("j")
            j += 1
    return result

def total_length(intervals:list)->int:
    """
    intervals: list[list[int]],
    return the total length of all intervals, (remember that overlapped interval should only be count once)
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
            if intervals[i][1] >= end_index:
                # [start_index,end_index] is within the range of intervals[i], no need to modify intervals
                return intervals
            # since intervals are non-overlapping,
            # intervals[i][0]==start_index and intervals[i][1] > end_index,
            # then start_index must smaller than intervals[i+1][0], so i+1 is the index we need to insert
            if intervals[i][1] > end_index:
                i+=1
            # if intervals[i][0]==start_index and intervals[i][1] < end_index,
            # then i is the index we need to insert
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
    # l = [[1,5]]
    # new_interval = [2,7]
    # print(insert_interval(l,new_interval))
    # A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    # B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    # print('A',A,'B',B)
    # print(intervalIntersection(A,B))
    # print('-'*60)
    # print(intervalIntersection(B,A))
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(non_overlapping_interval(intervals))

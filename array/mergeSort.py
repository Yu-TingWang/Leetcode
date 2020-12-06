'''
Merge sort:
recursive approach - up to bottom
iterative approach - bottom to up

https://leetcode.com/problems/merge-sorted-array/
No.88. Merge Sorted Array


'''

def merge(nums1,m,nums2,n):
    '''
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
    Note:
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
    '''
    assert n == len(nums2), f"n must match for size of nums2. len(nums2):{len(nums2)}, n:{n}"
    assert len(nums1) == m+n, f"size of nums1 must be equal to m+n. len(nums1):{len(nums1)}, n:{n}"
    assert not any(nums1[m:]), f"nums1[m:] do not have enough space"
    while m>0 and n>0: # we start from the biggest number
        # since m,n is 1-based, and indexing is 0-based, we adjust m,n by 1
        if nums1[m-1] >= nums2[n-1]: # current biggest item in nums1 is bigger than /equal to that of in nums2
            nums1[m+n-1] = nums1[m-1] # then move it to end of nums1
            m-=1
        else:# current biggest item in nums2 is bigger than that of in nums1
            nums1[m+n-1] = nums2[n-1]
            n-=1
    # if nums2 still have items hasn't been compare, then they must smaller than the smallest item in nums1
    # by n>0, we know that m must reach 0 in the previous loop, so all m items in nums1 is in the right place now
    if n>0:
        nums1[:n] = nums2[:n]

def merge_recur(left, right):
    if len(left) == 0 or len(right) == 0:
        return left or right
    result = []
    i ,j = 0,0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result


def mergreSort_recursive(array: list):
    if len(array) < 2:
        return array
    middle = len(array) // 2
    left = mergreSort_recursive(array[:middle])
    right = mergreSort_recursive(array[middle:])
    return merge_recur(left, right)


def merge_iterative(array: list, left: int, mid: int, right: int):
    '''
    Modify array such that it is sorted
    '''
    n1 = mid - left + 1
    n2 = right - mid
    # Divide
    left_array, right_array =[] ,[]
    for i in range(n1):left_array.append(array[left+i])
    for i in range(n2):right_array.append(array[mid+i+1])
    # left_array = array[left:left + n1].copy()
    # right_array = array[mid + 1:mid + 1 + n2].copy()
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if left_array[i] > right_array[j]:
            array[k] = right_array[j]
            j += 1
        else:
            array[k] = left_array[i]
            i += 1
        k+=1
    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1


def mergeSort_iterative(array: list):
    curr_size = 1
    n = len(array)
    # outer loop for traversing each subarray of current_size
    while curr_size < n - 1:
        # inner loop for merge call in a sub array, each complete iteration sorts the the iterating sub-array
        left = 0
        while left < n - 1:
            # mid index = index (left subarray) + size(current sub-array) -1
            mid = min(left + curr_size, n) - 1
            right = min(2 * curr_size + left, n) - 1
            # merge call for each sub array
            merge_iterative(array, left, mid, right)
            left += curr_size * 2
        # increase sub-array size by multiple of 2
        curr_size *= 2


if __name__ == '__main__':
    # a = [12, 11, 13, 5, 6, 7]
    # print(a)
    # mergeSort_iterative(a)
    # print('iterative',a)
    # a = [12, 11, 13, 5, 6, 7]
    # k = mergreSort_recursive(a)
    # print('recursive',k)
    a = [2,5,6,0,0,0]
    k = [1,2,3]
    merge(a,3,k,3)
    print(a)

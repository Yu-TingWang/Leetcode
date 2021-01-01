import bisect
def insert_search(array:list,target:int):
    """
    Find the index to insert num, if there exists duplicated value in array, return
    the index i | array[:i] < target and array[i:] >= target.
    ex. to insert 5 in [1,2,5,7,8], return index = 2
    :param array: list[int], a sorted array
    :param target: the number to be inserted
    :return: the index to insert the number such that the array is still sorted
    """
    low=0
    high = len(array)-1
    while low<=high:
        mid = (low+high)//2
        if array[mid]==target:
            while mid>0 and array[mid-1]==target:
                mid-=1
            return mid
        elif array[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return low

def binary_find(array:list,target:int)->bool:
    """
    Iterative approach
    Find if target is in the array
    :param array: list[int], a sorted array
    :param target: int, the number to be searched
    :return:
    """
    low = 0
    high = len(array)-1
    while low<=high:

        mid= (low+high)//2
        print(low, mid,high)
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            high = mid-1
        else:
            low=mid+1
    return low

def binaryFind(array:list,target:int,left:int,right:int)->bool:
    """
    Recursive approach.
    Return the index of target in array, if not found, return -1.
    if there are multiple numbers equal to target in the array, return the first (left-most) index.
    :param array: list[int], a sorted array
    :param target: int, the number to be searched
    :param left: int, the start index, first stack call one would be 0
    :param right: int, the end index, first stack call one would be len(array)-1
    :return: if the target is in the array
    """
    if right>=left:
        mid = (left+right)//2
        if array[mid]==target:
            while mid>0 and array[mid-1]==target:
                mid-=1
            return mid
        elif array[mid]>target:
            return binaryFind(array,target,left,mid-1)
        else:
            return binaryFind(array,target,mid+1,right)
    else:
        return -1


def find_insert(array:list,target:int,start:int,end:int):
    if start==end:
        if array[start]>target:
            return start
        else:
            return start+1
    if start>end:
        return start
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    if target>array[mid]:
        return find_insert(array,target,mid+1,end)
    else:
        return find_insert(array,target,start,mid-1)


if __name__ == '__main__':
    array=[1,2,3,4,5,6,7,8,9]
    print(array)
    target=9
    #print(bisect.bisect(array,target))
    index = insert_search(array,target)
    #print(index)
    #array.insert(index,target)
    #print(array)
    #i = insert_search(array,5)
    # print(i)
    # i = binary_find(array,11)
    # print(i)
    print('-----------')
    a=[0,1,1,2,3]
    print(a)
    print(binaryFind(a,1,0,len(a)-1))
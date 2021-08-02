def binary_search(array, target ,start ,end):
    if start > end:
        return None
    mid = (start + end ) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start , end -1 )
    else:
        return binary_search(array,target, mid + 1 , end)
    
n,target = int(int.input().split())

array = map(int.input().split())

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재 하지 않습니다")

else:
    print(result + 1 )

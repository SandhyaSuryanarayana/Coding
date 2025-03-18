lst = [2,5,6,7,8,8,9,10,11,90]
target = 12

def find_closest(data,targer):
    low = 0
    high = len(lst) -1 

    min_diff = float("inf")
    closest_num = None

    while low<= high:
        mid = (low+high)//2

        if mid < len(data) -1:
            rmid_diff = abs(target-data[mid+1])
        if mid > 0:
            lmid_diff = abs(target-data[mid-1])

        if rmid_diff < min_diff :
            min_diff = rmid_diff
            closest_num = data[mid+1]
            #print("min_diff,closest_num 1",min_diff,closest_num)
        if lmid_diff < min_diff:
            min_diff = lmid_diff
            closest_num = data[mid-1]
            #print("min_diff,closest_num 2",min_diff,closest_num)
        
        if data[mid] < target:
            low = mid+1

        elif data[mid] > target:
            high = mid-1

        else:
            return mid
        
    return closest_num

res = find_closest(lst,target)        
print("The closest element to the target {} in the array is {}:".format(target,res))







        
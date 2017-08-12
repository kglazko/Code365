#This code returns the 2nd highest number of any array
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    #This is gross and I need to refactor this later
    max1 = -99999999999999
    max2 = -99999999999999
    for i in arr:
        if max1 < i:
            max2 = max1
            max1 = i
        else:
            if max2 < i and i != max1:
                max2 = i   
    print max2
        
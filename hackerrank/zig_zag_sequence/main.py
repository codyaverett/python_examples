def findZigZagSequence(a, n):
    a.sort() # Sort 
    mid = int(n/2) # Find mid
    a[mid], a[n-1] = a[n-1], a[mid] # swap last(biggest) number to mid

    st = mid + 1 # start at mid
    ed = n - 2 # last number
    while(st < ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)


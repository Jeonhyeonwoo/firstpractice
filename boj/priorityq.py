import heapq

def sync(arr): #max_arr에서 삭제 되거나 min_arr에서 삭제된걸 서로 삭제하기 위해서
    while arr and id[arr[0][1]] == 0:
        heapq.heappop(arr)

t = int(input())

for _ in range(t):
    max_arr = []
    min_arr = []
    id = [0] * 1000000
    k = int(input())
    for i in range(k):
        cmd,n = input().split()

        if cmd == 'I':
            heapq.heappush(max_arr,(-1*int(n),i))
            heapq.heappush(min_arr,(int(n),i))
            id[i] = 1
        else:
            if n == '1':
                sync(max_arr)
                if max_arr:
                    id[max_arr[0][1]] = 0
                    heapq.heappop(max_arr)
            elif n == '-1':
                sync(min_arr)
                if min_arr:
                    id[min_arr[0][1]] = 0
                    heapq.heappop(min_arr)

    sync(max_arr)
    sync(min_arr)

    if len(max_arr) == 0:
        print("EMPTY")
    else:
        print(-1*max_arr[0][0],end=" ")
        print(min_arr[0][0])
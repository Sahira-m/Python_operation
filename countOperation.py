# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    sumValue=0
    operation=0 
    print("start")
    sumValue =int("".join(str(x) for x in S), 2)                  
    while(sumValue):
        if((sumValue)%2==0):
            sumValue=int(sumValue//2)
            operation=operation+1
        else:
            sumValue=int(sumValue-1)  
            operation=operation+1  
    return operation  
print(solution("10101010"))

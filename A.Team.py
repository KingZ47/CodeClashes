#CODE FORCES // PROBLEM SET
#Input: The first input line contains a single integer n (1 ≤ n ≤ 1000) — the number of problems in the contest. Then n lines contain three integers each, each integer 
        #is either 0 or 1. If the first number in the line equals 1, then Petya is sure about the problem's solution, otherwise he isn't sure. The second number shows Vasya's 
        #view on the solution, the third number shows Tonya's view. The numbers on the lines are separated by spaces.
#Output: Print a single integer — the number of problems the friends will implement on the contest.
#-------------------
n=int(input())
s=0
for i in range(n):
    m=input().split()
    if m.count("1")>=2:
        s+=1
print(s)

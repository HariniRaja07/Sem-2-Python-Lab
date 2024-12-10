#5.counting the odd and even numbers.
n=int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
even=0
odd=0
l1=[]
l2=[]
for i in list1:
    if i%2==0:
        even+=1
        l1.append(i)
    else:
        odd+=1
        l2.append(i)
print(f"The list of Even Numbers: {l1} occured {even} times")
print(f"The list of Odd Numbers: {l2} occured {odd} times")

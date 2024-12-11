user=input()
c1=0
c2=0
capital=[]
small=[]
for i in user:
    if i in ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"):
        capital.append(i)
        c1+=1
    elif i in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"):
        small.append(i)
        c2+=1

print("The count of Capital:",c1)
print("The count of Small:",c2)





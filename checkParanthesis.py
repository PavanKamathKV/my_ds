st=[]
def push(e):
    st.append(e)

def pop():
    e = st.pop()
    return e

flag=0
b="{ [ ( )] }"
b=b.replace(" ","")
print(b)
dic={
    "]":"[",
    "}":"{",
    ")":"("
}
for i in b:
    if i in dic.values() and i not in dic.keys():
        push(i)
    elif i in dic.keys():
        top=len(st)
        if dic[i]==st[top-1]:
            e=pop()
        else:
            print("invslid exp") 
            flag=1
            break
    else:
        print("invalid char ")
        flag=1
        break

if len(st)==0 and flag==0:
    print("valid")
else:
    print("invalid")
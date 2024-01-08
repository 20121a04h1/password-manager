def view():
    with open("D:\\html\\password.txt",'r') as f:
        import os
        n=os.path.getsize("D:\\html\\password.txt")
        if n==0:
            print("none")
        else:
            for i in f.readlines():
                print(i.rstrip())
def add():
    u=input("enter username:")
    p=input("enter password:")
    with open("D:\\html\\password.txt",'w') as f:
        f.write("username:"+u+" "+"password:"+p)
paw=input("enter master password:").lower()
if paw=="20121a04h1":
    while True:
        v=input("view or add password?").lower()
        if v=="view password":
            view()
        elif v=='add password':
            add()
        else:
            print("invalid")
        
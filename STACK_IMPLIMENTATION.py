class stack:
    def __init__(self):
        self.stk=[]

    def push(self):
        print("How much values you want to enter in stack: ",end=" ")
        val=int(input())
        for i in range(1,val+1):
            value=int(input())
            self.stk.append(value)
            
    def pop(self):
        if self.stk==[]:
            print("stack is empty")
        else:
            return self.stk.pop()

    def display(self):
        print(self.stk)

    def exit_stk(self):
        exit()

obj=stack()
ch='y'
while ch=='y':
    print("What do you want to do in stack\n1. Insert\n2. Delete\n3. Display\n4. Exit\nEnter your choice")
    choice=int(input())
    if choice==1:
        obj.push()
    elif choice==2:
        obj.pop()
    elif choice==3:
        obj.display()
    elif choice==4:
        obj.exit_stk()
    print("Do you want to continue: \n Then press y")
    ch=str(input())



class queue:

    def __init__(self):
        self.que=[]

    def insert(self):
        print("How much elements do you want to enter in queue: ",end=" ")
        ele=int(input())
        for i in range(1,ele+1):
            value=int(input())
            self.que.append(value)

    def delete(self):
        if self.que==[]:
            print("Queue is empty")
        else:
            return self.que.pop(0)

    def display(self):
        print(self.que)

    def ext(self):
        exit()

obj=queue()
ch='y'
while ch=='y':
    print("What do you want to do in Queue\n1. Insert\n2. Delete\n3. Display\n4. Exit\nEnter your choice")
    choice=int(input())
    if choice==1:
        obj.insert()
    elif choice==2:
        obj.delete()
    elif choice==3:
        obj.display()
    elif choice==4:
        obj.ext()
    print("Do you want to continue: \n Then press y")
    ch=str(input())

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
        # to check if stack is empty

    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
        
    def size(self):
        return len(self.stack)
    
stack=Stack()
stack.push(10)
stack.push(20)
print("Top element: ", stack.top())
stack.pop()
print("Top element after pop: ", stack.top())
user_input = int(input("Which number do you want to push onto the start?: "))
stack.push(user_input)
print("The stack after push is:", stack)

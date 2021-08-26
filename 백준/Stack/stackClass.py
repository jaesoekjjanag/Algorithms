class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.itmes.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty")

    def __len__(self):
        return len(self.items)

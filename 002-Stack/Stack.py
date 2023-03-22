
class Stack():

    def __init__(self) -> None:
        self.list = []

    def push(self, value: int):
        self.list.append(value)

    def pop(self):
        if self.isEmpty() == True:
            return
        self.list.pop()

    def peek(self):
        if self.isEmpty() == True:
            return
        return self.list[len(self.list) - 1]

    def isEmpty(self):
        if (self.list == []):
            return True
        return False

    def deleteStack(self):
        self.list = []


def main():
    

    s = Stack()


    print(s.isEmpty())

    s.push(7)
    s.push(6)
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)

    print(s.peek())

    s.pop()
    s.pop()
    s.pop()

    print(s.peek())

    s.deleteStack()

    print(s.peek())



if __name__ == "__main__":
    main()
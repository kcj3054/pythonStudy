

def mainStack():
    stack = []
    stack.append(1)   # push
    stack.append(2)
    stack.append(3)
    stack.append(4)
    print(stack)
    while stack:
        print("pop >", stack.pop())


def mainQueue():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    print(queue)

    while queue:
        print("pop >", queue.pop(0))    
mainStack()
mainQueue()



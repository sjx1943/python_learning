count = 1

def a():
    count = 'a函数里面'
    def b():

        nonlocal count
        print(count)
        count = 2
    b()
    print(count)

if __name__ == '__main__':
    a()
    print(count)
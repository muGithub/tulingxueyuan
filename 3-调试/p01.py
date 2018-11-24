def SayHello(name):
    print("Hello, {0}".format(name))


if __name__ == "__main__":
    print("****"*20)
    name = input("input:")
    print(SayHello(name=name))
    print("@@"*30)
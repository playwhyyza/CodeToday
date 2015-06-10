import sys

def show():
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = "world"
    print "hello " + name

def main():
    show()

if __name__== '__main__':
    main()

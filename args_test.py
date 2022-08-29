import sys

def main():
    print(f"# of arguments: {len(sys.argv)}")
    print(f"Arguments List: {str(sys.argv)}")
    print(f"{str(sys.argv[1])}")

def show_output(): 
    pass

if __name__ == '__main__':
    main()

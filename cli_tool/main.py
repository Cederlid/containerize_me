import sys

def main():
    if len(sys.argv) > 1:
        print(f'Hello, {sys.argv[1]}!')
    else:
        print('Hello from CLI tool!')

if __name__ == '__main__':
    main()

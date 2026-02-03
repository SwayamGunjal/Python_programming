import os

def main():
    print("PID of running process is :",os.getpid())    # Process ID
    print("PID of parent process is :",os.getppid())    # Parent ID

if __name__ == "__main__":
    main()
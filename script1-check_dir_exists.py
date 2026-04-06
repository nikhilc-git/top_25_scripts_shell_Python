import os, sys

#check the legth of inpurt agrs
if len(sys.argv) < 2:
    print("Please provide the dir name to check.")
    print("Usage: script.py <dir>")
    sys.exit(1)



def main():
    try:
        
        dirr = sys.argv[1]
        if os.path.isdir(dirr):
            print(f"Dir {dirr} is exist.")
            count = sum(1 for entry in os.scandir(dirr))
            print(f"The file and dir inside the {dirr}: {count}")

        else:
            print(f"The dir {dirr} is not exist, hence creating the dir...")
            os.mkdir(dirr)
            print("Created the dir {dirr}..")
    except Exception as e:
        print(f"Error is: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

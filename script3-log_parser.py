import sys,os

if len(sys.argv) < 3:
    print("Please provide the path of log file and temp file storing the error logs.\n")
    print("Usage: script.py <log file path> <error log file>.")
    sys.exit(1)

log_file = sys.argv[1]
error_file = sys.argv[2]

#print(log_file)

if os.path.isfile(log_file):
    print(f"The provided log file {log_file} is valid.")
    
    with open(log_file, "r") as f:
        error_count = sum( 1 for line in f if "ERROR" in line)

    print(f"The number of error lines in {log_file} file:: {error_count}")
    print("Moving the error log lines to temp file.")

    moved_error_lines = False

    with open(log_file,"r") as src, open(error_file,"w") as dest:
        for line in src:
            if "ERROR" in line:
                dest.write(line)
                moved_error_lines = True

    if moved_error_lines:
        print("Error lines moved successfully.")

else:
    print("Please provide the valid log file.")
    sys.exit(1)



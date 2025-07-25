import re


def find_patterns_in_log(log_file_path, pattern):
    """
    Searches for a specified pattern in a log file and prints the matching lines.

    Args:
        log_file_path (str): The path to the log file.
        pattern (str): The regular expression pattern to search for.
    """
    error={}
    info={}
    warning={}
    error_count=0
    info_count=0
    warning_count=0
    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                if re.search(pattern, line):
                    print(line.strip())
                    if 'ERROR' in line.strip():
                        error["ERROR"]=line.strip()
                        error_count=error_count+1
                        print("Error Count="+str(error_count))
                        print(error)
                    if 'WARNING' in line:
                        warning["WARNING"]=line.strip()
                        warning_count = warning_count + 1
                        print("Warning Count=" + str(warning_count))
                        print(warning)
                    if 'INFO' in line:
                        info["INFO"]=line.strip()
                        info_count = info_count + 1
                        print("Info Count=" + str(info_count))
                        print(info)
                    print(error)
                    print(warning)
                    print(info)

    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # print(error)
    # print(warning)
    # print(info)
# Example usage:
log_file = 'example.log'

# Example log file content:
# 2024-07-20 10:00:00 INFO: User logged in successfully.
# 2024-07-20 10:01:00 WARNING: Invalid password attempt for user.
# 2024-07-20 10:02:00 ERROR: Database connection failed.
# 2024-07-20 10:03:00 INFO: User logged out.
# 2024-07-20 10:04:00 ERROR: Another database connection failure.
# 2024-07-20 10:05:00 INFO: Server started.

error_pattern = r'ERROR: .*'  # Matches lines starting with "ERROR:"
find_patterns_in_log(log_file, error_pattern)
# Expected output:
# 2024-07-20 10:02:00 ERROR: Database connection failed.
# 2024-07-20 10:04:00 ERROR: Another database connection failure.

warning_pattern = r'WARNING: .*'  # Matches lines starting with "WARNING:"
find_patterns_in_log(log_file, warning_pattern)

warning_pattern = r'INFO: .*'  # Matches lines starting with "WARNING:"
find_patterns_in_log(log_file, warning_pattern)
# Expected output:
# 2024-07-20 10:01:00 WARNING: Invalid password attempt for user.

import re
def find_patterns_in_log(log_file_path, pattern):
    """
    Searches for a specified pattern in a log file and prints the matching lines.

    Args:
        log_file_path (str): The path to the log file.
        pattern (str): The regular expression pattern to search for.
    """
    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                if re.search(pattern, line):
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


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
# Expected output:
# 2024-07-20 10:01:00 WARNING: Invalid password attempt for user.


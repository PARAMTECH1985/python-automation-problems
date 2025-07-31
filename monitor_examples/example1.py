import time


def monitor_log_polling(log_file_path):
    with open(log_file_path, 'r') as f:
        f.seek(0, 2)  # Go to the end of the file initially
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)  # Wait for new lines
                continue
            print(line.strip())  # Process the new log line


monitor_log_polling('path/to/your/logfile.log')

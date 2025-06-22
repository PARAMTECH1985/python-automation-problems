import re


class PatternMatch:
    def __init__(self):
        print("Initialization")

    def findPatternAndPrintLine(self, log_File_Path, pattern):
        with open(log_File_Path, 'r') as file:
            print("Reading the file")
            for line in file:
                if re.search(pattern, line):
                    print(line.strip())


log_file = "example.log"
p = PatternMatch()
pattern = "WARNING"
p.findPatternAndPrintLine(log_file, pattern)
pattern = "INFO"
p.findPatternAndPrintLine(log_file, pattern)
pattern = "ERROR"
p.findPatternAndPrintLine(log_file, pattern)
pattern = "NO_PATTERN"
p.findPatternAndPrintLine(log_file, pattern)

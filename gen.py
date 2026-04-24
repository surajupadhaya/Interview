# Dummy log file content for testing
logs = [
    "INFO: Server-01: Heartbeat OK",
    "CRITICAL: Server-02: Disk Failure",
    "WARNING: Server-01: High CPU",
    "CRITICAL: Server-03: Network Down",
    "INFO: Server-04: Backup Complete",
    "CRITICAL: Server-02: Power Supply Fail",
    "CRITICAL: Server-05: Kernel Panic"
]

def log_streamer(log_list):
    """
    TASK 1: Create a generator that yields one line at a time.
    """
    for line in log_list:
        yield line

def critical_filter(stream):
    """
    TASK 2: Create a generator that takes the stream and 
    only yields if the line contains 'CRITICAL'.
    """
    for line in stream:
        if "CRITICAL" in line:
            yield line

# --- YOUR IMPLEMENTATION HERE ---

# 1. Initialize the log_streamer
# 2. Pass that into critical_filter
# 3. Use a loop to grab ONLY the first 3 critical errors and print them.
streamer=log_streamer(logs)
filter=critical_filter(streamer)

print(next(filter))
print(next(filter))
print(next(filter))
#for line in filter:
#    print(line)
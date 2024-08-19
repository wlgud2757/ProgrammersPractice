import sys
from datetime import datetime, timedelta

def check_diff(start, end):
    start_time = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    diff = end_time - start_time
    return diff.total_seconds() / 60

def check_time(times):
    total_min = 0
    for start, end in times:
        total_min += check_diff(start, end)
    return int(total_min)

def main():
    times = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        start, end = line.split()
        times.append((start, end))
    
    result = check_time(times)
    print(result)

if __name__ == "__main__":
    main()

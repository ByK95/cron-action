import sys
from datetime import datetime, timezone, timedelta

CUTOFF = timedelta(days=20)


def send_slack_notification(task_name):
    print("slack notification send", task_name)


if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line)

    size = int(len(lines) / 2)
    times = [time[time.find('(')+1:time.find(')')] for time in lines[:size]]
    times = [datetime.strptime(time, "%a %b %d %H:%M:%S %Y %z") for time in times]
    tasks = [task.replace('\n', '') for task in lines[size:]]

    NOW = datetime.now(timezone.utc)
    for index, time in enumerate(times):
        timediff = NOW - time
        if timediff > CUTOFF:
            send_slack_notification(tasks[index])



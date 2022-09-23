import sys
from datetime import datetime, timezone, timedelta


def send_slack_notification(task_name):
    print("slack notification send", task_name)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Missing difference delta as (days: int) argument")
        sys.exit(2)

    CUTOFF = timedelta(days=int(sys.argv[1]))
    lines = []
    for line in sys.stdin:
        lines.append(line)

    size = int(len(lines) / 2)
    times = [time[time.find('(') + 1:time.find(')')] for time in lines[:size]]
    times = [datetime.strptime(time, "%a %b %d %H:%M:%S %Y %z") for time in times]
    tasks = [task.replace('\n', '') for task in lines[size:]]

    filtered = []
    expired = []
    NOW = datetime.now(timezone.utc)
    for index, time in enumerate(times):
        filtered.append("{} {}".format(tasks[index], times[index]))
        timediff = NOW - time
        if timediff > CUTOFF:
            expired.append("{} {}".format(tasks[index], times[index]))
            send_slack_notification(tasks[index])

    print("::set-output name=filtered::{}".format("\n".join(filtered)))
    print("::set-output name=expired::{}".format("\n".join(expired)))
    print("\n".join(filtered))
    print("\n".join(expired))
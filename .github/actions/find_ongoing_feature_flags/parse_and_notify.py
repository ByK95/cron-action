import sys
from datetime import datetime, timezone, timedelta
import ipdb

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Missing difference delta as (days: int) argument")
        sys.exit(2)

    CUTOFF = timedelta(days=int(sys.argv[1]))
    lines = []
    for line in sys.stdin:
        lines.append(line)

    size = int(len(lines) / 2)
    times = []
    authors = []
    for line in lines[:size]:
        author, time = line.split('-')
        time = time[time.find('(') + 1:time.find(')')]
        times.append(datetime.strptime(time, "%a %b %d %H:%M:%S %Y %z"))
        authors.append(author)

    tasks = [task.replace('\n', '') for task in lines[size:]]

    filtered = []
    expired = []
    NOW = datetime.now(timezone.utc)
    for index, time in enumerate(times):
        filtered.append("{} {}".format(authors[index], tasks[index]))
        timediff = NOW - time
        if timediff > CUTOFF:
            expired.append("{} {}".format(authors[index], tasks[index]))

    print("::set-output name=filtered::{}".format(",".join(filtered)), flush=True)
    print("::set-output name=results::{}".format(",".join(expired)), flush=True)


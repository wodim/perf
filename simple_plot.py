import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy
import sqlite3

connection = sqlite3.connect("plot.sqlite")
cursor = connection.cursor()

cursor.execute("SELECT _timestamp, accepted_conn, listen_queue, active_processes, total_processes, _elapsed FROM plot WHERE _timestamp >= DATETIME('NOW', '-7 DAY')")

_timestamp, accepted_conn, listen_queue, active_processes, total_processes, _elapsed = zip(*cursor.fetchall())
accepted_conn = [i if i >= 0 else 0 for i in [0] + list(numpy.diff(accepted_conn))]

plt.figure()
plt.plot(range(len(_timestamp)), accepted_conn, linewidth=0.3)
plt.xticks(range(len(_timestamp)), _timestamp, size=2, rotation=90)
plt.savefig("accepted_conn.png", dpi=1000)

plt.figure()
plt.plot(range(len(_timestamp)), listen_queue, linewidth=0.3)
plt.xticks(range(len(_timestamp)), _timestamp, size=2, rotation=90)
plt.savefig("listen_queue.png", dpi=1000)

plt.figure()
plt.plot(range(len(_timestamp)), active_processes, linewidth=0.3)
plt.plot(range(len(_timestamp)), total_processes, linewidth=0.3)
plt.xticks(range(len(_timestamp)), _timestamp, size=2, rotation=90)
plt.savefig("processes.png", dpi=1000)

plt.figure()
plt.plot(range(len(_timestamp)), _elapsed, linewidth=0.3)
plt.xticks(range(len(_timestamp)), _timestamp, size=2, rotation=90)
plt.savefig("_elapsed.png", dpi=1000)

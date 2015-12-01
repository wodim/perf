import json
import requests
import sqlite3
import time

before = time.time()
r = requests.get("http://lalala/status.php?full&json")
elapsed = time.time() - before
j = json.loads(r.text)

connection = sqlite3.connect("plot.sqlite")
cursor = connection.cursor()

cursor.execute("""INSERT INTO plot (process_manager, start_time, start_since, accepted_conn,
                  listen_queue, max_listen_queue, active_processes, total_processes, _elapsed)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                  (j["process manager"], j["start time"], j["start since"], j["accepted conn"],
                  j["listen queue"], j["max listen queue"], j["active processes"], j["total processes"],
                  elapsed))

connection.commit()
connection.close()
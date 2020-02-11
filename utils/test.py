import subprocess
import os
import time


tests = [
    "python-flask-dev-file-none",
    "python-flask-dev-file-preload",
    "python-tornado-tornado-file-none",
    "python-tornado-tornado-file-preload",
]

for t in tests:
    subprocess.run(["docker-compose", "up", "-d", t], cwd="../speed-tests")
    time.sleep(2)
    subprocess.run(["docker-compose", "run", "wrk", "-c64", "-d5s",
                    "-t8", "-s", "urls.lua", "http://{}/bbUISe".format(t)], cwd="../speed-tests")
    subprocess.run(["docker-compose", "down"], cwd="../speed-tests")
    os.rename("../speed-tests/result.json", "reports/{}.json".format(t))

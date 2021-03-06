import subprocess
import os
import time


tests = [
    "python-flask-dev-file-none",
    "python-flask-dev-file-preload",
    "python-flask-gunicorn1-file-preload",
    "python-flask-gunicorn2-file-preload",
    "python-flask-gunicorn4-file-preload",
    "python-flask-gunicorn8-file-preload",
    "python-flask-gunicorn16-file-preload",
    "python-flask-gunicorn1-mainheld-file-preload",
    "python-flask-gunicorn2-mainheld-file-preload",
    "python-flask-gunicorn4-mainheld-file-preload",
    "python-flask-gunicorn8-mainheld-file-preload",
    "python-flask-gunicorn16-mainheld-file-preload",
    "python-flask-gunicorn1-gevent-file-preload",
    "python-flask-gunicorn2-gevent-file-preload",
    "python-flask-gunicorn4-gevent-file-preload",
    "python-flask-gunicorn8-gevent-file-preload",
    "python-flask-gunicorn16-gevent-file-preload",
    "python-flask-gunicorn1-eventlet-file-preload",
    "python-flask-gunicorn2-eventlet-file-preload",
    "python-flask-gunicorn4-eventlet-file-preload",
    "python-flask-gunicorn8-eventlet-file-preload",
    "python-flask-gunicorn16-eventlet-file-preload",
    "python-flask-gevent-file-preload",
    "python-flask-twisted-file-preload",
    "python-flask-uwsgi1-file-preload",
    "python-flask-uwsgi2-file-preload",
    "python-flask-uwsgi4-file-preload",
    "python-flask-uwsgi8-file-preload",
    "python-flask-uwsgi16-file-preload",
    "python-tornado-tornado-file-none",
    "python-tornado-tornado-file-preload",
    "python-flask-apache-wsgi-file-preload",
    "go-http",
    "go-fast-http",
]

subprocess.run(["docker-compose", "build"], cwd="../speed-tests")

for i in range(3):
    for t in tests:
        subprocess.run(["docker-compose", "up", "-d", t], cwd="../speed-tests")
        time.sleep(2)
        subprocess.run(["docker-compose", "run", "wrk", "-c64", "-d5s",
                        "-t8", "-s", "urls.lua", "http://{}/bbUISe".format(t)], cwd="../speed-tests")
        subprocess.run(["docker-compose", "down"], cwd="../speed-tests")
        pth = os.path.join("reports", str(i))
        if not os.path.exists(pth):
            os.mkdir(pth)
        os.rename("../speed-tests/result.json", "reports/{}/{}.json".format(str(i), t))

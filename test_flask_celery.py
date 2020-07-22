## start redis (depercated)
## redis-server

## start mongodb
# mongod --dbpath /Users/zhiyul/Documents/Projects/wherecovid19/VNE/mongodb
# https://stackoverflow.com/questions/15740755/working-example-of-celery-with-mongo-db/17127115
## start celery worker
# celery -A test_flask_celery.celery worker -E -l info
## start flower
# celery flower -A test_flask_celery --address=127.0.0.1 --port=5555
## start beat
# celery -A test_flask_celery.celery beat -l info
## start flask
# FLASK_APP=test_flask_celery.py flask run

from VulnerablePOP4_celery import my_main_run
import uuid
from flask import jsonify
from celery import Celery
from flask import Flask
from flask import request


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


flask_app = Flask(__name__)
flask_app.config.update(
    # CELERY_BROKER_URL='redis://localhost:6379',
    # CELERY_RESULT_BACKEND='redis://localhost:6379'
    CELERY_BROKER_URL='mongodb://localhost:27017/celery',
    CELERY_RESULT_BACKEND='mongodb'
)
celery = make_celery(flask_app)


@flask_app.route('/')
def hello_world():
    return 'Hello, World!'

@celery.task()
def add_together(a, b):
    return a + b


@celery.task()
def su_task(job_id, base_output_path):
    my_main_run(job_id=job_id, base_output_path=base_output_path)
    return "OK"

base_output_path="/tmp"

@flask_app.route('/su')
def submit_job_su():
    job_id = str(uuid.uuid4())
    job_id = "su_" + job_id

    t = su_task.apply_async(
        task_id=job_id,
        countdown=1,
        kwargs={'job_id': job_id,
                'base_output_path': base_output_path},
    )

    return jsonify({"job_id": job_id, "status": t.state})


@flask_app.route('/job')
def job_status():
        job_id = request.args.get('job_id', None)
        try:
            if job_id:
                resp_dict = {"job_id": job_id}
                result = su_task.AsyncResult(job_id)
                job_status = result.state.lower()
                resp_dict["status"] = job_status
                return jsonify(resp_dict)
            else:
                return jsonify({"error": "No job_id is provided"})
        except Exception as ex:
            print(str(ex))
            return jsonify(message=str(ex), status=500), 500

from datetime import timedelta

## celery app configuration
celery.conf.CELERYBEAT_SCHEDULE = {
    'run-every-1-minute': {
        'task': 'test_flask_celery.add_together',
        "args": (10, 16),
        'schedule': timedelta(seconds=60),
    },
}

celery.conf.CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "localhost",
    "port": 27017,
    "database": "celery",
    "taskmeta_collection": "celery_task_results",}


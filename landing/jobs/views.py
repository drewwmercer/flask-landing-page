from flask import jsonify
from landing import app

# json
@app.route('/jobs/')
def jobs_api():
    data = {'job_id': 23, 'tasks': ['work', 'werk', 'wurk']}
    return jsonify(data)

# more dynamic routing
@app.route('/jobs/<job_id>/')
def jobs(job_id):
    return '<p>job id: {job_id}</p>'.format(job_id=job_id)
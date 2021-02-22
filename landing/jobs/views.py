from landing import app

# more dynamic routing
@app.route('/jobs/<job_id>/')
def jobs(job_id):
    return '<p>job id: {job_id}</p>'.format(job_id=job_id)
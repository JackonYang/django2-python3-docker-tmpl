from flask import Flask
# from flask import abort, request

app = Flask(__name__)


heartbeat_url = "/heartbeat/"
heartbeat_file = "/http-mock/heartbeat/running.json"


@app.route("/")
def hello():
    return "Hello World!"


@app.route(heartbeat_url)
def heartbeat():
    # param = request.args.get('param', None)
    # if not param:
    #     abort(400)

    with open(heartbeat_file, 'r') as f:
        data = ''.join(f.readlines())

    return app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )

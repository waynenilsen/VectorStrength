
import database
from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('sensors.html')


@app.route('/data', methods=['GET', 'POST'])
def post_data():
    if request.method == 'POST':
        data = request.get_json()
        database.add_record(data)
        return "OK"
    elif request.method == 'GET':
        return app.send_static_file('database.db')
    else:
        abort(404)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        app.run('0.0.0.0', 5000)

    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()

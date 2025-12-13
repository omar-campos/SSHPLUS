from flask import Flask, send_file

app = Flask(__name__)

@app.route('/checkuser')
def servir_archivo():
    return send_file('/root/checkuser.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET','POST'] )
def index():
    return "<h1> this is an flask application</h1>"

if __name__ == "__main__":
    app.run()
# for histing the heroku we install requiremnts file
# we are installing gunicorn will allow us to run on linux envirolment
# heroku is an application which will run on VM  it will run on linux
# gunicon will allow us to run server


import flask,sys
import logging
logging.getLogger("werkzeug").disabled = True
app = flask.Flask(__name__)
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None
@app.route("/")
def giveAnswer():
    global word
    return word
app.run("0.0.0.0",9200)

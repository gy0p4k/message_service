from flask import Flask, render_template, request
import uuid
app = Flask(__name__)

messages = {}


@app.route('/')
def send_pm():
    return render_template('text.html')


@app.route('/generate', methods=['POST'])
def link():
    text = request.form['message']
    link = uuid.uuid4().hex
    messages[link] = text
    return "http://pm-me.herokuapp.com/pm/" + link


@app.route('/pm/<link>')
def view_pm(link):
    try:
        text = messages[link]
        del messages[link]
        return text
    except:
        return "no messages"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

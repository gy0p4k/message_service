from flask import Flask, render_template, request
import uuid
app = Flask(__name__)

base_url = "http://pm-me.herokuapp.com/pm/"
messages = {}


@app.route('/')
def send_pm():
    return render_template('text.html')


@app.route('/generate', methods=['POST'])
def link():
    link = uuid.uuid4().hex
    messages[link] = request.form['message']
    return base_url + link


@app.route('/pm/<link>')
def view_pm(link):
    try:
        return message.pop(link)
    except:
        return "no messages"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

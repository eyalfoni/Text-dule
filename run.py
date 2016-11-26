from flask import Flask, request, session
from twilio.rest import TwilioRestClient
from Schedule import Schedule
from Event import Event
import twilio.twiml
import os

SECRET_KEY = os.environ.get('TWILIO_AUTH_TOKEN')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = TwilioRestClient(account_sid, auth_token)
TEST_NUMBER = os.environ.get('TWILIO_TEST_NUMBER')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

app = Flask(__name__)
app.config.from_object(__name__)

schedule = Schedule()


@app.route("/", methods=['GET', 'POST'])
def run_server():

    print type(request.values)
    body = request.values.get('Body', None)
    body = body.split()

    event = body[0].lower()
    resp = None
    if event == 'add':
        resp = add_event(body)
    elif event == 'remove':
        resp = remove_event(body)
    elif event == 'show':
        resp = show_all()

    return str(resp)


def add_event(body):
    event_title = " ".join(body[1:])
    event = Event(event_title)
    schedule.add(event)

    resp = twilio.twiml.Response()
    mssg = "Event added. \n"
    resp.message(mssg)

    return resp


def remove_event(body):
    event_title = " ".join(body[1:])
    event = Event(event_title)
    schedule.remove(event)

    resp = twilio.twiml.Response()
    mssg = "Event removed. \n"
    resp.message(mssg)

    return resp


def show_all():
    resp = twilio.twiml.Response()
    mssg = schedule.to_str()
    resp.message(mssg)

    return resp


# Sets up schedule if none is found in session
def setup_sessions():
    schedule = session.get('Schedule', None)
    if schedule is None:
        session['Schedule'] = Schedule()

if __name__ == "__main__":
    app.run(debug=True)

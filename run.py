from flask import Flask, request, session
import twilio.twiml
import os

SECRET_KEY = os.environ.get('TWILIO_AUTH_TOKEN')
app = Flask(__name__)
app.config.from_object(__name__)

contacts = {
}


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    """
    # Example of session - to/from number identifier
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter

    """

    """
    # Example of parsing text message for commands.
    body = request.values.get('Body', None)
    body = body.split()
    """

    if body[0] == 'ADD:':
        resp = twilio.twiml.Response()
        mssg = "correct answer buddy"
        resp.message(mssg)
    from_num = request.values.get('From', None)
    if from_num in contacts:
        mssg = "".join([contacts[from_num], ", thanks for texting!"])
    else:
        mssg = "Hello, Mobile Monkey"

    # resp = twilio.twiml.Response()
    # resp.message(mssg)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

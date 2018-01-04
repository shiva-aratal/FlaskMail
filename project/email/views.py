from flask import jsonify, request, Blueprint
from flask import current_app as flask_app
from flask_mail import Message
from .. import mail


email_blueprint = Blueprint('email', __name__)


def send_email():
	content = request.get_json()

	validContent = False
	if 'to' in content and 'subject' in content and 'body' in content and 'from' in content:
		validContent = True

	response = sg.client.mail.send.post(request_body=mail.get())
		return jsonify({'Message': 'Email Sent'})
	else:
		return jsonify({'Error': 'Missing Parameters'})



def send_test_email():
	content = request.get_json()

	validContent = False
	if 'to' in content and 'subject' in content and 'body' in content:
		validContent = True
	if validContent:
		return jsonify({'Message': 'Input Parameters Returned', 'Mail send to': content['to'], 'Mail Subject': content['subject'],
			'Mail Body': content['body']})
	else:
		return jsonify({'Error': 'Missing Input'})
from flask import jsonify, request, Blueprint
from flask import current_app as flask_app
from flask_mail import Message
from .. import mail
import os
import sendgrid
from sendgrid.helpers.mail import *
sg = sendgrid.SendGridAPIClient(apikey="SG.APIKey")




email_blueprint = Blueprint('email', __name__)




@email_blueprint.route('/email', methods=['POST'])
def send_email():
	content = request.get_json()

	validContent = False
	if 'to' in content and 'subject' in content and 'body' in content and 'from' in content:
		validContent = True
	if validContent:
		from_email = Email(content['from'])
		to_email = Email(content['to'])
		subject = content['subject']
		content_body = Content("text/plain",content['body'])
		mail = Mail(from_email, subject, to_email, content_body)

		response = sg.client.mail.send.post(request_body=mail.get())
		return jsonify({'Message': 'Email Sent'})
	else:
		return jsonify({'Error': 'Missing Parameters'})


@email_blueprint.route('/testapp', methods=['POST'])
def send_test_email():
	content = request.get_json()

	validContent = False
	if 'to' in content and 'subject' in content and 'body' in content:
		validContent = True
	if validContent:
		return jsonify({'Message': 'Input Parameters Returned', 'Mail send to': content['to'], 'Mail Subject': content['subject'],
			'Mail Body': content['body']})
	else:
		return jsonify({'Error': 'Invalid Input'})

from flask import Blueprint, request, jsonify
import message_producer.app.service.email_service as email_service

email_blueprint = Blueprint('email', __name__)


@email_blueprint.route('email', methods=['POST'])
def new_email():
    email = request.json
    email_service.sorting_emails(email)
    return jsonify("info for new email recived"), 200

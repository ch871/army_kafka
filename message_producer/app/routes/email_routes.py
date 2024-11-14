from flask import Blueprint, request, jsonify
import message_producer.app.service.email_service as email_service
from db.repositories.sentences_repo import get_all_sentences_by_email, find_most_common_word

email_blueprint = Blueprint('email', __name__)


@email_blueprint.route('email', methods=['POST'])
def new_email():
    email = request.json
    email_service.sorting_emails(email)
    return jsonify("info for new email recived"), 200


@email_blueprint.route('email/<email>', methods=['GET'])
def get_by_email(email):
    sentences = get_all_sentences_by_email(email)
    return jsonify(sentences), 200


@email_blueprint.route('email/most_common', methods=['GET'])
def get_by_email():
    most_common = find_most_common_word()
    return jsonify(most_common), 200


most_common

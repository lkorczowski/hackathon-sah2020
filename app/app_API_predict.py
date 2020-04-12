#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
import pickle
from utils.config import Config

"""
curl -i -H "Content-Type: application/json" -X POST -d '{"data":{"id":2,"fk_user_id":12,"uuid":"NaklEVVoaJvhA","status":"incomplete","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","get_responses_answers":[{"id":4,"fk_answer_id":6,"fk_question_id":85,"content":"aaa","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","pivot":{"fk_survey_id":2,"fk_response_answer_id":4},"get_answer":{"id":6,"slug":"free","content":"free","type":"free","created_at":"2020-04-11 21:30:22","updated_at":"2020-04-11 21:30:22","category":null},"get_question":{"id":85,"order":1,"description":"Comment sont survenus vos acouph\u00e8nes ?","uuid":"gHDb7kcC6w7ERNR1vWaO3fAcyywkBMnCBTZdIEWN3KyqoPRT0vtHocsVteHGIYjNzNnrNfRuxN5TFw58om8WOCf0MWWveNXNgoJlU30u1wjR1RDb06GueC15ZkR","slug":"comment-sont-survenus-vos-acouphenes","active":"1","type":"free","created_at":"2020-04-11 21:32:09","updated_at":"2020-04-11 21:32:09"}},{"id":5,"fk_answer_id":6,"fk_question_id":86,"content":"aaa","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","pivot":{"fk_survey_id":2,"fk_response_answer_id":5},"get_answer":{"id":6,"slug":"free","content":"free","type":"free","created_at":"2020-04-11 21:30:22","updated_at":"2020-04-11 21:30:22","category":null},"get_question":{"id":86,"order":2,"description":"Avez-vous des ant\u00e9c\u00e9dents m\u00e9dicaux \/ des conditions m\u00e9dicales que vous pensez \u00eatre cause de vos acouph\u00e8nes ou en lien eux ?","uuid":"OETYezp0bmiqxg2f5K7r058ejccyzwLKAC2TiWjBxRupposPUGjZGIjCok3D4aMcFn3Z8koIqQv7TMPrd1mLQwrIQHclVw4FOaLztgVZVqCOfSY28pC7Xnr3UQc","slug":"avez-vous-des-antecedents-medicaux-des-conditions-medicales-que-vous-pensez-etre-cause-de-vos-acouphenes-ou-en-lien-eux","active":"1","type":"free","created_at":"2020-04-11 21:32:09","updated_at":"2020-04-11 21:32:09"}},{"id":6,"fk_answer_id":6,"fk_question_id":87,"content":"aaaa","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","pivot":{"fk_survey_id":2,"fk_response_answer_id":6},"get_answer":{"id":6,"slug":"free","content":"free","type":"free","created_at":"2020-04-11 21:30:22","updated_at":"2020-04-11 21:30:22","category":null},"get_question":{"id":87,"order":3,"description":"D\u00e9crivez en quelques phrases vos acouph\u00e8nes, que percevez - vous ?","uuid":"2nkITXSLrdcFXzshwC5DG955YNitPYDsDsV0lQFyZ0I3SMLFBNsNgU9NJNNuZzsXgMfcOT8kXmjHAgDWbNw1NI8GlcG41GmEF4f1VAoW9cbYqwupmdeZM4cSZVk","slug":"decrivez-en-quelques-phrases-vos-acouphenes-que-percevez-vous","active":"1","type":"free","created_at":"2020-04-11 21:32:09","updated_at":"2020-04-11 21:32:09"}},{"id":7,"fk_answer_id":6,"fk_question_id":88,"content":"aaaa","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","pivot":{"fk_survey_id":2,"fk_response_answer_id":7},"get_answer":{"id":6,"slug":"free","content":"free","type":"free","created_at":"2020-04-11 21:30:22","updated_at":"2020-04-11 21:30:22","category":null},"get_question":{"id":88,"order":4,"description":"En quoi vos acouph\u00e8nes vous d\u00e9rangent ?","uuid":"Ym5lug4DW4m6afFwMH688lENVfwL4U4OsGZshzv3VGMM6rucC3qTrrLrWkUusRH1kpSn4G2XlPoAhBRCe10ARww6KbvZ7HW6bl0xpS3XYZs21ReF9x2UYpQc1Rx","slug":"en-quoi-vos-acouphenes-vous-derangent","active":"1","type":"free","created_at":"2020-04-11 21:32:09","updated_at":"2020-04-11 21:32:09"}}]}}' http://localhost:5000/predict
"""

app = Flask(__name__)

lda_tf = pickle.load(open('../data/lda_tf.pk', "rb"))
tf_vectorizer = pickle.load(open('../data/tf_vectorizer.pk', "rb"))


def predict(sentence):
    new_vector = tf_vectorizer.transform([sentence])
    return lda_tf.transform(new_vector)


def contactenate_sentences(json_var):
    sentence = ""
    for data in json_var["data"]["get_responses_answers"]:
         sentence += data["content"] + '. '
    return sentence


requests = [
    {"data": {"id":2,"fk_user_id":12,"uuid":"NaklEVVoaJvhA","status":"incomplete","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","get_responses_answers":[{"id":4,"fk_answer_id":6,"fk_question_id":85,"content":"aaa","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","pivot":{"fk_survey_id":2,"fk_response_answer_id":4},"get_answer":{"id":6,"slug":"free","content":"free","type":"free","created_at":"2020-04-11 21:30:22","updated_at":"2020-04-11 21:30:22","category":None},"get_question":{"id":85,"order":1,"description":"Comment sont survenus vos acouph\u00e8nes ?","uuid":"gHDb7kcC6w7ERNR1vWaO3fAcyywkBMnCBTZdIEWN3KyqoPRT0vtHocsVteHGIYjNzNnrNfRuxN5TFw58om8WOCf0MWWveNXNgoJlU30u1wjR1RDb06GueC15ZkR","slug":"comment-sont-survenus-vos-acouphenes","active":"1","type":"free","created_at":"2020-04-11 21:32:09","updated_at":"2020-04-11 21:32:09"}},{"id":5,"fk_answer_id":6,"fk_question_id":86,"content":"aaa","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","pivot":{"fk_survey_id":2,"fk_response_answer_id":5},"get_answer":{"id":6,"slug":"free","content":"free","type":"free","created_at":"2020-04-11 21:30:22","updated_at":"2020-04-11 21:30:22","category":None},"get_question":{"id":86,"order":2,"description":"Avez-vous des ant\u00e9c\u00e9dents m\u00e9dicaux \/ des conditions m\u00e9dicales que vous pensez \u00eatre cause de vos acouph\u00e8nes ou en lien eux ?","uuid":"OETYezp0bmiqxg2f5K7r058ejccyzwLKAC2TiWjBxRupposPUGjZGIjCok3D4aMcFn3Z8koIqQv7TMPrd1mLQwrIQHclVw4FOaLztgVZVqCOfSY28pC7Xnr3UQc","slug":"avez-vous-des-antecedents-medicaux-des-conditions-medicales-que-vous-pensez-etre-cause-de-vos-acouphenes-ou-en-lien-eux","active":"1","type":"free","created_at":"2020-04-11 21:32:09","updated_at":"2020-04-11 21:32:09"}},{"id":6,"fk_answer_id":6,"fk_question_id":87,"content":"aaaa","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","pivot":{"fk_survey_id":2,"fk_response_answer_id":6},"get_answer":{"id":6,"slug":"free","content":"free","type":"free","created_at":"2020-04-11 21:30:22","updated_at":"2020-04-11 21:30:22","category":None},"get_question":{"id":87,"order":3,"description":"D\u00e9crivez en quelques phrases vos acouph\u00e8nes, que percevez - vous ?","uuid":"2nkITXSLrdcFXzshwC5DG955YNitPYDsDsV0lQFyZ0I3SMLFBNsNgU9NJNNuZzsXgMfcOT8kXmjHAgDWbNw1NI8GlcG41GmEF4f1VAoW9cbYqwupmdeZM4cSZVk","slug":"decrivez-en-quelques-phrases-vos-acouphenes-que-percevez-vous","active":"1","type":"free","created_at":"2020-04-11 21:32:09","updated_at":"2020-04-11 21:32:09"}},{"id":7,"fk_answer_id":6,"fk_question_id":88,"content":"aaaa","created_at":"2020-04-11 21:33:07","updated_at":"2020-04-11 21:33:07","pivot":{"fk_survey_id":2,"fk_response_answer_id":7},"get_answer":{"id":6,"slug":"free","content":"free","type":"free","created_at":"2020-04-11 21:30:22","updated_at":"2020-04-11 21:30:22","category":None},"get_question":{"id":88,"order":4,"description":"En quoi vos acouph\u00e8nes vous d\u00e9rangent ?","uuid":"Ym5lug4DW4m6afFwMH688lENVfwL4U4OsGZshzv3VGMM6rucC3qTrrLrWkUusRH1kpSn4G2XlPoAhBRCe10ARww6KbvZ7HW6bl0xpS3XYZs21ReF9x2UYpQc1Rx","slug":"en-quoi-vos-acouphenes-vous-derangent","active":"1","type":"free","created_at":"2020-04-11 21:32:09","updated_at":"2020-04-11 21:32:09"}}]}}
]

preditions = [
    {
        'id': 0,
        'fk_user_id': 0,
        'uuid': "",
        'probabilities': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        'description': Config.dict_motsclefs,
        "status": "complete"
    }
]

@app.route('/predict/<int:prediction_id>', methods=['GET'])
def get_task(prediction_id):
    prediction = [prediction for prediction in preditions if prediction['id'] == prediction_id]
    if len(prediction) == 0:
        abort(404)
    return jsonify({'prediction': prediction[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/predict', methods=['POST'])
def return_prediction():
    if not request.json or not 'data' in request.json:
        abort(400)
    sentences = contactenate_sentences(request.json)
    predition = {
        'id': request.json['data']["id"],
        'fk_user_id': request.json['data']["fk_user_id"],
        'uuid': request.json['data']["uuid"],
        'sentences': sentences,
        'probabilities': predict(sentences).tolist(),
        'description': Config.dict_categories,
        "status": "complete"
    }
    preditions.append(predition)
    return jsonify({'prediction': predition}), 201


if __name__ == '__main__':
    app.run(debug=True)

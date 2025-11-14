from flask import Flask, request, jsonify
import random
import os
import firebase_admin
from firebase_admin import firestore, credentials
import json

app = Flask(__name__)

# Firebase
cred_dict = json.loads(os.getenv('FIREBASE_SERVICE_ACCOUNT'))
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/gerar_palpites')
def gerar():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'unauthorized'}), 401
    nums = sorted(random.sample(range(1, 26), 15))
    return jsonify({'palpites': [nums]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

from flask import Flask, render_template, request, jsonify
from google_auth_oauthlib.flow import Flow
import services

class values():
    token = ""

app = Flask(__name__)

appflow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['openid', 'https://www.googleapis.com/auth/dialogflow',
            'https://www.googleapis.com/auth/cloud-platform'],
    redirect_uri= 'http://localhost:5000/chatbot')


@app.route('/')
def Home():
    
    auth_uri = appflow.authorization_url()
    print(auth_uri)

    if request.is_json:
        return auth_uri #jsonify({'code': auth_uri})

    return render_template("index.html")


@app.route('/chatbot')
def Chatbot():

    code = request.args.get('code')
    print(code)
    appflow.fetch_token(code=code)
    credentials = appflow.credentials
    values.token = credentials.token
    
    res = services.Chat('oi', values.token)
    
    return render_template("pedido.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
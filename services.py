'''
Responsável por montar e enviar a requisição a API. 

<> Chat(<string> txt, <string>credencial)
<string> txt: Entrada do usuário 
<string> credencial: Credencial do Google OAuth
'''

import requests
import json

def Chat(txt, credencial):

    payload = payload = {
        "queryParams": {
            "source": "DIALOGFLOW_CONSOLE",
            "timeZone": "America/Fortaleza",
            "sentimentAnalysisRequestConfig": {
                "analyzeQueryTextSentiment": True
            }
        },
        "queryInput": {
            "text": {"text": txt, "languageCode": "pt-br"}
        }
    }

    headers = {
        'accept': 'application/json text/plain, */*',
        'content-type': 'application/json; charset=UTF-8',
        'authorization': 'Bearer ' + credencial
    }



    ### Talvez aqui dê problema pq nao lembro se troquei o link de requisicao p o novo bot!!
    res = requests.post("https://dialogflow.clients6.google.com/v2/projects/newagent-dprt/locations/global/agent/sessions/31ac21cc-7e7c-1557-cf1e-157789db166e:detectIntent", headers=headers, json=payload)
    if(res.status_code == 200):
        resp = json.loads(res.text)
        resp_message = resp['queryResult']['fulfillmentMessages']
 
        if len(resp_message) > 1:
            c = 0
            re = []
            for i in resp_message:
                contagem = resp_message[c]['text']['text'][0]
                re.append(contagem)
                c += 1
        else:
            re = contagem = resp_message[0]['text']['text'][0]
        
        return re
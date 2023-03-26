from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

class TelegramBot:          # comunica a chave no acesso do env#
    def __init__(self):
        TOKEN = os.getenv("API_KEY")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"  #acessa o bot por aqui#

    def start(self):        # Inicia o bot e o mantém funcionando a espera de novas request/mensagens#
        update_id = None
        while True: 
           update = self.get_message(update_id)
           messages = update['result']
           if messages: 
                for message in messages:
                    try:
                        update_id = message['update_id'] #identifica a mensagem#
                        chat_id = message['message']['from']['id'] #identifica quem mandou a mensagem#
                        message_text = message['message']['text']
                        answer_bot = self.create_answer(message_text)
                        self.send_answer(chat_id, answer_bot)
                    except:
                        pass # Se der problema, passa para proxima iteração#

    def get_message(self, update_id):  # Recebe o texto e o trata como dicionario json#
        link_request = f"{self.url}getUpdates?timeout=120"
        if update_id:
            link_request = f"{self.url}getUpdates?timeout=120&offset={update_id + 1}"
        result = requests.get(link_request)
        return json.loads(result.content)

    def create_answer(self, message_text):  #cria os textos que serão enviados#
        if message_text in ["oi", "ola", "salve", "boa noite"]:
            return "Ola laurinha meu bebe, tinhamu S2"
        else:
            return "Não entendi porque meu bb não me deu um boa noite ainda :("

    def send_answer(self, chat_id, answer): #envia os textos criados#
        link_to_send = f"{self.url}sendMessage?chat_id={chat_id}&text={answer}" #envia uma determinada mensagem via determinada id de usuário#
        requests.get(link_to_send)
        return
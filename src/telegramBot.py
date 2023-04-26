from dotenv import load_dotenv
import os
import requests
import json
from src.data.driveBot import driveBot
from src.data.transform_dataframe import transform_data
from src.visualization.visualize import barv_npsmean_by, barv_npsmean_by_contract, hist_nps, mean_age, mean_salary, colab_sector, contracts
from PIL import Image


load_dotenv()

class TelegramBot():
    def __init__(self):
        TOKEN = os.getenv("API_KEY")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"
        self.driveBot = driveBot()

    def start(self):
        print("Inicializando bot...")
        update_id = None
        while True:
            update = self.get_message(update_id)
            messages = update['result']
            if messages:
                for message in messages:
                    try:
                        update_id = message['update_id']
                        chat_id = message['message']['from']['id']
                        message_text = message['message']['text']
                        answer_bot, figure_boolean = self.create_answer(message_text)
                        self.send_answer(chat_id, answer_bot, figure_boolean)
                    except:
                        pass

    def get_message(self, update_id):
        link_request = f"{self.url}getUpdates?timeout=1000"
        if update_id:
            link_request = f"{self.url}getUpdates?timeout=1000&offset={update_id + 1}"
        result = requests.get(link_request)
        return json.loads(result.content)
    
    def create_answer(self, message_text):
        dataframe = transform_data(self.driveBot.get_data())
        message_text = message_text.lower()
        if message_text in ["/start", "ola", "eae", "menu", "oi", "oie"]:
            return "Olá, Saudações! Seja bem vindo ao Bot da turma 001 do Projeto Integrador IV do polo Assis - SP. Selecione o que deseja:" + "\n" + "\n" + "1 - NPS interno mensal médio por setor" + "\n" + "2 - NPS interno mensal médio por contratação" + "\n" + "3 - Distribuição do NPS interno" + "\n" + "4 - Média das idades por setor" + "\n" + "5 - Média salarial de dos setores" + "\n" + "6 - Quantidade de colaboradores" + "\n" + "7 - Percentual de contratos" + "\n", 0
        elif message_text == '1':
            return barv_npsmean_by(dataframe, "Setor"), 1
        elif message_text == '2':
            return barv_npsmean_by_contract(dataframe, "Tipo de Contratação"), 1
        elif message_text == '3':
            return hist_nps(dataframe), 1
        elif message_text == '4':
            return mean_age(dataframe), 1
        elif message_text == '5':
            return mean_salary(dataframe), 1
        elif message_text == '6':
            return colab_sector(dataframe), 1
        elif message_text == '7':
            return contracts(dataframe), 1
        else:
            return "Comando não encontrado, tente novamente. Por favor selecione alguma funcionalidade disponível:" + "\n" + "\n" + "1 - NPS interno mensal médio por setor" + "\n" + "2 - NPS interno mensal médio por contratação" + "\n" + "3 - Distribuição do NPS interno" + "\n" + "4 - Média das idades por setor" + "\n" + "5 - Média salarial de dos setores" + "\n" + "6 - Quantidade de colaboradores" + "\n" + "7 - Percentual de contratos" + "\n", 0
    
    def send_answer(self, chat_id, answer, figure_boolean):
        if figure_boolean == 0:
            link_to_send = f"{self.url}sendMessage?chat_id={chat_id}&text={answer}"
            requests.get(link_to_send)
            return
        else:
            answer.seek(0)
            requests.post(f"{self.url}sendPhoto?chat_id={chat_id}", files = dict(photo=answer))
            answer.close()
            return
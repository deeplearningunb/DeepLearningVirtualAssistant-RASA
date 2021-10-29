# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from os import name
from typing import Any, Text, Dict, List


from pathlib import Path
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Eu irei lembrar seu nome {text}!")

        return [SlotSet("user_name", text)]


class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        username = tracker.get_slot("user_name")
        if not username:
            dispatcher.utter_message(text=f"Eu não sei seu nome. :(")
        else:
            dispatcher.utter_message(
                text=f"Seu nome, {username}!")
        return []

# class ActionAskName(Action):

#     def name(self) -> Text:
#         return "action_facility_search"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         facility = tracker.get.slot("facility_type")
#         estado = "Goias"
#         dispatcher.utter_message(
#             "Aqui é a sua localidade {}.{}".format(facility, estado))

#         return [SlotSet("estado", estado)]


# class ActionAskName(Action):
#     knowledge = Path("data/content.txt").read_text().split("/n")

#     def name(self) -> Text:
#         return "action_definition"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         for blob in tracker.latest_message['entities']:
#             print(tracker.latest_message)
#             if blob['entity'] == 'content_name':
#                 name = blob['value']
#                 if name in self.knowledge:
#                     dispatcher.utter_message(text=f"Sim, eu sei sobre {name}")
#                 else:
#                     dispatcher.utter_message(
#                         text=f"Eu não sei sobre {name}, desculpe.")

#         return []

class ActionReceiveContent(Action):

    def name(self) -> Text:
        return "action_receive_content"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Eu irei falar sobre {text}!")

        return [SlotSet("content_name", text)]


class ActionContentDefinition(Action):

    def name(self) -> Text:
        return "action_content_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        content = tracker.get_slot("content_name")
        if not content:
            dispatcher.utter_message(
                text=f"Eu não sei qual conteúdo você quer que eu ensine")
        else:
            contentlow = content.lower()
            if contentlow == "ann":
                dispatcher.utter_message(
                    text=f"{content} significa artificial neural network, traduzido para português como rede neural artificial. A rede neural artificial é uma rede artificial que utiliza uma série de neurônios para aprender, sendo este um sistema de hardware e/ou software padronizado após a operação de neurônios no cérebro humano.!")
            elif contentlow == "cnn":
                dispatcher.utter_message(
                    text=f"{content} significa Convolutional Neural Network, traduzido para português como rede neural convolucional. Uma Rede Neural Convolucional (ConvNet / Convolutional Neural Network / CNN) é um algoritmo de Aprendizado Profundo que pode captar uma imagem de entrada, atribuir importância (pesos e vieses que podem ser aprendidos) a vários aspectos / objetos da imagem e ser capaz de diferenciar um do outro. O pré-processamento exigido em uma ConvNet é muito menor em comparação com outros algoritmos de classificação. Enquanto nos métodos primitivos os filtros são feitos à mão, com treinamento suficiente, as ConvNets têm a capacidade de aprender esses filtros / características.")
            elif contentlow == "rnn":
                dispatcher.utter_message(
                    text=f"{content} significa recurrent neural network, trauduzido para português como rede neural recorrente. Uma Rede Neural Recorrente (RNN) é um algoritmo de Aprendizado Profundo que pode captar uma sequência de dados e ser capaz de aprender a reconhecer essa sequência. As conexões entre os nós formam um grafo direcionado ao longo de uma sequência temporal. Isso permite que ele exiba um comportamento dinâmico temporal. Derivado de redes neurais feedforward, os RNNs podem usar seu estado interno (memória) para processar sequências de entradas de comprimento variável.")
            elif contentlow == "sae":
                dispatcher.utter_message(
                    text=f"{content} significa 'Sequential Autoencoder', ou seja, uma rede autoencoder sequencial. A rede autoencoder sequencial é uma rede neural que aprende a reconhecer uma sequência de dados, usando um processo de treinamento de recursos de aprendizagem não supervisionados por cada camada, o que resulta em uma precisão de previsão consideravelmente melhorada do modelo de calibração.")
            elif contentlow == "som":
                dispatcher.utter_message(
                    text=f"{content} signfica Self Organizing Map, traduzindo para português temos Mapa Auto Organizável, esta é uma rede neural que aprende a reconhecer um mapa de dados, usando um processo de treinamento de recursos de aprendizagem não supervisionados por cada camada, o que resulta em uma precisão de previsão consideravelmente melhorada do modelo de calibração.")

        return []


# class ActionCheckKnowledge(Action):
#     knowledge = Path("data/content.txt").read_text().split("/n")

#     def name(self) -> Text:
#         return "action_check_knowledge"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         for blob in tracker.latest_message['entities']:
#             print(tracker.latest_message)
#             name = blob['value']
#             if name in self.knowledge:
#                 dispatcher.utter_message(text=f"Sim, eu sei {name}.")
#             else:
#                 dispatcher.utter_message(
#                     text=f"Eu não sei {name}, desulpe.")
#         return[]

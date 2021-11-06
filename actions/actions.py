# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
from os import name
from typing import Any, Text, Dict, List


from pathlib import Path
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Import para o json
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

from rasa_sdk.events import SlotSet

import json

with open('data/contentdb.json', 'r') as f:
    data = json.load(f)

print(data['content'][0]['name'])
1
2
3


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phrase = "Texto de teste para ver se funciona com o utter mensage"
        dispatcher.utter_message(text="Hello world")

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
            count = 0
            while count < 5:
                if data['content'][count]['name'] == contentlow:
                    dispatcher.utter_message(
                        text=data['content'][count]['description'])
                count += 1
        return []


class ActionContentCheck(Action):
    knowledge = Path("data/content.txt").read_text().split(',')

    def name(self) -> Text:
        return "action_check_knowledge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'content_name':
                name = blob['value']
                if name in self.knowledge:
                    dispatcher.utter_message(text=f"Sim, eu sei sobre {name}")
                else:
                    dispatcher.utter_message(
                        text=f"Eu não sei sobre {name}, desculpe.")

        return []


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data/contentdb.json")
        super().__init__(knowledge_base)

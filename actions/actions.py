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


# class ActionAskName(Action):

#     def name(self) -> Text:
#         return "action_facility_search"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         facility = tracker.get.slot("facility_type")
#         estado = "Goias"
#         dispatcher.utter_message(
#             "Aqui � a sua localidade {}.{}".format(facility, estado))

#         return [SlotSet("estado", estado)]

class ActionAskName(Action):
    knowledge = Path("data/content.txt").read_text().split("/n")

    def name(self) -> Text:
        return "action_definition"

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

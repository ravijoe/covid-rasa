# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="sorry for the foul language :( !")

        return []


class ActionSearchRestaurant(Action):

    def name(self) -> Text:
        return "action_search_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities=tracker.latest_message['entities']
        print(entities)
        message=None
        for e in entities:
            if e['entity']=='hotel':
                name=e['value']
            if name=='indian':
                message='indian1,indian2,indian3'
            if name=='chinese':
                message='chini.....'
            if name=='that':
                message='ong bak'
            # else:
            #     message='pata nahi bhai'

        dispatcher.utter_message(text=message)

        return []
import requests
class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response=requests.get("https://api.covid19india.org/data.json").json()
        entities=tracker.latest_message['entities']
        state=None
        message=''
        for e in entities:
            if e['entity']=='state':
                state=e['value']
        for data in response['statewise']:
            if data['state'].lower()==state.lower():
            # print(data['state'])
            # print(state)
                message='Active: '+data['active']+' Confirmed: '+data['confirmed']+' Deaths: '+data['deaths']
                print(message)

        dispatcher.utter_message(text=message)

        return []
































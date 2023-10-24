from typing import List
import datetime
import logging

import azure.functions as func

#def main(events: List[func.EventHubEvent]):
#        for event in events:
#             logging.info('Python EventHub trigger processed an event: %s',
#                         event.get_body().decode('utf-8'))

def main(events: List[func.EventHubEvent], outputEvent: func.Out[str]):
     for event in events:
         event_data = event.get_body().decode('utf-8')
         logging.info('Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))
         outputEvent.set(event_data)
     




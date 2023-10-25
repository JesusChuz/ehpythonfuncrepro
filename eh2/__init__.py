from typing import List
import datetime
import logging

import azure.functions as func


def main(events2: List[func.EventHubEvent]):
        for event in events2:
             logging.info('Python EventHub trigger processed an event: %s',
                         event.get_body().decode('utf-8'))

#def main(events2: List[func.EventHubEvent], outputEvent2: func.Out[str]):

#     for event in events2:
#         event_data = event.get_body().decode('utf-8')
#         logging.info('Python EventHub trigger processed an event: %s',
#                        event.get_body().decode('utf-8'))
#         outputEvent2.set(event_data)
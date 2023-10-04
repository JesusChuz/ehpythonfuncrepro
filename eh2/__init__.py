from typing import List
import logging

import azure.functions as func


def main(events2: List[func.EventHubEvent]):
     for event in events2:
         logging.info('Python EventHub trigger processed an event: %s',
                         event.get_body().decode('utf-8'))

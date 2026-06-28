import json
import logging
import azure.functions as func

from function_app import app

@app.function_name(name="eventHubTrigger")
@app.event_hub_message_trigger(arg_name="event",
                               event_hub_name="testhub",
                               connection="EventHubConnectionAppSetting")
def main(event: func.EventHubEvent):
    logging.info('Function triggered to process a message: %s', event.get_body().decode('utf-8'))
    logging.info('  EnqueuedTimeUtc = %s', event.enqueued_time)
    logging.info('  SequenceNumber = %s', event.sequence_number)
    logging.info('  Offset = %s', event.offset)

    result = json.dumps({
        'body': event.get_body().decode('utf-8'),
        'enqueued_time': str(event.enqueued_time),
        'sequence_number': event.sequence_number,
        'offset': event.offset,
    })

    logging.info('Python EventHub trigger processed an event: %s', result)




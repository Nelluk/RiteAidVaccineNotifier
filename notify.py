import requests
import json
import time
import pync
from pushsafer import Client, init
import logging
import datetime
import config

init(config.pushsafer_api_key)
client = Client('')
logging.captureWarnings(True)  # Supress SSL warning
last_push_notification = datetime.datetime.min


def send_push(title: str = 'Nearby RiteAid has shots', message: str = 'Vaccine Alert'):
    if not config.notify_via_pushsafer or not config.pushsafer_api_key:
        return

    global last_push_notification

    if (last_push_notification + datetime.timedelta(hours=1)) > datetime.datetime.now():
        print('Skipping push notification due to last_push_notification')
        return

    last_push_notification = datetime.datetime.now()

    client.send_message(message,
                        title,
                        "a",  # device or group. 'a' = all devices on account
                        "1",  # icon
                        "4",  # sound
                        "2",  # vibration
                        "https://www.riteaid.com/pharmacy/covid-qualifier",  # url
                        "Open RiteAid.com",  # urltitle
                        "0",  # time2live
                        "1",  # priority
                        None,  # retry
                        None,  # expire
                        "0",  # answer
                        "",  # picture1
                        "",  # picture2
                        "")  # picture3


while True:

    print(f'New loop with stores {config.close_stores + config.far_stores}')

    for store in config.close_stores + config.far_stores:

        time.sleep(3)
        url = "https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber=" + store
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Content-Type': 'application/json'}

        try:
            result = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError as e:
            print(f'CONNECTION ERROR ERROR: {e}')
            continue

        try:
            output = result.json()
        except json.JSONDecodeError:
            print(f'JSON PARSE ERROR for output {output}')
            continue

        print(output)

        if output and output['Data'] and output['Data']['slots'] and output['Data']['slots']['1']:
            if store in config.close_stores:
                if config.notify_via_macos:
                    pync.notify('❗ ' + store + ' Has Shots', title='RITE AID', open='https://www.riteaid.com/pharmacy/covid-qualifier')

                send_push()
                print(f'Close store {store} has shots')
                time.sleep(60)
            else:
                if config.notify_via_macos:
                    pync.notify(store + ' Has Shots', title='RITE AID', open='https://www.riteaid.com/pharmacy/covid-qualifier')
                print(f'Far store {store} has shots')
                break  # abandon rest of list if found shot in a far-away store
        else:
            print(f'No shots at store {store}')

    time.sleep(20)

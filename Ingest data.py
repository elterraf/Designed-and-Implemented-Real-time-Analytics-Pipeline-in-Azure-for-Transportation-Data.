import time
import json
from csv import reader
from azure.eventhub import EventHubProducerClient, EventData

connection_str = 'Endpoint=sb://transportation-data-eventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=zu4Gf00lj1eYZMGn1hkDqIIK/X9slbOmN4a0cYmvEYE='
eventhub_name = 'transport-stream'

class Transport:   
    def __init__(self, reportyear, race_eth_code, race_eth_name, geoname, mode, mode_name, pop_total, pop_mode):
        self.reportyear = reportyear
        self.race_eth_code = race_eth_code
        self.race_eth_name = race_eth_name
        self.geoname = geoname
        self.mode = mode
        self.mode_name = mode_name
        self.pop_total = pop_total
        self.pop_mode = pop_mode
    def __str__(self):
        return f"{self.reportyear}, {self.race_eth_code}, {self.race_eth_name}, {self.geoname}, {self.mode}, {self.mode_name}, {self.pop_total}, {self.pop_mode}"

def send_to_eventhub(client, data):
    event_data_batch = client.create_batch()
    event_data_batch.add(EventData(data))
    client.send_batch(event_data_batch)

def main():
    with open(r'C:\Users\Hinnovis\OneDrive\Bureau\CV_PROJECT\Azure project\Data\Data\transportation.csv', 'r') as transport_desc:
        csv_reader = reader(transport_desc)
        header = next(transport_desc)

        client = EventHubProducerClient.from_connection_string\
                 (connection_str, eventhub_name=eventhub_name)
        for row in csv_reader:
            reportyear1 = row[0]
            race_eth_code1 = row[1]
            race_eth_name1 = row[2]
            geoname1 = row[3]
            mode1 = row[4]
            mode_name1 = row[5]
            pop_total1 = row[6]
            pop_mode1 = row[7]

            weather = Transport(reportyear1, race_eth_code1, race_eth_name1, geoname1, mode1, mode_name1, pop_total1, pop_mode1)
            send_to_eventhub(client, json.dumps(weather.__dict__))
            print(json.dumps(weather.__dict__))

main()











# countries = header[:-1].split(',')[1:]
# connection_str = 'Endpoint=sb://weather-data-eventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=AXgSPNVwK+ZGB8wdK5tdF1bNsduLFgSsGRd4bsJiT2I='
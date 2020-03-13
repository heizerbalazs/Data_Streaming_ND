from kafka import KafkaConsumer
import json

def binary_to_dict(self, binary_stream):
        return json.loads(binary_stream.decode("utf-8"))

if __name__ == "__main__":
    
    consumer = KafkaConsumer(
        "com.udacity.sf.crime.calls",
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest"
    )
    
    for message in consumer:
        print(*[f"key={message.key}", f"value={message.value}"],sep="\n")
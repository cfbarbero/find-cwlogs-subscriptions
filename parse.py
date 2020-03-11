import json
import argparse

parser = argparse.ArgumentParser(description='Parse the subscriptions')
parser.add_argument('filename', type=str, help='an integer for the accumulator')

args = parser.parse_args()

with open(args.filename, 'r') as f:
    data = json.load(f)


subscriptions={}
for item in data:
    for subscription in item['subscription_filters']:
        if subscription not in subscriptions:
            subscriptions[subscription]=[]
        subscriptions[subscription].append(item['log_group'])

print(json.dumps(subscriptions, indent=2))
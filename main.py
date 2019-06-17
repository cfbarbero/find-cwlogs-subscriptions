import argparse
import boto3
import json

client = boto3.client('logs')
subscriptions = []

paginator = client.get_paginator('describe_log_groups')
page_iterator = paginator.paginate(
    PaginationConfig={
    })

for page in page_iterator:

    for loggroup in page['logGroups']:
        print('.', end='', flush=True)
        name = loggroup['logGroupName']
        subscription_response = client.describe_subscription_filters(
            logGroupName=name,
        )
        if subscription_response['subscriptionFilters']:
            subscriptions.append({'log_group': name, 'subscription_filters': [
                [f['destinationArn'] for f in subscription_response['subscriptionFilters']]
            ]})

print(json.dumps(subscriptions, indent=2))


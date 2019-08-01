#!/usr/bin/env python3

import boto3
import datetime
import pprint
from configuration import Config

def get_month_costs():

        now = datetime.datetime.utcnow()
        start = ('2019-07-01')
        end = now.strftime('%Y-%m-%d')

        client = boto3.client(
                    'ce',
                    aws_access_key_id=Config.ACCESS_KEY,
                    aws_secret_access_key=Config.SECRET_KEY,
                    region_name=Config.EC2_REGION
                )

        results = []

        token = None
        while True:
            if token:
                kwargs = {'NextPageToken': token}
            else:
                kwargs = {}

            response = client.get_cost_and_usage(
                TimePeriod={
                    'Start': start,
                    'End': end
                },
                Filter={
                    'Dimensions': {
                        'Key': 'SERVICE',
                        'Values': [
                            'Amazon Elastic Compute Cloud - Compute'
                        ]
                    }
                },
                Granularity='MONTHLY',
                Metrics=['UnblendedCost'],
                GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}],
                **kwargs
            )
            results += response['ResultsByTime']
            token = response.get('NextPageToken')
            if not token:
                break

        pprint.pprint(results)

        finaldict = {}
        for monthData in results:
            month = monthData['TimePeriod']['Start'][:-3]
            total = '$' + monthData['Groups'][0]['Metrics']['UnblendedCost']['Amount'][:4]

            finaldict[month] = total

        return finaldict

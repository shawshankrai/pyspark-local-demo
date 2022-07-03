import boto3
import os
from botocore.exceptions import ClientError

os.environ.setdefault("AWS_Profile", "shashank-iam")
os.environ.setdefault("AWS_DEFAULT_REGION", "us-east-1")
glue_client = boto3.client('glue')


def glue_start_crawler():
    try:
        glue_client.start_crawler(
            Name='Retail Crawler'
        )

        crawler_status = glue_client.get_crawler(
            Name='Retail Crawler'
        )['Crawler']['State']

        return crawler_status
    except ClientError as e:
        raise Exception("boto3 client error in list_of_crawlers: " + e.__str__())
    except Exception as e:
        raise Exception("Unexpected error in list_of_crawlers: " + e.__str__())


def glue_get_databases():
    return [db['Name'] for db in glue_client.get_databases()['DatabaseList']]


def glue_get_tables():
    return [table['Name'] for table in glue_client.get_tables(
        DatabaseName='retail_db'
    )['TableList']]


def glue_get_table():
    return glue_client.get_table(
        DatabaseName='retail_db',
        Name='orders'
    )['Table']

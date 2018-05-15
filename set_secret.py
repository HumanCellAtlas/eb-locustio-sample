import boto3
import os

from botocore.exceptions import ClientError
import logging


secret_name = f"{os.environ['DSS_SECRETS_STORE']}/{os.environ['DSS_DEPLOYMENT_STAGE']}/gcp-credentials.json"
endpoint_url = f"https://secretsmanager.{os.environ['AWS_DEFAULT_REGION']}.amazonaws.com"
region_name = os.environ['AWS_DEFAULT_REGION']

session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name,
    endpoint_url=endpoint_url
)

try:
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        logging.error("The requested secret " + secret_name + " was not found")
    elif e.response['Error']['Code'] == 'InvalidRequestException':
        logging.error("The request was invalid due to:", e)
    elif e.response['Error']['Code'] == 'InvalidParameterException':
        logging.error("The request had invalid params:", e)
else:
    secret = get_secret_value_response['SecretString']
    with open(os.environ["GOOGLE_APPLICATION_CREDENTIALS"], 'w') as fp:
        fp.write(secret)
        logging.info("GOOGLE_APPLICATION_CREDENTIALS stored")
import boto3
from datetime import datetime
import logging

from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

s3_client = boto3.client('s3', 
        aws_access_key_id = AWS_ACCESS_KEY_ID, 
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = 'us-east-1')

def create_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('{}_{}.log'.format(logger_name, datetime.now().isoformat().split('.')[0]))
    fh.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)

    return logger

def upload_log(logger):
    file_name = logger.handlers[0].baseFilename
    directory = datetime.now().date().isoformat()
    key = "{}/{}".format(directory, file_name.split('/')[-1])
    # The name of my bucket on S3 is 'crypta-bot-log'
    bucket_name = 'crypta-bot-logs'

    s3_client.upload_file(Filename = file_name, Bucket = bucket_name, Key = key)

def logger(func):
    def function_wrapper(*args, **kwargs):
        function_name = func.__name__
        logger = create_logger(function_name)
        logger.info("Now running - {}".format(function_name))
        
        resp = func(logger = logger, *args, **kwargs)
        upload_log(logger)

        return resp

    return function_wrapper



import os

# Coinbase Credentials
CB_CREDENTIALS = {
    'PASSPHRASE': os.environ['CB_PASSPHRASE'],
    'SECRET': os.environ['CB_SECRET'],
    'KEY': os.environ['CB_KEY'],
    'URL': os.environ['CB_URL']
}

# AWS Credentials
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
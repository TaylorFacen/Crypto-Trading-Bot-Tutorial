import cbpro

from config import CB_CREDENTIALS

def get_client(credentials):
    """Returns the cbpro AuthenticatedClient using the credentials from the parameters dict"""

    cbpro_client = cbpro.AuthenticatedClient(credentials['KEY'], credentials['SECRET'], credentials['PASSPHRASE'], api_url=credentials['URL'])
    return cbpro_client

def cbpro_client(func):
    def function_wrapper(*args, **kwargs):
        cbpro_client = get_client(CB_CREDENTIALS)
        resp = func(cbpro_client = cbpro_client, *args, **kwargs)

        return resp

    return function_wrapper

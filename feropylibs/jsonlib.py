import decimal

def json_encode_decimal(obj):
    """
    [JSON] encode Decimal into json as strings

    This way we can use the `parse_float` parameter of json.loads
    to get the Decimal decoded as before it has been encoded

    Taken from http://stackoverflow.com/a/1960553/720743
    """
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    raise TypeError(repr(obj) + " is not JSON serializable")

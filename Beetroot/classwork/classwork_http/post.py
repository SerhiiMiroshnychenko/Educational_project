import requests  # type: ignore

# defining the api-endpoint
API_ENDPOINT = "https://pastebin.com/api/api_post.php"

# your API key here
API_KEY = "FlBvpNxoEmyJvvotbyyJv4ybC5Bn2YD9"

# your source code here
source_code = '''
import doctest
from typing import Union

def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    """
    Returns  x ^ exp

    >>> to_power(2, 3) == 8
    True

    >>> to_power(3.5, 2) == 12.25
    True

    >>> to_power(2, -1)
    Traceback (most recent call last):
    ValueError: This function works only with exp > 0.
    """
    if exp > 0:
        return x if exp == 1 else x * to_power(x, exp - 1)
    elif exp == 0:
        return 1
    else:
        raise ValueError("This function works only with exp > 0.")


if __name__ == "__main__":
    doctest.testmod()
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    print(to_power(2, 0))
    try:
        print(to_power(2, -1))
    except ValueError as error:
        print(f'ValueError: {error}')
    doctest.testmod()
'''

# data to be sent to api
data = {"api_dev_key": API_KEY,
        "api_option": "paste",
        "api_paste_code": source_code,
        "api_paste_format": "python"
        }

r = requests.post(API_ENDPOINT, data=data)

# extracting response text
pastebin_url = r.text
print(f"The pastebin URL is:{pastebin_url}")

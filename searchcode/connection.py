import json
import urllib.error
import urllib.request
from typing import Union


def __api_handler(endpoint: str) -> Union[dict, list, str]:
    """
    Sends a request to the designated API endpoint and returns the response.
    If the API returns a 429 error code, indicating that the user has sent too many requests in a short period of time,
    the handler will extract the retry-after header value and return it as an integer.

    Parameters:
    -----------
    endpoint (str): A string representing the API endpoint to send a request to.

    Returns:
    --------
    Union[dict, list, str]: If the response is successful, returns the response data as a dictionary, list or string,
        depending on the API endpoint.

    Raises:
    -------
        Exception: If the function was unable to get a valid response after making the request, or if the retry-after
        header is missing in the API response.
    """
    try:
        with urllib.request.urlopen(endpoint) as response:
            if response.status == 429:
                # If the API returns a 429 response, extract the retry-after header value
                retry_after = response.getheader("Retry-After")
                if retry_after:
                    raise Exception(f"Too many requests. Please try again in {retry_after}.")
                else:
                    # Retry-after header not found
                    raise Exception("Too many requests. Retry-after header not found in the response.")
            else:
                api_data = response.read().decode("utf-8")
                return json.loads(api_data)
    except (urllib.error.HTTPError, urllib.error.URLError) as error:
        # Catch and yield any network errors or timeouts
        yield error

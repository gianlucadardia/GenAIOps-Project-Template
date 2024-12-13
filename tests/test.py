import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
    "question": "how can I refill my perspriction?",
    "chat_history": []
}

body = str.encode(json.dumps(data))

url = 'https://ragwithtrace1213gd-ep.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMy8iLCJpYXQiOjE3MzQwODU2MzUsIm5iZiI6MTczNDA4NTYzNSwiZXhwIjoxNzM0MDkwMDY2LCJhY3IiOiIxIiwiYWlvIjoiQWFRQVcvOFlBQUFBTG1TSXhrSmtJVitJam1kMzBkdVJXcHFIcTF1NjZnYWl4TUxlZXVuS0JyZEtIcytxWlp4ZS9BWTZYM2NMdTBua2V4TEs3bGhrVXI4SHExbzM0bkYxeG5EbE5xWTMxZWZPMlV5MU53RGt0ZHovcWFUMHBWa05DN1N0Y0NQS1JrTEM0WklrcjNLWlRoMTBWZUMrN0phWjFVQVJtU0tWQk53dU1sVGU4OUpXN3ZFenRFd2ZGcDBoZndSMGpFaS8rUmxyS2FLRDJyLzE3L2EzQzJDVGppS3ljdz09IiwiYWx0c2VjaWQiOiI1OjoxMDAzMjAwMTA5MTMzMjZGIiwiYW1yIjpbImZpZG8iLCJyc2EiLCJtZmEiXSwiYXBwaWQiOiJjYjJmZjg2My03ZjMwLTRjZWQtYWI4OS1hMDAxOTRiY2Y2ZDkiLCJhcHBpZGFjciI6IjAiLCJkZXZpY2VpZCI6IjgwZDNlZGQxLWM2MDgtNGQwMi04ZDMyLTg2NWRhYTk0YmNiNyIsImVtYWlsIjoiZ2RhcmRpYUBtaWNyb3NvZnQuY29tIiwiZmFtaWx5X25hbWUiOiJEJ0FyZGlhIiwiZ2l2ZW5fbmFtZSI6IkdpYW5sdWNhIiwiZ3JvdXBzIjpbImIxMzA0MDIyLTA4ZTYtNDQ3ZC1iMDk0LTE1MzcwNTk3YzZiNiIsIjA5NTMxYTcyLTJjM2UtNGUwNi1iZTFlLTI1OTZiZDA4ZGNkZCIsImQzNGM0ZWJlLTQ5ODQtNDkwMy1hNjRkLThjMjAyODNkNTE2YiIsImUzMDk2ZGY3LWI2NWMtNGUzMi1hYjFhLTdhMzVkYzY4NGYwYSJdLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMTY3LjIyMC4xOTcuNTgiLCJuYW1lIjoiR2lhbmx1Y2EgRCdBcmRpYSIsIm9pZCI6Ijk4NzJiY2ZiLTE5ODgtNDE4MC05MzBkLWM2MTk2ZTk3M2ZjMiIsInB1aWQiOiIxMDAzMjAwMjNDMUNGRUU2IiwicmgiOiIxLkFVWUFFOEN6RmdEVGpVYXNaSDdhQ0NDMjAxOXZwaGpmMnhkTW5kY1dOSEVxbkw3eEFCVkdBQS4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzaWQiOiI3MTQyMzE1Zi1iYWJkLTRjZTgtOGMyMy1kNDI2ZjUyODRmM2UiLCJzdWIiOiJkUUJDck1xeG1Gdy00LUltLU5HblEzSVFvbXpoUUtBbmNXQWF2R2ZHVkxZIiwidGlkIjoiMTZiM2MwMTMtZDMwMC00NjhkLWFjNjQtN2VkYTA4MjBiNmQzIiwidW5pcXVlX25hbWUiOiJnZGFyZGlhQG1pY3Jvc29mdC5jb20iLCJ1dGkiOiJFXzY0aS1rYU9rS1hRQUgyMW9JM0FBIiwidmVyIjoiMS4wIiwieG1zX2lkcmVsIjoiMSAyNiJ9.RYTZK6CrOwvRxJ_D3AbXNxLOSyVQqEQ5rwdrF-N-bD2yDaqAHF9gv1oPQjiJLOvqhcG70WfGHMUAb7JE0mwNXIodkw4eh0e91akXnwyD-OqYihhDoXu5Q_ZdtmnlZBCFFo7WpcxtirtoFW-F9UxzflyarwrHud87DfqCuWbjSv2zQrKpAPw4epbdpaPXKxCQK0oKwb5P_QtKJiob0fqEUHkk78rlYA8nIANlrGlQyXkQZvOsSd9a9STfpmrvzFB6KJDpgC7K3gShc4NhjeKg1qbJwgf8S2INfhEd9Wbvh_kN7MN6FWE3pfQEkGpJTN98sZyFE-qFPEXLtI9RRRlFKA'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
# Mailer

A client to send emails to multiple directions programatically using Python

## Execution

To execute the script, just run the following:

```python
python3 main.py
```

## Setup

- Go into [this link](https://developers.google.com/gmail/api/quickstart/python) and click the button that reads "ENABLE THE GMAIL API", making sure to enter with the gmail account from which all the mails will be sent (this will create a project inside your google console, you want to remember the name. You can also change its name to your convenience).
- Click the button that reads "DOWNLOAD CLIENT CONFIGURATION" and move the downloaded file to the root of this repository. Make sure that the file is named _client\_secret.json_.
- Inside the file _parameters.py_, replace the content of the variable **MAIL_SENDER** with the name of the gmail account from which all the mails will be sent.
- Run the following command:
  ```python
    python3 setup.py
  ```
- If that mail is being used for the first time, a browser will open asking for permission to use extraordinary data from that Google Account. Agree to everything. It is possible that the browser blocks the connection thinking that it is fraudulent, in which case the browser should be gracefully ingnored.
- If that mail had already been used, no browser will open. Either way, a mail will be sent to the account by itself.

## Used Libraries

- os
- re
- pip
- sys
- json
- requests
- base64
- email
- googleapiclient
- httplib2
- oauth2client
- flask

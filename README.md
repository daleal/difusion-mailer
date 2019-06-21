# Mailer

A client to send emails to multiple directions programatically using Python

## Setup

- Go into [this link](https://developers.google.com/gmail/api/quickstart/python) and click the button that reads "ENABLE THE GMAIL API", making sure to enter with the gmail account from which all the mails will be sent (this will create a project inside your google console, you want to remember the name. You can also change its name to your convenience).
- Click the button that reads "DOWNLOAD CLIENT CONFIGURATION" and move the downloaded file to the root of this repository. Make sure that the file is named _client\_secret.json_.
- Inside the file _parameters.py_, replace the content of the variable **MAIL_SENDER** with the name of the gmail account from which all the mails will be sent and comment the last 2 lines.
- Run the following command:
  ```python
    python3 setup.py
  ```
- If that mail is being used for the first time, a browser will open asking for permission to use extraordinary data from that Google Account. Agree to everything. It is possible that the browser blocks the connection thinking that it is fraudulent, in which case the browser should be gracefully ingnored.
- If that mail had already been used, no browser will open. Either way, a mail will be sent to the account by itself.

## Files Required

- The script requires a file called _mail\_list.csv_ that, for the moment, must contain a header, be separated by a comma and a space and have the following columns: name, last_name, mail and enterprise.
- The script requires a file called _template.txt_ which is a template for the mail which is going to be sent. The template can use each of the target's name, last name, mail or enterprise inside the body just placing, for example, {name} where you want the name to appear.
- The repository contains a _sample\_mail\_list.csv_ file and a _sample\_template.txt_ file for you to modify. Note that the names **MUST** be _mail\_list.csv_ and _template.txt_.
- The script won't work without the setup being completed and the file _client\_secret.json_ being in the repository.
- If you want to send attachments, you must put them in a folder inside the root of the repository named _attachments_.

## Usage

Once the setup is completed and every required file is added, to run the script all that is left is to run:

```python
python3 main.py title
```

Where `title` will be the subject of the mails sent. Note that if `title` is ommited, the subject will be 'Sample Diffusion'.

You can also change most of the naming requirements inside the _parameters.py_ file if you want to do so.

## Considerations

- The column which contains the mails to send the emails **MUST** be called `mail` by default, but it can be changed within _parameters.py_ to match the specific database.
- The csv format can be changed within _parameters.py_ by changing the value `DELIMITER` for the separator and `SKIPINITIALSPACE` to specify an initial space after each delimiter.

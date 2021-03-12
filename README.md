# Motivation Test

This is made to send you a motivational text in the morning. It uses the affirmations api.

## 1. Install dependencies by

`pip install -r requirements.txt`

## 2. Get credentials.json from Gmail API, and add to folder

Make sure to set the callback uri to: `http://localhost:3000/`

Example of 'credentials.json':
 
 `{"web":{"client_id":"<id>","project_id":"<id>","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"<secret>","redirect_uris":["http://localhost:3000/"]}}`

## 3. Configure your settings in `utils.py`.
```py
phone_number = '5555555555' # your phone number
scheduled_time = '01:20'  # make sure the hour has 2 digits (24-hour standard).
email = 'youremail@gmail.com' # your email
carriers = {
    'att': '@txt.att.net',
    'sprint': '@messaging.sprintpcs.com',
    'tmobile': '@tmomail.net',
    'verizon': '@vtext.com'
} # these are the carrier options for SMS
mac = True # set this flag if you want to send the message with iMessage or not. True for iMessage False for SMS
carrier = carriers['att'] # select your carrier
```

## 4. Run script

`python main.py`
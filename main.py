from __future__ import print_function
import requests
import schedule
import time
import subprocess
import util
import pickle
import base64
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


def create_message(to, subject, message_text):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = util.email
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))
    return {'raw': raw_message.decode("utf-8")}


def send_email(service, message):
    try:
        message = service.users().messages().send(userId=util.email, body=message).execute()
        print('Message Id: %s' % message['id'])
        print('Message Sent!')
        return message
    except Exception as e:
        print('An error occurred: %s' % e)
        return None


def send_message(message):
    subprocess.call("osascript sendMessage.applescript '%s' '%s'" % (f'{util.phone_number}', f'{message}'), shell=True)


def get_affirmation():
    r = requests.get('https://www.affirmations.dev/')
    if r.status_code == 200:
        return r.json()['affirmation']
    return ''


def job():
    try:
        affirmation = get_affirmation()
        if affirmation != '':
            if util.mac:
                send_message(affirmation)
            else:
                email_sms(affirmation)
        else:
            print('Error occurred')
    except:
        print('Unable to send email')


def email_sms(message):
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=3000)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    message = create_message(f'{util.phone_number}{util.carrier}', 'Motivation', message)
    send_email(service, message)


if __name__ == '__main__':
    schedule.every().day.at(util.scheduled_time).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

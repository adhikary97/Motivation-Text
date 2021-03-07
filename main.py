import requests
import schedule
import time
import subprocess


def send_message(message):
    subprocess.call("osascript sendMessage.applescript '%s' '%s'" % ('<phone number>', f'{message}'), shell=True)


def job():
    r = requests.get('https://www.affirmations.dev/')
    if r.status_code == 200:
        send_message(r.json()['affirmation'])
    print(r.status_code, r.json())


if __name__ == '__main__':
    schedule.every().day.at("08:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

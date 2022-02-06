# Automated Emails
Send Automated Daily Email News

## Description

An app that reads excel with user names, email addresses, and interests and sends an email to each user
with news feeds about the user's interest once a day.

## Local Installation

* Copy `.env.example` to `.env` and update it with your [NewsApi](https://newsapi.org/account) API key and inputs.

* `python -m venv .venv`
* `source ./.venv/bin/activate`
* `pip install -r requirements.txt`

## Running the application

* py -3 email_file.py



## Developer Notes

### Update requirements
* pip freeze > requirements.txt
* refresh

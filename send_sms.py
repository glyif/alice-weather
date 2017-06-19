from amoeba import env
import os
env.set_env("./.env")
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")

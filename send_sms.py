from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC9f9b2b77ccbd0b7d15b2c40f4a9fe820"
auth_token = "9671335cf1ac69e8de20f746feb0c17d"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="Your number", from_="+",
                                     body="Hello there!")

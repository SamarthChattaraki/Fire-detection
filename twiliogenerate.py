from twilio.rest import Client

account_sid = 'AC1351f5d31a87f241dfe739a0a4d4c343'
auth_token = 'a284dde85f87780df20e41a1f50dcfcd'

twilio_number = '+19289637445'
my_phone_number = '+917259323346'

client = Client(account_sid, auth_token)
msg = "status: HII CLASS"
message = client.messages.create(
body=msg,
from_=twilio_number,
to=my_phone_number
	)
print(message.body)

contacts = [{'ice': '21382173'}, {'david': '7489247892'}]
from twilio.rest import Client


# Find these values at https://twilio.com/user/account
account_sid = "ACcb2b49456476e58cefda5c3bdc623d21"
auth_token = "cefd9804843a804aa86dc97faeac66d1"
client = Client(account_sid, auth_token)

problem = 'mood'
u = 'pereson'

for dictionary in contacts:	#for i in contacts:
	for name in dictionary:
		print dictionary[name]
		message = client.api.account.messages.create(to="+14016543213", from_="+15085572143", body="Hello " + name + ". " + u + "is currently having a hard time with" + problem)
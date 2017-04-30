# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client
import mongoQ

def check_date(m, user):
	# u = {'username': user}
	# uid = m.getUID(u) # {UID: uid}
	# frequency = m.getFrequency(uid) 
	input_info = m.getInput(user, 5) # [{'date': date, 'mood': 5, 'appetite': #, 'productivity': #, 'sleep': #, 'energy': }, {...}, {...}

	print(input_info)
	#date = 'YYYYMMDD'

	thirty = ['04', '06', '09', '11']
	thirtyone = ['01', '03', '05', '07', '08', '10', '12']

	#if frequency == 3:

	for i in range(input_info.count()):
		if i < input_info.count()-2:

			#1 comes after 2 
			n = i + 1
			n2 = n + 1
			log1 = input_info[i]
			log2 = input_info[n]
			log3 = input_info[n2]
			year1 = input_info[i]['date'][:4]
			year2 = input_info[n]['date'][:4]
			year3 = input_info[n2]['date'][:4]
			month1 = input_info[i]['date'][4:6]
			month2 = input_info[n]['date'][4:6]
			month3 = input_info[n2]['date'][:4]
			day1 = input_info[i]['date'][6:]
			day2 = input_info[n]['date'][6:]
			day3 = input_info[n2]['date'][:4]

			if year1 == year2 and year2 == year3:	#if the years are the same
				print '1'
				if month1 == month2 and month2 == month3: 	#if the months are the same
					print '2'
					if int(day1) - int(day2) <= 1 and int(day2) - int(day3) <= 1: #check if the dates are 1 day apart 
						print '3'
						check_status(m,log1, log2, log3)
					else:
						print '4'
						#send reminder to user
				elif month1 >= month2 and month2 == month3: #if left month > right month
					print '5'
					if (month2 in thirty and day1 == '01' and day3 == '29') or (month2 in thirtyone and day1 == '01' and day3 == '30') or (month2 == '02' and day1 == '01' and day3 == '27'):
						print '6'
						check_status(m,log1, log2, log3)
					else:
						print '7'
						#send reminder to user
				elif month1 == month2 and month2 > month3:
					if (month3 in thirty and day1 == '02' and day2 == '01') or (month3 in thirtyone and day1 == '02' and day2 == '01') or (month2 == '02' and day1 == '02' and day3 == '31'):
						print '6'
						check_status(m,log1, log2, log3)
					else:
						print '7'
						#send reminder to user

			elif year1 >= year2 and year2 == year3: #if left month > right month
					print '5'
					if (month1 == '01' and day1 == '01' and month2 == '12' and day2 == '31'):
						print '6'
						check_status(m,log1, log2, log3)
					else:
						print '7'
						#send reminder to user


def check_status(m, l1, l2, l3):
	'''
	date = ''
	mood = #
	appetite = 'Hungry', 'So-so', 'Didnt want to eat anything'
	productivity = 'Productive', 'Did a few things', 'Stayed in bed all day'
	sleep = '0-3', '3-6', '6-9', '9+'
	energy = 'Energized, High, Low, Exhausted'
	feelings = 'Focused, distracted, calm, stressed'
	friends = danrower
	good = reuoqrhioehro

	'''

	if l1['mood'] < l2['mood'] < l3['mood']: 
		call_friends(m,'mood')

	if (l1['appetite'] == 'Didnt want to eat anything' and l2['appetite'] == 'Didnt want to eat anything') or (l2['appetite'] == 'Didnt want to eat anything' and l3['appetite'] == 'Didnt want to eat anything') or (l1['appetite'] == 'Didnt want to eat anything' and l3['appetite'] == 'Didnt want to eat anything'):
		call_friends(m,'appetite')

	if (l1['sleep'] == '0-3' and l2['sleep']) or (l2['sleep'] == '0-3' and l3['sleep']) or (l1['sleep'] == '0-3' and l3['sleep']):
		call_friends(m,'sleep')

	if (l1['energy]'] == 'Low' or l1['energy]']=='Exhausted' and l2['energy'] == 'Low' or l2['energy]']=='Exhausted') or (l2['energy]'] == 'Low' or l2['energy]']=='Exhausted' and l3['energy'] == 'Low' or l3['energy]']=='Exhausted') or (l1['energy]'] == 'Low' or l1['energy]']=='Exhausted' and l3['energy'] == 'Low' or l3['energy]']=='Exhausted'):
		call_friends(m,'energy')

def call_friends(m, problem):

	# Find these values at https://twilio.com/user/account
	account_sid = "ACcb2b49456476e58cefda5c3bdc623d21"
	auth_token = "cefd9804843a804aa86dc97faeac66d1"
	client = Client(account_sid, auth_token)

	contacts = m.getContacts(uid)

	for i in range(len(contacts)):
		for i in contacts.keys: 
			message = client.api.account.messages.create(to="+14016543213", from_="+15085572143", body="Hello")











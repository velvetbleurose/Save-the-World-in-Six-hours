# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client
import mongoQ

def check_date(m, u):
	# u = {'username': user}
	# uid = m.getUID(u) # {UID: uid}
	# frequency = m.getFrequency(uid) 
	input_info = m.getInput(u, 5) # [{'date': date, 'mood': 5, 'appetite': #, 'productivity': #, 'sleep': #, 'energy': }, {...}, {...}

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
			month3 = input_info[n2]['date'][4:6]
			day1 = input_info[i]['date'][6:]
			day2 = input_info[n]['date'][6:]
			day3 = input_info[n2]['date'][6:]

			print(month1 +" " + month2 + " " + month3);

			if year1 == year2 and year2 == year3:	#if the years are the same
				print '1'
				if month1 == month2 and month2 == month3: 	#if the months are the same
					print '2'
					if int(day1) - int(day2) <= 1 and int(day2) - int(day3) <= 1: #check if the dates are 1 day apart 
						print '3'
						print("Check Status one")
						check_status(m,u,log1, log2, log3)
					else:
						print '4'
						#send reminder to user
				elif month1 >= month2 and month2 == month3: #if left month > right month
					print '5'
					if (month2 in thirty and day1 == '01' and day3 == '29') or (month2 in thirtyone and day1 == '01' and day3 == '30') or (month2 == '02' and day1 == '01' and day3 == '27'):
						print '6'
						print("Check Status two")
						check_status(m,u,log1, log2, log3)
					else:
						print '7'
						#send reminder to user
				elif month1 == month2 and month2 > month3:
					if (month3 in thirty and day1 == '02' and day2 == '01') or (month3 in thirtyone and day1 == '02' and day2 == '01') or (month2 == '02' and day1 == '02' and day3 == '31'):
						print '6'
						print("Check Status three")
						check_status(m,u,log1, log2, log3)
					else:
						print '7'
						#send reminder to user

			elif year1 >= year2 and year2 == year3: #if left month > right month
					print '5'
					if (month1 == '01' and day1 == '01' and month2 == '12' and day2 == '31'):
						print '6'
						print("Check Status four")
						check_status(m,u,log1, log2, log3)
					else:
						print '7'
						#send reminder to user



def check_status(m, u, l1, l2, l3):
	'''
	date = ''
	mood = #
	appetite = 'Hungry', 'So-so', 'Didnt want to eat anything'
	productivity = 'Productive', 'Did a few things', 'Stayed in bed all day'
	sleep = '0-3', '3-6', '6-9', '9+'
	energy = 'Energized, High, Low, Exhausted'
	feel = 'Focused, distracted, calm, stressed'
	friends = danrower
	good = reuoqrhioehro

	'''

	if l1['mood'] <= l2['mood'] <= l3['mood']: 
		call_friends(m, u, 'mood')
		return 0

	if (l1['appetite'] == '1' and l2['appetite'] == '1') or (l2['appetite'] == '1' and l3['appetite'] == '1') or (l1['appetite'] == '1' and l3['appetite'] == '1'):
		call_friends(m, u, 'appetite')
		return 0

	if (l1['sleep'] == '1' and l2['sleep'] == '1') or (l2['sleep'] == '1' and l3['sleep'] == '1') or (l1['sleep'] == '1' and l3['sleep'] == '1'):
		call_friends(m, u, 'sleep')
		return 0
	if (l1['productivity'] == '1' and l2['productivity'] == '1') or (l2['productivity'] == '1' and l3['productivity'] == '1') or (l1['productivity'] == '1' and l3['productivity'] == '1'):
		call_friends(m, u, 'productivity')
		return 0
	if (l1['energy'] == '1' or l1['energy']=='2' and l2['energy'] == '1' or l2['energy']=='2') or (l2['energy'] == '1' or l2['energy']=='2' and l3['energy'] == '1' or l3['energy']=='2') or (l1['energy'] == '1' or l1['energy']=='2' and l3['energy'] == '1' or l3['energy']=='2'):
		call_friends(m, u, 'energy')
		return 0
	if (l1['feel'] == '1' or l1['feel']=='2' and l2['feel'] == '1' or l2['feel']=='2') or (l2['feel'] == '1' or l2['feel']=='2' and l3['feel'] == '1' or l3['feel']=='2') or (l1['feel'] == '1' or l1['feel']=='2' and l3['feel'] == '1' or l3['feel']=='2'):
		call_friends(m, u, 'feel')
		return 0

def call_friends(m, u, problem):

	print("calling jeraldin")
	# Find these values at https://twilio.com/user/account
	account_sid = "ACcb2b49456476e58cefda5c3bdc623d21"
	auth_token = "cefd9804843a804aa86dc97faeac66d1"
	client = Client(account_sid, auth_token)

	contacts = m.getContacts(u)

	for dictionary in contacts:	#for i in contacts:
		for name in dictionary:
			print dictionary[name]
			if problem == 'mood':
				message = client.api.account.messages.create(to=dictionary['phone'], from_="+15085572143", body="Hello " + dictionary['name'] + ". " + str(m.getAccount(u)['fullname']) + " needs you today. They have been feeling a little down. Please call them and say hello!")
				return 0
			elif problem == 'appetite':
				message = client.api.account.messages.create(to=dictionary['phone'], from_="+15085572143", body="Hello " + dictionary['name'] + ". " + str(m.getAccount(u)['fullname']) + " needs you today. They haven't been eating well. Please call them and say hello!")
				return 0
			elif problem == 'sleep':
				message = client.api.account.messages.create(to=dictionary['phone'], from_="+15085572143", body="Hello " + dictionary['name'] + ". " + str(m.getAccount(u)['fullname']) + " needs you today. They haven't been sleeping. Please call them and say hello!")
				return 0
			elif problem == 'productivity':
				message = client.api.account.messages.create(to=dictionary['phone'], from_="+15085572143", body="Hello " + dictionary['name'] + ". " + str(m.getAccount(u)['fullname']) + " needs you today. They stayed in bed all day for a couple days. Please call them and say hello!")
				return 0
			elif problem == 'energy':
				message = client.api.account.messages.create(to=dictionary['phone'], from_="+15085572143", body="Hello " + dictionary['name'] + ". " + str(m.getAccount(u)['fullname']) + " needs you today. Their energy has been a little down. Please call them and say hello!")
				return 0
			elif problem == 'feel':
				message = client.api.account.messages.create(to=dictionary['phone'], from_="+15085572143", body="Hello " + dictionary['name'] + ". " + str(m.getAccount(u)['fullname']) + " needs you today. Their feeling a little off today. Please call them and say hello!")
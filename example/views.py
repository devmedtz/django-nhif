import requests
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from nhif.token import generateToken

def client_verification(request):

	username = settings.USERNAME
	password = settings.PASSWORD

	#Specify the url for token generation according to requested service
	address = 'http://196.13.105.15/nhifservice/Token'
	results = generateToken(username, password, address)
	access_token = results['access_token']


	# Client Verification Start
	url = 'http://196.13.105.15/nhifservice/breeze/verification/AuthorizeCard'

	# Define your parameters
	card_no = '01-nhif241'
	visit_type_id = '1'
	referral_no = ''
	remarks = ''

	payload = {
		'CardNo': card_no,
		'VisitTypeID': visit_type_id,
		'ReferralNo': referral_no,
		'Remarks': remarks,
	}

	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Bearer {}'.format(access_token)
	}

	output = requests.get(url=url, params=payload, headers=headers)
	output = json.loads(output.text)

	print(output)

	return JsonResponse(data=output, safe=False)
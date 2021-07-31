# django-nhif

A Django application which assist on integration of your web application with NHIF System with easy step.

## Prerequisites

* Python 3.6+
* Pip or Pipenv

## It will Cover

* [x] Generate Access Token to initiate call
* [x] Enable easy generation of access token for any nhif service claim

## Installation

This package is available in [Python Package Index](https://pypi.org/project/django-nhif/) and can be installed using `pip` or `pipenv`

1. Run ``pip install django-nhif``
2. Add ``nhif`` to ``INSTALLED_APPS``

## Usage

### Contact with NHIF office near your to get username and password, for testing use bellow credentials

1. username = 'integrationuser'
2. password = 'nhif@2018'

## Open "settings.py" on your project, set the following variables

1. USERNAME = "your username"
2. PASSWORD = "your api password"

## After setting above,Then on your views.py file, This show an example on how to generate access token and verify patient before offer any service.

```python
import json
import requests
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
```

### sample response

```python
{"$id": "1", "$type": "Dapper.SqlMapper+DapperRow, Dapper", "AuthorizationID": "0aaf0dcd-eb40-4df5-8ed0-56bb62cdbf37", "CardNo": "01-nhif241", "MembershipNo": "900035308", "EmployerNo": null, "EmployerName": null, "HasSupplementary": "No", "SchemeID": 1001, "SchemeName": "Standard NHIF Benefit Scheme", "CardExistence": "EXISTING", "CardStatusID": 4, "CardStatus": "Inactive", "IsValidCard": false, "IsActive": false, "StatusDescription": "Revoked", "FirstName": "Amour", "MiddleName": "R", "LastName": "Hamad", "FullName": "Amour R Hamad", "Gender": "Male", "PFNumber": "NHIF241", "DateOfBirth": "1974-03-18", "YearOfBirth": 1974, "Age": "47", "ExpiryDate": null, "CHNationalID": null, "LatestContribution": "Not Available", "AuthorizationStatus": "REJECTED", "AuthorizationNo": null, "LatestAuthorization": "UPANGA EYE SPECIALIZED CLINIC on July 26,2021", "Remarks": "The card is In Active,If the beneficiary thinks this is is a mistake he should visit the nearby NHIF office for verification", "FacilityCode": "06697", "ProductName": "STANDARD", "ProductCode": "NH011", "CreatedBy": "integrationuser", "AuthorizationDate": "2021-07-31T18:33:32.050", "DateCreated": "2021-07-31T18:33:32.050", "LastModifiedBy": "integrationuser", "LastModified": "2021-07-31T18:33:32.050", "AuthorizationDateSerial": 20210731}
```

### For full example on how to integrate please visit the github repo on example folder you will find all source codes [here](https://github.com/devmed/django-nhif)

## Give it a star

If you found this repository useful, give it a star so as the whole community of Tanzania developers can get to know it.

## Bug bounty?

If you encounter issue with the usage of the package, feel free raise an issue so as we can fix it as soon as possible(ASAP).

## Pull Requests

If you have something to add I welcome pull requests on improvement , you're helpful contribution will be merged as soon as possible

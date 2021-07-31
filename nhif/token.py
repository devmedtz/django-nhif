from nhif.api_call import (APIRequest, APIResponse, APIContext, APIMethodType) 


def generateToken(username, password, address):

	api_context = APIContext()

	# USERNAME
	api_context.username = username

	# Password
	api_context.password = password

	# address
	api_context.address = address

	# Method type (can be GET/POST)
	api_context.method_type = APIMethodType.POST

	# Define your grant type parameters
	parameters = {
		'grant_type' : 'password',
        'username': username,
        'password': password,
	}

	# add parameters on request 
	api_context.parameters = parameters

	#Do the API call and put result in a response packet
	api_request = APIRequest(api_context)

	result = None

	try:
		result = api_request.execute()
	except Exception as e:
		print('Call Failed:', e)

	if result is None:
		raise Exception('Call failed to get result. Please check.')

	return result.body
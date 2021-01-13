from instamojo_wrapper import Instamojo


API_KEY = 'test_e6f3ee14401e08c4f2605416b8b'
AUTH_TOKEN = 'test_1f464b71f44e8a749d23a337209'
api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');

response = api.payment_request_create(
    amount='11',
    purpose='testing',
    send_email=True,
    email="pox420@gmail.com",
    redirect_url="http://www.example.com/handle_redirect.py"
)

print(response['payment_request']['longurl'])

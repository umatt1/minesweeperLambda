import requests

def lambda_handler(event, context):
    try:
        # Define the API endpoint URL
        api_url = 'https://api.example.com/endpoint'

        # Make an HTTP GET request to the API
        response = requests.get(api_url)

        # Log the API response
        print('API Response:', response.json())

        # Return a success message or any relevant data
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Successfully called the API', 'data': response.json()})
        }
    except Exception as e:
        # Log and return an error message if the API call fails
        print('Error calling the API:', str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error calling the API', 'error': str(e)})
        }


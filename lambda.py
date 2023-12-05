import requests
import json
import random
import time

def puzzle_maker(length, width, mines):
    random.seed(time.time())

    puzzle = [[0 for _ in range(width)] for _ in range(length)]

    # Place mines randomly
    for _ in range(mines):
        row = random.randint(0, length - 1)
        col = random.randint(0, width - 1)
        puzzle[row][col] = 1

    return puzzle

def lambda_handler(event, context):
    try:
        # Define the API endpoint URL
        api_url = 'https://api.example.com/endpoint'

        # Create a puzzle
        puzzle = puzzle_maker(5,5,5)

        # Make an HTTP GET request to the API
        response = requests.post(api_url)

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


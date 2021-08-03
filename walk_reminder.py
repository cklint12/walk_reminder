import time
import webbrowser 
import requests
import random 

"""
A reminder that that tells you to go for a walk when the countdown timer reaches zero

"""

def countdown(time_input): 
    """Counts down 

    Args:
        time_input minutes: User input time in minuts
    """

    time_input_secs = minutes_to_secs(time_input)
    while time_input_secs:
        mins, secs = divmod(time_input_secs, 60)
        print(mins, secs)
        time.sleep(1)
        time_input_secs -= 1
    

def minutes_to_secs(minutes):
    """
        A helper function to convert minutes to seconds

        Arguments: minutes - the time that needs to be converted
    
    """
    return minutes*60 

def launch_gif():
    data_api = {

    'api_key': 'X6w98bPrMJB9yKnnM8j0vhJa8QdxrFZZ',
    'q' :'walk'
    
    }
    
    response = requests.get('https://api.giphy.com/v1/gifs/search', data_api).json()
    random_index = random.randint(0,len(response['data']))
    url = response['data'][random_index]['embed_url']
    webbrowser.open(url)


if __name__=='__main__':
    while True: 
        countdown(50)
        launch_gif()



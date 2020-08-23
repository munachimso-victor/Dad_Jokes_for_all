from pyfiglet import figlet_format as formati
from termcolor import colored
import requests
from random import choice


def heading():
    response = formati("Dad Jokes for all")
    color_it = colored(response)
    color_it= colored(response, color="red", attrs=["blink"])
    print(color_it)


def joke(input_user):
    """
    query strings are used to send additional data along with a get request. they can either be hardcoded to the link,
    or done using the params keyword, and putting it the query (queries are jey value pair). the term parameter is used
    to search term to use to find a joke. We knew this about term from the api documentation provided by
    "icanhazdadjoke.com" we can use the limit parameter to specify max amount of jokes needed instead ("limit": 1)
    instead of using random.choices to pick from all the jokes given, but random makes it random so we do not get the
    same joke eveytime

    the result from data gives us a dictionary of lists, but we are only interested in two key-value pairs
    the "total_jokes" pair that gives us the total number of jokes, and the "results" pair which gives us
     a list that contains a dictionary of  ID and joke of what we asked for from the "term": input_user query string

    we use the above 'for loop' to loop through the the data[results] values and create a list taking out the jokes
    from the 'jokes' key in the dictionary of (joke and id) contained in the value of results which is a list

    """


    url = "https://icanhazdadjoke.com/search"
    my_source = requests.get(url, headers={"Accept": "application/json"}, params={"term": input_user})
    data = my_source.json()
    jokes = [collection["joke"] for collection in data["results"]]
    total_jokes = data["total_jokes"]

    if input_user:
        if total_jokes > 1:
            choices = choice(jokes)
            print(f"I have {len(jokes)} jokes that contains '{input_user}' for you. Here is one: ")
            print("\n")
            print(choices)
            print("\n")

        elif total_jokes == 1:
            print(f"I've got one joke that contains '{input_user}' for you. Here it is: ")
            print("\n")
            print(jokes[0])
            print("\n")
        else:
            print(f"Sorry, I do not have jokes that contains '{input_user}' for you")
            print("\n")

    else:
        choices = choice(jokes)
        print(f"I have {len(jokes)} random jokes for you. Here is one: ")
        print("\n")
        print(choices)
        print("\n")

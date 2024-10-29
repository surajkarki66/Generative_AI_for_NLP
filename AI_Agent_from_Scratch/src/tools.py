"""
These tools are simple Python functions that perform specific tasks.
Here’s an example of a news, a string capitalizer and a string reverser:
"""

import requests

def fetch_trending_news():
    """
    Fetch and return trending news headlines using the News API.

    Returns:
    str: A formatted string containing trending news headlines.
    """
    # Define the URL and parameters for the News API request
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",  # Fetches top headlines from the United States
        "apiKey": "a38396c0b3254e3cb4c178f10a892e1c"
    }

    try:
        # Send a request to the News API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error if the request failed
        data = response.json()

        # Extract the top 10 headlines
        articles = data.get("articles", [])[:10]
        trending_news = [article["title"] for article in articles]

        # Format the trending news into a single string
        news_string = "\n".join(f"{i+1}. {headline}" for i, headline in enumerate(trending_news))
        formatted_news = f"Trending News Headlines:\n{news_string}\n\n.Executed using the fetch_trending_news function."

        # print(f"DEBUG: formatted_news: {formatted_news}")
        return formatted_news

    except requests.exceptions.RequestException as e:
        return f"Error fetching trending news: {e}"


def capitalize_words(input_string):
    """
    Capitalize the first letter of each word in the given string.

    Parameters:
    input_string (str): The string with words to be capitalized.

    Returns:
    str: The string with each word capitalized.
    """
    # Capitalize each word
    capitalized_string = input_string.title()

    capitalized_string = f"The capitalized string is: {capitalized_string}\n\n.Executed using the capitalize_words function."
    # print(f"DEBUG: capitalized_string: {capitalized_string}")
    return capitalized_string


def reverse_string(input_string):
    """
    Reverse the given string.

    Parameters:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Reverse the string using slicing
    reversed_string = input_string[::-1]

    reversed_string = f"The reversed string is: {reversed_string}\n\n.Executed using the reverse_string function."
    # print (f"DEBUG: reversed_string: {reversed_string}")
    return reversed_string
#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [

    "You must be the change you wish to see in the world. -Mahatma Gandhi",
    "Spread love everywhere you go. Let no one ever come to you without leaving happier. -Mother Teresa",
    "The only thing we have to fear is fear itself. -Franklin D. Roosevelt",
    "Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that. -Martin Luther King Jr.",
    "Do one thing every day that scares you. -Eleanor Roosevelt",
    "Well done is better than well said. -Benjamin Franklin",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. -Helen Keller",
    "It is during our darkest moments that we must focus to see the light. -Aristotle",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. -Ralph Waldo Emerson",
    "Be yourself; everyone else is already taken. -Oscar Wilde"

]
 
def get_quote_of_the_day(quotes):
    todays_quote = None
    today = date.today()
    todays_quote = random.choice(quotes)  

    return todays_quote

if __name__ == "__main__":
    quote_of_the_day = get_quote_of_the_day(quotes)
    print(quote_of_the_day)

    with open("daily_quotes.txt", "a") as file:
        file.write(f"{date.today()}: {quote_of_the_day}\n")

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 "C:/Users/jelou\-/Documents/DataSci_217_Git_Python/03-data-structures-klouie07/01-daily_quote.py" >> "C:/Users/jelou/Documents/DataSci_217_Git_Python/03-data-structures-klouie07/daily_quotes.txt"
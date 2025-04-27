import discord
import os
import csv
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Discord Bot Token from environment variable
DISCORD_TOKEN = os.getenv("TOKEN")  # The bot token will be fetched from the .env file

# Function to load bot rules from CSV (dynamic handling of message/response headers)
def load_rules(file_path):
    rules = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)  # Use DictReader to access header columns
            for row in reader:
                pattern = row['message']  # Assuming 'message' column contains the pattern
                response = row['response']  # Assuming 'response' column contains the response
                if pattern.strip():  # Skip empty patterns
                    # Replace '*' with '.*' to match any characters (wildcard to regex)
                    pattern = pattern.replace('*', '.*')
                    rules[pattern] = response
                else:
                    print(f"Warning: Skipping empty pattern in row: {row}")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
    return rules

# Bot Test class for Discord
class BotTester(discord.Client):
    def __init__(self, rules, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rules = rules

    async def on_ready(self):
        print(f'Bot has logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:  # Ignore messages from the bot itself
            return
        
        # Check for matching patterns in the CSV rules
        response = self.get_response(message.content)
        
        # Send the response to the Discord channel
        await message.channel.send(response)

    def get_response(self, message):
        # Iterate through each pattern in the rules and return the matching response
        for pattern, response in self.rules.items():
            if re.search(pattern, message, re.IGNORECASE):
                return response
        return "I'm sorry, I don't understand that."

    def run_tests(self, channel_id):
        # Iterate over the test cases and simulate sending messages to the bot
        for message, expected_response in self.rules.items():
            print(f"Testing message: {message}")
            actual_response = self.get_response(message)  # Simulate response
            
            print(f"Expected response: {expected_response}")
            print(f"Actual response: {actual_response}")
            
            # Compare responses and log result
            if re.search(expected_response, actual_response, re.IGNORECASE):
                print("Test Passed!")
            else:
                print("Test Failed!")

if __name__ == '__main__':
    # Example: Use .env file or hardcode path to CSV file and token
    CSV_FILE_PATH = 'bot-rules-2.csv'  # Your path to the CSV file with test cases
    
    # Load the bot rules from CSV file
    rules = load_rules(CSV_FILE_PATH)
    
    if rules:
        # Initialize and run the bot
        bot_tester = BotTester(rules)
        bot_tester.run(DISCORD_TOKEN)  # Use the bot's token to run the bot
    else:
        print("No rules found. Please check the CSV file.")

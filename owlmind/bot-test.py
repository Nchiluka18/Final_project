import re
import csv

# Function to load the bot rules from a CSV file and store them in a dictionary
def load_rules(file_path):
    rules = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                pattern, response = row
                # Check if the pattern is not empty
                if pattern.strip():
                    # Replace '*' with '.*' to match any characters (similar to wildcard in regex)
                    pattern = pattern.replace('*', '.*')
                    rules[pattern] = response
                else:
                    print(f"Warning: Skipping empty pattern: {row}")
            else:
                print(f"Warning: Invalid row (not a pattern-response pair): {row}")
    return rules


# Bot Test class to simulate bot message handling based on loaded rules
class BotTest:
    def __init__(self, rules):
        self.rules = rules
    
    def process_message(self, message):
        for pattern, response in self.rules.items():
            # Match the message to the pattern (simple regex match)
            if re.search(pattern, message, re.IGNORECASE):
                return response
        return "I'm sorry, I don't understand that."


if __name__ == '__main__':
    # Load the bot rules from CSV file
    rules = load_rules('rules/bot-rules-2.csv')
    
    # Create an instance of BotTest (instead of DiscordBot in this test)
    bot_test = BotTest(rules)
    
    # Test the bot by simulating a message and printing the response
    test_messages = [
        "hello", 
        "Hi!",  
        "hello everyone", 
        "hi there",
        "Good evening", 
        "Good morning", 
    ]
    
    # Simulate processing each test message and output the response
    for message in test_messages:
        response = bot_test.process_message(message)
        print(f"Input: {message}\nResponse: {response}\n")

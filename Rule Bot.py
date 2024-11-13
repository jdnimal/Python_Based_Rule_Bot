import re
import random

class RuleBot:
    ### Potential negative responses
    negative_responses = ("no", "nope", "na", "nuh", "nah", "not a chance", "sorry", "not")
    ### Potential positive responses
    positive_responses = ("yes", "yep", "yeah", "yuh", "yea", "yup", "sure")
    ### Potential neutral responses
    neutral_responses = ("maybe", "i don't know", "i'm not sure", "idk")
    ### Conversation Quitting Keywords
    exit_commands = ("quit", "exit", "stop", "bye", "goodbye", "later", "peace out", "thank you", "close")
    # Random starter questions
    random_questions = ("Why are you here?\n", 
                        "Are there many humans like you?\n", 
                        "What do you consume for sustenance?\n", 
                        "Is there intelligent life on this planet?\n", 
                        "Does this planet have a leader?\n", 
                        "Which plantes have you visited?\n", 
                        "What is the technology of this planet?\n")

    def __init__(self):
        self.alienblabber = {'describe_planet_intent': r'.*\s*your planet.*',
                            'answer_why_intent': r'why\sare.*',
                            'about_creator': r'.*\s*creator'}
        
    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input( f"Hi {self.name}, I am a Rule-Bot. Will you help me learn about your planet?\n")
        if will_help in self.negative_responses:
            print("Okay, I'll just go ahead and leave then.")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, I'll just go ahead and leave then.")
                return True

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienblabber.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_creator':
                return self.about_creator()
            if not found_match:
                return self.no_match_intent()


    def describe_planet_intent (self):
        responses = ("My planet is a utopia of diverse organisms and species.\n", 
                    "I am from Opidipus, the capital of the Wayward Galaxies.\n")
        return random.choice (responses)

    def answer_why_intent (self):
        responses = ("I come in peace\n", 
                    "I am here to collect data on your planet and its inhabitants\n",
                    "I heard the coffee is good\n")
        return random.choice(responses)

    def about_creator(self):
        responses = ("Creator is world's smartest and utmost prime form an entity\n",
                    "He can help you move forward in life and grow in the way you cannot even imagine\n",
                    "He is known as the creator because he created everything\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("Please tell me more.\n", 
                    "Tell me more! \n", 
                    "Why do you say that?\n", 
                    "I see. Can you elaborate?\n",
                    "Interesting. Can you tell me more?\n", 
                    "I see. How do you think?\n", "Why?\n",
                    "How do you think I feel when you say that?\n")
        return random.choice (responses)

AlienBot = RuleBot()
AlienBot.greet()
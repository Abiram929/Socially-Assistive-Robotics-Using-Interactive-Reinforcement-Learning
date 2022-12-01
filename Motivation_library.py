import random


def get_positive(correct):
    positive_success = ["That was great! Keep up the good work!", "Wow, you do really great! Go on!", "That's awesome! You got it! Keep going!", "Fantastic! You do great! Keep going!", "Quite amazing, you are the best!!","That was great! Keep it up!", "You are in your zone now... quite literally unstoppable!!"]
    
    positive_failure = ["Oh, that was wrong! But that's fine! Don't give up!", "Oh, you missed it! No problem! Go on!", "Oops, that was not correct! That's OK! Keep going!", "Oops, too close! Stay focused and you will do it!", "You have another chance, you can do it!", "Try again next time, there is some promise here!"]
    
    if correct==0:
        return random.choice(positive_success)
    else:
        return random.choice(positive_failure)

def get_neutral(correct):
    neutral_success = ["Great.. now let's proceed further", "You got that right, can you do it again?", "That was correct, now on to the next one!", "You gave the right answer, let's see if you can continue to do so"]
    
    neutral_failure = ["Hmmm wrong answer, you have the opportunity to redeem yourself!", "So that was incorrect, you can make that right on the next question", "Not so great that, lets try again shall we"]
    
    if correct==0:
        return random.choice(neutral_success)
    else:
        return random.choice(neutral_failure)
    

def get_negative(correct):   
    negative_success = ["Ok, that was easy enough! Let's see again!", "Well, ok! Maybe you were lucky! Let's check the next one!", "OK, you got it! Was it random?? Let's try again.", "OK, I guess you made it! Maybe, it was an easy one!", "Google the definition of luck and you will get a replay of what just happened", "Yeah yeah, that was pretty easy and you know it", "Some questions are easier than others I guess"]
    
    negative_failure = ["Hmmm! I don't think you are paying any attention! Try harder!", "Hey! Are you there? Stay focused when I speak!", "Oh! was that wrong? Well, you actually need to pay attention!", "If you want to succeed, you need to pay attention!", "My faith in humanity is decreasing with every question", "I don't think you are cut out for this", "When will you ever learn to repeat the sequence properly!", "When you finally have your brain back, call me!", "Utter rubbish! Even my pet dog could've answered that correctly", "You are a failure, I hope you know that. And no, this is not the phrase to repeat."]
    
    if correct==0:
        return random.choice(negative_success)
    else:
        return random.choice(negative_failure)



def generate_motivation(valence, correct):
    
    if valence == 2:
        return get_positive(correct)
    elif valence == 1:
        return get_neutral(correct)
    else:
        return get_negative(correct)


    
   
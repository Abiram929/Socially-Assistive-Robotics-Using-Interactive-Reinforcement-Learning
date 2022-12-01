from furhat_remote_api import FurhatRemoteAPI
import time
from Questions_library import generate_question
import easygui
from Motivation_library import generate_motivation
from Gesture_library import generate_gestures
import random

def furhat_questions(question_no,valence,task_difficulty):

    # Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
    furhat = FurhatRemoteAPI("localhost")
    
    # Attend the user closest to the robot
    furhat.attend(user="CLOSEST")
    
    # Get the voices on the robot
    voices = furhat.get_voices()
    # Set the voice of the robot
    furhat.set_voice(name='Aditi')
    # Say "Hi there!"
    furhat.say(text="Hi there!", lipsync=True)
    
    if question_no==1:
        furhat.gesture(name="BrowRaise")
        furhat.say(text="Welcome to the sequence learning task!", lipsync=True)
        furhat.say(text="You will be given six sequences of letters of varying length to repeat!", lipsync=True)

        

    
    furhat.say(text="Get ready for the upcoming question!", lipsync=True)
    
    furhat.say(text="The following is your phrase to repeat", lipsync=True)
    
    current_sequence = generate_question(task_difficulty)
    
    print(current_sequence)
    
    for i in current_sequence:
        furhat.say(text=i, lipsync=True)
        furhat.gesture(name="BrowRaise")
        time.sleep(2)

    
    # Listen to user speech and return result
    answer=""
    
    while answer == "" or answer == " ":
        result = furhat.listen()        
        answer=result.message
        furhat.gesture(name="BrowRaise") 
        answer=answer.replace(" ","")
        answer=answer.upper()
    
    
    title_string="Sequence Learning Task: Question" + " " + str(question_no)
    
    answer = easygui.enterbox(msg='Confirm your answer:', title=title_string, default=answer, strip=True)
    
    answer=answer.replace(" ","")
    answer=answer.upper()
    
    correct=0
    
    if current_sequence==answer:
            furhat.say(text="Correct answer", lipsync=True)
            correct=0
    else:
            furhat.say(text="Incorrect answer", lipsync=True)
            correct=1
            
        
    
    furhat.say(text=generate_motivation(valence, correct), lipsync=True)
    
    # Perform a custom gesture
    chosen_gesture= generate_gestures(valence)

    if chosen_gesture[1]==0:
        furhat.gesture(name=chosen_gesture[0])
    else:
        furhat.gesture(body=chosen_gesture[0])
        
        
    if valence==2:
        for i in range(3000):
            furhat.set_led(red=0, green=0, blue=0)
            furhat.set_led(red=0, green=255, blue=0)
    elif valence==1:
        for i in range(3000):
            furhat.set_led(red=0, green=0, blue=0)            
            furhat.set_led(red=255, green=215, blue=0)
    else:
        for i in range(3000):
            furhat.set_led(red=0, green=0, blue=0)            
            furhat.set_led(red=255, green=0, blue=0)
        
        
    # Get the users detected by the robot 
    users = furhat.get_users()

    # Attend the user closest to the robot
    furhat.attend(user="CLOSEST")
    
    return current_sequence, answer


def user_model_one(question_no,valence,task_difficulty):

    current_sequence = generate_question(task_difficulty)
    print(current_sequence)
    # Listen to user speech and return ASR result
    answer= current_sequence
    
    return current_sequence, answer


def user_model_two(question_no,valence,task_difficulty):
    
    current_sequence = generate_question(task_difficulty)
    print(current_sequence)
    # Listen to user speech and return ASR result
    answer= "A"
    
    valenceProbabilities={0:0.9, 1:0.6, 2:0.9}
    
    taskProbabilities = {1:0.90, 2:0.8, 3:0.6, 4:0.5}
    
    questionProbabilities = {1:0.7, 2:0.8, 3:0.9, 4:1, 5:1, 6:1}
    
    probability = valenceProbabilities[valence] * taskProbabilities[task_difficulty] * questionProbabilities[question_no] * 100
    
    probability = int(probability)
    
    if random.randint(0,100) < probability:
        answer=current_sequence
    else:
        answer="A"
    
    return current_sequence, answer

def user_model_three(question_no,valence,task_difficulty):
    
    current_sequence = generate_question(task_difficulty)
    print(current_sequence)
    # Listen to user speech and return ASR result
    answer= "A"
    
    valenceProbabilities = {0:0.4, 1:0.6, 2:0.9}
    
    taskProbabilities = {1:0.9, 2:0.8, 3:0.6, 4:0.5}
    
    questionProbabilities = {1:0.7, 2:0.8, 3:0.9, 4:1, 5:1, 6:1}
    
    probability = valenceProbabilities[valence] * taskProbabilities[task_difficulty] * questionProbabilities[question_no] * 100
    
    probability = int(probability)
    
    if random.randint(0,100) < probability:
        answer=current_sequence
    else:
        answer="A"
    
    return current_sequence, answer

def user_model_four(question_no,valence,task_difficulty):
    
    current_sequence = generate_question(task_difficulty)
    print(current_sequence)
    # Listen to user speech and return ASR result
    answer= "A"
    
    valenceProbabilities = {0:0.9, 1:0.5, 2:0.5}
    
    taskProbabilities = {1:0.5, 2:0.6, 3:0.9, 4:0.9}
    
    questionProbabilities = {1:0.7, 2:0.8, 3:0.9, 4:1, 5:1, 6:1}
    
    probability = valenceProbabilities[valence] * taskProbabilities[task_difficulty] * questionProbabilities[question_no] * 100
    
    probability = int(probability)
    
    if random.randint(0,100) < probability:
        answer=current_sequence
    else:
        answer="A"
    
    return current_sequence, answer

def user_model_five(question_no,valence,task_difficulty):
    
    current_sequence = generate_question(task_difficulty)
    print(current_sequence)
    # Listen to user speech and return ASR result
    answer= "A"
    
    valenceProbabilities = {0:0.1, 1:0.9, 2:0.9}
    
    taskProbabilities = {1:0.9, 2:0.8, 3:0.6, 4:0.5}
    
    questionProbabilities = {1:0.7, 2:0.8, 3:0.9, 4:1, 5:1, 6:1}
    
    probability = valenceProbabilities[valence] * taskProbabilities[task_difficulty] * questionProbabilities[question_no] * 100
    
    probability = int(probability)
    
    if random.randint(0,100) < probability:
        answer=current_sequence
    else:
        answer="A"
    
    return current_sequence, answer

def user_model_six(question_no,valence,task_difficulty):
    
    current_sequence = generate_question(task_difficulty)
    print(current_sequence)
    # Listen to user speech and return ASR result
    answer= "A"
    
    valenceProbabilities = {0:0, 1:0, 2:1}
    
    taskProbabilities = {1:0, 2:1, 3:0, 4:0}
    
    questionProbabilities = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}
    
    probability = valenceProbabilities[valence] * taskProbabilities[task_difficulty] * questionProbabilities[question_no] * 100
    
    probability = int(probability)
    
    if random.randint(0,100) < probability:
        answer=current_sequence
    else:
        answer="A"
    
    return current_sequence, answer
    
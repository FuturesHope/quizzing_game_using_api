import requests as r
import json
import random

# inform the user about the purpose of this game
print('\nThis is "FuturesHope" quizz game \n')
# take user's name
user_name = input('Please provide your name: ')
# Choose a theme for quiz game from API or think or how to let the user make the choice
print('You will be given multiple choice questions from different categories of knowledge \n')
user_difficulty_choice = input('Choose the difficulty for questions: \n1 - for easy\n2 - for medium\n3 - for hard\n')
print("\nOK, lets Go!\n")
# save the API url without difficulty variable
api_url = 'https://opentdb.com/api.php?amount=1&type=multiple&difficulty='
# combine the API url with the user difficulty choice
list_of_difficulty = ['easy', 'medium', 'hard']
try:
    user_api = api_url+list_of_difficulty[int(user_difficulty_choice)-1]
except:
    user_api = 'https://opentdb.com/api.php?amount=1&type=multiple&difficulty=easy'
    print("\n 'easy' mode questions were picked automatically due to unrecognized value of choice..\n")
# ask the user to press Enter to start the game
input('Press enter to start the game')# put some progress calculations

num_of_correct_answers = 0
# num_of_incorrect_answers = 0
total_num_of_plays = 0

while True:
    # load an api request
    quizz_api_req = r.get(user_api)
    # make a local dictionary out of the HTTP response
    py_dict = json.loads(quizz_api_req.text) # this is a dict type obj
    # parse the variables out of the request json
    category = py_dict['results'][0]['category']
    question = py_dict['results'][0]['question']
    correct_answer = py_dict['results'][0]['correct_answer']
    incorrect_answers_list = py_dict['results'][0]['incorrect_answers']

    # Put together all the answers
    all_variants_answers = incorrect_answers_list + [correct_answer]
    # shuffle the deck of answers
    random.shuffle(all_variants_answers)
    ava = all_variants_answers

    print('\n   Question category: {}'.format(category))
    print('\n Question: {}'.format(question))
    print("\n1. {}\n2. {}\n3. {}\n4. {}".format(ava[0],ava[1],ava[2],ava[3]))

    user_input_validated=False
    while(user_input_validated==False):
        user_input=input('give your variant (1 to 4), or "Enter" for next question or type "quit"\n ').lower()
        if (user_input=="" or user_input=="quit"):
            user_input_validated=True
            break
        try:
            int(user_input)
            user_input_validated=True
        except:
            print("\n Ups, please type the number of the answer instead of words..\n")
            continue

    if user_input=='quit':
        print('\nThank you for playing "FuturesHope" quiz game')
        print("\n You played {} quizzez!".format(total_num_of_plays))
        print("{}, You answered {} correct answers!!! Good job! =)\n".format(user_name,num_of_correct_answers))
        break
    elif user_input=='':
        print('The correct answer was: {}\n'.format(correct_answer))
        print('\n Next question: \n')
        continue
    else:
        total_num_of_plays+=1 # record the fact of user guess attempt
        # the block of code to compare user input to correct answers
        if int(user_input)==ava.index(correct_answer)+1:
            num_of_correct_answers+=1
            print("\n This is correct answer! Congratulations! Lets's continue..")
            input("\n Press Enter to continue.")
            continue
        else:
            # num_of_incorrect_answers+=1
            print("\n Ups, a miss.., \n The correct answer is: {}".format(correct_answer))
            input("\nPress Enter to continue.")
            continue

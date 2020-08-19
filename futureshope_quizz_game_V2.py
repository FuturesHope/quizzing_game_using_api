import requests
import json
import random
import html

# inform the user about the purpose of this game
print('\nThis is "FuturesHope" quizz game \n')
# take user's name
user_name = input('Please provide your name: ')
print("\nOK ***{}***, lets Go!\n".format(user_name))
# save the API url
api_url = 'https://opentdb.com/api.php?amount=1&type=multiple'

num_of_correct_answers = 0
# num_of_incorrect_answers = 0
total_num_of_plays = 0
# create a var for holding user inputs for game control in while loop
stop_game = ""

while stop_game != "quit":
    # load an api request
    quizz_api_req = requests.get(api_url)
    #check for the status code
    if(quizz_api_req.status_code != 200):
        stop_game = input('\nConnection to server failed, please press Enter to restart or quit.\n')
    else:
        # make a local dictionary out of the HTTP response
        py_dict = json.loads(quizz_api_req.text) # this is a dict type obj
        # parse the variables out of the request json
        question_category = py_dict['results'][0]['category']
        question = py_dict['results'][0]['question']
        correct_answer = py_dict['results'][0]['correct_answer']
        incorrect_answers_list = py_dict['results'][0]['incorrect_answers']

        #TEMPorary
        print('corect answer is {}'.format(correct_answer))
        # _____________________________
        # Put together all the answers
        all_answers = incorrect_answers_list + [correct_answer]
        # shuffle the deck of answers
        random.shuffle(all_answers)

        print('\n Question category: {}'.format(html.unescape(question_category)))
        print('\n Question: {}\n'.format(html.unescape(question)))
        # hold the number of answers for user presentation
        answer_number = 1
        # print the variants of answers to user
        for el in all_answers:
            print(str(answer_number)+' - '+html.unescape(el))
            answer_number+=1

        # ask for user answer, vaidate user answer
        user_answer_validated=False
        while user_answer_validated==False:
            user_answer=input("\nPlease provide your answer \n\t")
            try:
                user_answer=int(user_answer)
                if user_answer<=0 or user_answer>=5:
                    print("Please provide a digit from 1 to 4 as an answer")
                else:
                    user_answer_validated=True
            except:
                print("\nPlease provide a digit as an answer from question numbers")
        # check for user answer correctness
        user_answer=all_answers[int(user_answer)-1]
        if user_answer==correct_answer:
            num_of_correct_answers+=1
            print('\n "{}"  is the correct answer!'.format(correct_answer))
        else:
            print('\nThis is an incorrect answer, the correct one is "{}"'.format(correct_answer))
        # register user progress
        # tell the results
        total_num_of_plays+=1
        print('\n**Your scores*******')
        print("Number of correct asnwers: {}".format(num_of_correct_answers))
        print("Total rounds: {}".format(total_num_of_plays))
        print('******************')
        stop_game=input('\nPress Enter you like to continue the game or quit?  ')

print("\n Thank you for playing this quizz game!")

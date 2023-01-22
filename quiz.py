quiz = {
    "quesion1":{
        "question":"What is the capital of India?",
        "answer":"Delhi"
    },
    "question2":{
        "question":"What is the capital of Germany?",
        "answer":"Berlin"
    },
    "quesion3":{
        "question":"What is the capital of Italy?",
        "answer":"Rome"
    },
    "question4":{
        "question":"What is the capital of Portugal?",
        "answer":"Lisbon"
    },
    "quesion5":{
        "question":"What is the capital of Austria?",
        "answer":"Vienna"
    },
    "question6":{
        "question":"What is the capital of Switzerland?",
        "answer":"Bern"
    },

}


score = 0

for key,value in quiz.items():
    print(value['question'])
    answer = input("Answer?")

    if answer.lower() ==value['answer'].lower():
        print('Correct')
        score = score +1
        print("Your score is: "+ str(score))

    else:
        print("Wrong")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score))



print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")







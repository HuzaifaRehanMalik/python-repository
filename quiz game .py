

questions = [
    "Who is the founder of Pakistan",
    "What is the capital of Pakistan",
    "What is the biggest city of Pakistan "
    ]
options = [
    ("a.  Quaid-e-Azam Muhammad Ali Jinnah", "b. Allama Iqbal", "c. Liaquat Ali Khan", "d. Benazir Bhutto"),
    ("a. Karachi", "b. Islamabad", "c. Lahore", "d. Multan"),
    ("a. Karachi", "b. Islamabad", "c. Lahore", "d. Multan")
    ]

answeres = ["a","b","a"]


guesses=[]

score = 0

question_number=0



for question in questions:
        print(question)
        for option in options[question_number]:
            print(option)
        
        guess=input("enter (a,b,c,d):").lower()
        guesses.append(guess)
        if guess == answeres[question_number]:
            score+=1
            print("right!") 
            print("You score is",score)
        else:
            print("Wrong!") 
            print(f"{answeres[question_number]} is right answere")
           
        
        question_number +=1
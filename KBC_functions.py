import random
life_count = 0
life_used={
    'A':False,
    'B':False,
    'C':False,
    'D':False
}
def random_cho(arg):
    ind = random.randrange(len(arg))
    que = arg[ind]
    return ind,que

def fifty_fifty(question):
    correct=question['answer']
    correct1=f"{correct}){question['options1'][correct]}"
    wrong_options=[f"{key}) {value}" for key , value in question['options1'].items() if key!=correct]
    wrong=random.choice(wrong_options)
    print(wrong,correct1)

def audience_poll(question):
    max_poll=[32,34,46,46,41,39,45,35,56,51,47]
    rand_poll=random.choice(max_poll)
    remaining=100-rand_poll
    cuts=sorted(random.sample(range(1,remaining),2))
    poll1=cuts[0]
    poll2=cuts[1]-cuts[0]
    poll3=remaining-cuts[1]
    poll_list=[poll1,poll2,poll3]
    random.shuffle(poll_list)
    correct=question['answer']
    incorrect=[key for key in question['options1'] if key !=correct]
    votes={correct:rand_poll}
    for i in range(len(incorrect)):
        votes[incorrect[i]]=poll_list[i]
    for key in question['options1']:
        print(f"audience poll for {key}) {question['options1'][key]} is {votes[key]}%")

def double_dip(question):
    print("you got two chances for answer correctly")
    print("choose your option")
    user = input()
    user = user.upper()
    if user == question['answer']:
        print("this was first attempt and --------->")
        return True
    else:
        print("this was first attempt and ------------>")
        return False

def expert_advice(question):
    print("you choose to take expert advice")
    print("our experts read the question carefully\nafter thinking about the question asked,our expert suggests you to go with the option",question['answer'])

def life_line():
    global life_used,life_count
    choice = input("\ndo you want to choose life line??\nenter 'yes' or 'no' : ")
    choice = choice.upper()
    if choice=="YES" :
        if life_count >=4:
            print("you have used all your life lines ")
        else:
            print(f"life line remaining : {4 - life_count}")
            print("which lifeline do want to choose ")
            print("->50-50\n->audience poll\n->double dip\n->expert advice")
            choice1 = input("Enter A for 50-50\nEnter B for audience poll\nEnter C for double dip\nEnter D for expert advice\n")
            choice1 = choice1.upper()
            if life_used[choice1]:
                print("you have already used this lifeline")
                choice1 = input("choose another life line print\n->50-50\n->audience poll\n->double dip\n->expert advice\n")
                choice1 = choice1.upper()
                return 0
            life_used[choice1] = True
            life_count += 1
            if choice1 == "A":
                return 1
            elif choice1 == "B":
                return 2
            elif choice1 == "C":
                return 3
            elif choice1 == "D":
                return 4
            else:
                print("type correctly")
    else:
        print("enter your option")
        return 0
def difficulty_f(difficulty,level_list):
    print(f"you have chosen {difficulty} level !")
    print("let's start the game 'who is going to be billionaire' ")
    for i in range (5):
            level=level_list[i]
            idx,ques = random_cho(level)
            print(f"\n{ques['question']}")
            print(f"\n{ques['options']}")
            num = life_line()
            if num == 0:
                print("you did not choosed any  life line!")
            elif num == 1:
                fifty_fifty(ques)
            elif num==2:
                audience_poll(ques)
            elif num==3:
                val=double_dip(ques)
                if val==True:
                    print("your guess is correct")
                elif val==False:
                    print("your guess is incorrect! \ngo for your second attempt")
            elif num==4:
                expert_advice(ques)
            user_input=input()
            user_input=user_input.upper()
            if user_input==ques['answer']:
                print("WOW!\nyour answer is correct")
            else :
                print (f"your answer is wrong \nyou were able to answer correctly upto question{i}")
                right_ans = ques['answer']
                print(f"The correct answer was {right_ans}){ques['options1'][right_ans]}")
                break
            count = i
    if count == 4:
        print("\nCONGRATULATIONS! you managed to clear all five levels correctly\nit's bit unexpected but you are good at playing this game")

print("hello user! wellcome to KBC game ")
print("before starting the Game let me tell you some rules and instructions--->")
print("->you have to complete 5 levels in the difficulty you chose to win this game , each next level will be harder then the previous one")
print("->you will be given four lifelines")
print("\n 1)50-50 \n 2)audience poll\n 3)double dip\n 4)phone a friend\n you can choose any lifeline you want and you can choose maximum of 1 lifelines for each level")
print("With this lets start the Game and see what you have to got !")
print("there are three difficulty level:-\nA)easy\nB)medium\nC)extreme")
opt=["A","B","C"]
difficulty=input("Choose the difficulty level\n")
difficulty=difficulty.upper()

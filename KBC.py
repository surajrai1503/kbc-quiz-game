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
    print("our experts read the question carefully\nOur expert suggests you to go with the option",question['answer'])

def life_line():
    global life_used,life_count
    choice = input("do you want to choose life line??\nenter 'yes' or 'no' : ")
    choice = choice.upper()
    if choice=="YES" :
        if life_count >=4:
            print("you have used all your life lines ")
        else:
            print(f"life line remaing : {4 - life_count}")
            print("which lifeline do want to choose ")
            print("->50-50\n->audiance poll\n->double dip\n->expert advice")
            choice1 = input(
                "Enter A for 50-50\nEnter B for audiance poll\nEnter C for double dip\nEnter D for expert advice\n")
            choice1 = choice1.upper()
            if life_used[choice1]:
                print("you have already used this lifeline")
                choice1 = input("choose another life line print\n->50-50\n->audiance poll\n->double dip\n->expert advice\n")
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
            print(ques['question'])
            print(ques['options'])
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
                print("WOW!\n your answer is correct")
            else :
                print (f"your answer is wrong \nyou were able to answer correctly upto question{i}")
                right_ans = ques['answer']
                print(f"The correct answer was {right_ans}){ques['options1'][right_ans]}")
                break
            count = i
    if count == 4:
        print("CONGRATULATIONS! you answered all ten questions are correctly")

print("hello user! wellcome to KBC game ")
print("before starting the Game let me tell you some rules and instructions--->")
print("->you can choose between three difficulties :- ")
print("->you have to complete 5 levels in the difficulty you chose to win this game , each next level will be harder then the previous one")
print("->you will be given four lifelines")
print("\n1)50-50\n2)audience poll\n3)double dip\n4)phone a friend\nyou can choose any lifeline you want and you can choose maximum of 1 lifelines for each level")
print("With this lets start the Game and see what you have to got !")
print("there are three difficulty level:-\nA)easy\nB)medium\nC)extreme")
opt=["A","B","C"]
difficulty=input("Choose the difficulty level\n")
difficulty=difficulty.upper()
if difficulty=="A":
    level1 = [{
        'question': 'Q1. Which planet is known as the Red Planet?',
        'options1': {'A': 'Venus','B': 'Mars', 'C': 'Jupiter', 'D': 'Saturn'},
        'options': 'A) Venus   B) Mars   C) Jupiter  D) Saturn',
        'answer': 'B'
    },{
        'question': 'Q1. How many days are there in a leap year?',
        'options1': {'A': '364' ,  'B': '365' ,  'C': '366'  , 'D': '367'},
        'options': 'A) 364   B) 365   C) 366   D) 367',
        'answer': 'C'
    },{
        'question': 'Q1. What is the capital of France?',
        'options1': {'A': 'Berlin','B': 'Madrid','C':'Paris','D': 'Rome'},
        'options': 'A) Berlin   B) Madrid   C) Paris   D) Rome',
        'answer': 'C'
    },{
        'question': 'Q1. Which animal is known as the Ship of the Desert?',
        'options1': {'A':'Horse','B':'Camel','C':'Elephant',' D':' Donkey'},
        'options': 'A) Horse   B) Camel   C) Elephant   D) Donkey',
        'answer': 'B'
    },{
        'question': 'Q1. What color do you get by mixing blue and yellow?',
        'options1': {'A':'Purple','B':' Orange','C':'Green','D':'Brown'},
        'options': 'A) Purple   B) Orange   C) Green   D) Brown',
        'answer': 'C'
    }]
    level2 = [{
        'question': 'Q2. How many legs does a spider have?',
        'options1': {'A':'6','B':'8','C':'10','D':'12'},
        'options': 'A) 6   B) 8   C) 10   D) 12',
        'answer': 'B'
    },{
        'question': 'Q2. Which is the largest ocean on Earth?',
        'options1': {'A':'Atlantic','B':'Indian','C':'Arctic','D':'Pacific'},
        'options': 'A) Atlantic   B) Indian   C) Arctic   D) Pacific',
        'answer': 'D'
    },{
        'question': 'Q2. What is the freezing point of water in Celsius?',
        'options1': {'A':'0','B':'10','C':'32','D':'100'},
        'options': 'A) 0   B) 10   C) 32   D) 100',
        'answer': 'A'
    },{
        'question': 'Q2. Which fruit is known as the King of Fruits?',
        'options1': {'A':'Mango','B':'Banana','C':'Apple','D)': 'Grapes'},
        'options': 'A) Mango   B) Banana   C) Apple   D) Grapes',
        'answer': 'A'
    },{
        'question': 'Q2. How many players are there in a cricket team?',
        'options1': {'A':'9','B':'10','C':'11','D':'12'},
        'options': 'A) 9   B) 10   C) 11   D) 12',
        'answer': 'C'
    }]
    level3 = [{
        'question': 'Q3. Who wrote the national anthem of India, Jana Gana Mana?',
        'options1': {'A':'Bankim Chandra','B':'Rabindranath Tagore','C':' Sarojini Naidu','D':'Subhas Chandra Bose'},
        'options': 'A) Bankim Chandra   B) Rabindranath Tagore   C) Sarojini Naidu   D) Subhas Chandra Bose',
        'answer': 'B'
    },{
        'question': 'Q3. Which is the longest river in the world?',
        'options1': {'A':'Amazon','B':'Nile','C':'Yangtze','D':'Mississippi'},
        'options': 'A) Amazon   B) Nile   C) Yangtze   D) Mississippi',
        'answer': 'B'
    },{
        'question': 'Q3. What is the national bird of India?',
        'options1': {'A':'Parrot','B':'Sparrow','C':' Peacock',' D': 'Eagle'},
        'options': 'A) Parrot   B) Sparrow   C) Peacock   D) Eagle',
        'answer': 'C'
    },{
        'question': 'Q3. Which gas do plants absorb from the atmosphere for photosynthesis?',
        'options1': {'A':'Oxygen','B':'Nitrogen','C':'Carbon Dioxide','D':'Hydrogen'},
        'options': 'A) Oxygen   B) Nitrogen   C) Carbon Dioxide   D) Hydrogen',
        'answer': 'C'
    },{
        'question': 'Q3. Who painted the Mona Lisa?',
        'options1': {'A':'Vincent van Gogh','B':'Pablo Picasso','C':'Leonardo da Vinci','D':' Michelangelo'},
        'options': 'A) Vincent van Gogh   B) Pablo Picasso   C) Leonardo da Vinci   D) Michelangelo',
        'answer': 'C'
    }]
    level4 = [{
        'question': 'Q4. Which is the smallest planet in our solar system?',
        'options1': {'A': 'Mars', 'B': 'Mercury', 'C': 'Venus', 'D': 'Pluto'},
        'options': 'A) Mars   B) Mercury   C) Venus   D) Pluto',
        'answer': 'B'
    }, {
        'question': 'Q4. What is the currency of Japan?',
        'options1': {'A': 'Yuan', 'B': 'Won ', 'C': 'Yen', 'D': 'Ringgit'},
        'options': 'A) Yuan   B) Won   C) Yen   D) Ringgit',
        'answer': 'C'
    }, {
        'question': 'Q4. Which organ in the human body is primarily responsible for pumping blood?',
        'options1': {'A': 'Lungs', 'B': 'Brain', 'C': 'Heart', 'D': ' Liver'},
        'options': 'A) Lungs   B) Brain   C) Heart   D) Liver',
        'answer': 'C'
    }, {
        'question': 'Q4. In which continent is the Sahara Desert located?',
        'options1': {'A': 'Asia', 'B': 'Africa', 'C': 'Australia', 'D': ' South America'},
        'options': 'A) Asia   B) Africa   C) Australia   D) South America',
        'answer': 'B'
    }, {
        'question': 'Q4. Which sport is associated with the term Grand Slam?',
        'options1': {'A': 'Football', 'B': 'Cricket', 'C': 'Tennis', 'D': 'Hockey'},
        'options': 'A) Football   B) Cricket   C) Tennis   D) Hockey',
        'answer': 'C'
    }]

    level5 = [{
        'question': 'Q5. Who was the first President of India?',
        'options1': {'A': 'Jawaharlal Nehru', 'B': 'Dr. Rajendra Prasad', 'C': 'Sardar Patel',
                     'D': 'Dr. APJ Abdul Kalam'},
        'options': 'A) Jawaharlal Nehru   B) Dr. Rajendra Prasad   C) Sardar Patel   D) Dr. APJ Abdul Kalam',
        'answer': 'B'
    }, {
        'question': 'Q5. Which country gifted the Statue of Liberty to the USA?',
        'options1': {'A': 'United Kingdom', 'B': 'Spain', 'C': 'France', 'D': 'Germany'},
        'options': 'A) United Kingdom   B) Spain   C) France   D) Germany',
        'answer': 'C'
    }, {
        'question': 'Q5. What is the chemical symbol for gold?',
        'options1': {'A': 'Go', 'B': 'Gd', 'C': 'Au', 'D': 'Ag'},
        'options': 'A) Go   B) Gd   C) Au   D) Ag',
        'answer': 'C'
    }, {
        'question': 'Q5. Which is the tallest mountain in the world?',
        'options1': {'A': 'K2', 'B': 'Kangchenjunga', 'C': 'Mount Everest', 'D': 'Nanga Parbat'},
        'options': 'A) K2   B) Kangchenjunga   C) Mount Everest   D) Nanga Parbat',
        'answer': 'C'
    }, {
        'question': 'Q5. How many strings does a standard guitar have?',
        'options1': {'A': '4', 'B': '5', 'C': '6', 'D': '7'},
        'options': 'A) 4   B) 5   C) 6   D) 7',
        'answer': 'C'
    }]
    difficulty_f("EASY",[level1,level2,level3,level4,level5])
elif difficulty=="B":
    level1 = [{
        'question': 'Q1. Which Indian state has the longest coastline?',
        'options1': {'A': 'Tamil Nadu', 'B': 'Andhra Pradesh', 'C': 'Gujarat', 'D': 'Kerala'},
        'options': 'A) Tamil Nadu   B) Andhra Pradesh   C) Gujarat   D) Kerala',
        'answer': 'C'
    }, {
        'question': 'Q1. Who was the first man to step on the Moon?',
        'options1': {'A': 'Buzz Aldrin', 'B': 'Yuri Gagarin', 'C': 'Neil Armstrong', 'D': 'John Glenn'},
        'options': 'A) Buzz Aldrin   B) Yuri Gagarin   C) Neil Armstrong   D) John Glenn',
        'answer': 'C'
    }, {
        'question': 'Q1. What is the SI unit of electric current?',
        'options1': {'A': 'Volt', 'B': 'Watt', 'C': 'Ampere', 'D': 'Ohm'},
        'options': 'A) Volt   B) Watt   C) Ampere   D) Ohm',
        'answer': 'C'
    }, {
        'question': 'Q1. Which dynasty built the Ajanta and Ellora caves?',
        'options1': {'A': 'Mauryan', 'B': 'Gupta', 'C': 'Vakataka and Chalukya', 'D': 'Chola'},
        'options': 'A) Mauryan   B) Gupta   C) Vakataka and Chalukya   D) Chola',
        'answer': 'C'
    }, {
        'question': 'Q1. What is the term for a group of lions called?',
        'options1': {'A': 'Herd', 'B': 'Pack', 'C': 'Pride', 'D': 'Flock'},
        'options': 'A) Herd   B) Pack   C) Pride   D) Flock',
        'answer': 'C'
    }]

    level2 = [{
        'question': "Q2. Which country is known as the 'Land of the Rising Sun'?",
        'options1': {'A': 'China', 'B': 'South Korea', 'C': 'Japan', 'D': 'Thailand'},
        'options': 'A) China   B) South Korea   C) Japan   D) Thailand',
        'answer': 'C'
    }, {
        'question': "Q2. Who composed India's national song 'Vande Mataram'?",
        'options1': {'A': 'Rabindranath Tagore', 'B': 'Bankim Chandra Chattopadhyay', 'C': 'Muhammad Iqbal',
                     'D': 'Sarojini Naidu'},
        'options': 'A) Rabindranath Tagore   B) Bankim Chandra Chattopadhyay   C) Muhammad Iqbal   D) Sarojini Naidu',
        'answer': 'B'
    }, {
        'question': 'Q2. Which planet has the most moons in our solar system (as commonly cited)?',
        'options1': {'A': 'Jupiter', 'B': 'Saturn', 'C': 'Uranus', 'D': 'Neptune'},
        'options': 'A) Jupiter   B) Saturn   C) Uranus   D) Neptune',
        'answer': 'B'
    }, {
        'question': 'Q2. What is the study of fossils called?',
        'options1': {'A': 'Archaeology', 'B': 'Paleontology', 'C': 'Anthropology', 'D': 'Geology'},
        'options': 'A) Archaeology   B) Paleontology   C) Anthropology   D) Geology',
        'answer': 'B'
    }, {
        'question': "Q2. Which Indian sportsperson is known as the 'Flying Sikh'?",
        'options1': {'A': 'Kapil Dev', 'B': 'Milkha Singh', 'C': 'P.T. Usha', 'D': 'Abhinav Bindra'},
        'options': 'A) Kapil Dev   B) Milkha Singh   C) P.T. Usha   D) Abhinav Bindra',
        'answer': 'B'
    }]

    level3 = [{
        'question': 'Q3. Which battle marked the beginning of British rule in India?',
        'options1': {'A': 'Battle of Buxar', 'B': 'Battle of Panipat', 'C': 'Battle of Plassey',
                     'D': 'Battle of Wandiwash'},
        'options': 'A) Battle of Buxar   B) Battle of Panipat   C) Battle of Plassey   D) Battle of Wandiwash',
        'answer': 'C'
    }, {
        'question': 'Q3. What is the hardest naturally occurring substance on Earth?',
        'options1': {'A': 'Gold', 'B': 'Iron', 'C': 'Diamond', 'D': 'Platinum'},
        'options': 'A) Gold   B) Iron   C) Diamond   D) Platinum',
        'answer': 'C'
    }, {
        'question': 'Q3. Which organ produces insulin in the human body?',
        'options1': {'A': 'Liver', 'B': 'Kidney', 'C': 'Pancreas', 'D': 'Stomach'},
        'options': 'A) Liver   B) Kidney   C) Pancreas   D) Stomach',
        'answer': 'C'
    }, {
        'question': "Q3. Who wrote the play 'Romeo and Juliet'?",
        'options1': {'A': 'Christopher Marlowe', 'B': 'William Shakespeare', 'C': 'John Milton',
                     'D': 'Charles Dickens'},
        'options': 'A) Christopher Marlowe   B) William Shakespeare   C) John Milton   D) Charles Dickens',
        'answer': 'B'
    }, {
        'question': 'Q3. Which is the smallest bone in the human body?',
        'options1': {'A': 'Femur', 'B': 'Stapes', 'C': 'Tibia', 'D': 'Radius'},
        'options': 'A) Femur   B) Stapes   C) Tibia   D) Radius',
        'answer': 'B'
    }]

    level4 = [{
        'question': "Q4. Which Indian city is called the 'Pink City'?",
        'options1': {'A': 'Udaipur', 'B': 'Jodhpur', 'C': 'Jaipur', 'D': 'Bikaner'},
        'options': 'A) Udaipur   B) Jodhpur   C) Jaipur   D) Bikaner',
        'answer': 'C'
    }, {
        'question': "Q4. What does 'GDP' stand for in economics?",
        'options1': {'A': 'General Domestic Product', 'B': 'Gross Domestic Product', 'C': 'Global Development Plan',
                     'D': 'Gross Development Product'},
        'options': 'A) General Domestic Product   B) Gross Domestic Product   C) Global Development Plan   D) Gross Development Product',
        'answer': 'B'
    }, {
        'question': 'Q4. Which is the largest gland in the human body?',
        'options1': {'A': 'Thyroid', 'B': 'Liver', 'C': 'Pituitary', 'D': 'Pancreas'},
        'options': 'A) Thyroid   B) Liver   C) Pituitary   D) Pancreas',
        'answer': 'B'
    }, {
        'question': 'Q4. Who was the founder of the Maurya Empire?',
        'options1': {'A': 'Ashoka', 'B': 'Bindusara', 'C': 'Chandragupta Maurya', 'D': 'Chanakya'},
        'options': 'A) Ashoka   B) Bindusara   C) Chandragupta Maurya   D) Chanakya',
        'answer': 'C'
    }, {
        'question': 'Q4. Which country is the largest producer of coffee in the world?',
        'options1': {'A': 'Colombia', 'B': 'Vietnam', 'C': 'Brazil', 'D': 'Ethiopia'},
        'options': 'A) Colombia   B) Vietnam   C) Brazil   D) Ethiopia',
        'answer': 'C'
    }]

    level5 = [{
        'question': 'Q5. Which Indian classical dance form originated in Tamil Nadu?',
        'options1': {'A': 'Kathak', 'B': 'Odissi', 'C': 'Bharatanatyam', 'D': 'Kuchipudi'},
        'options': 'A) Kathak   B) Odissi   C) Bharatanatyam   D) Kuchipudi',
        'answer': 'C'
    }, {
        'question': 'Q5. What is the term for the fear of heights?',
        'options1': {'A': 'Claustrophobia', 'B': 'Acrophobia', 'C': 'Arachnophobia', 'D': 'Agoraphobia'},
        'options': 'A) Claustrophobia   B) Acrophobia   C) Arachnophobia   D) Agoraphobia',
        'answer': 'B'
    }, {
        'question': 'Q5. Which treaty ended the First World War?',
        'options1': {'A': 'Treaty of Paris', 'B': 'Treaty of Versailles', 'C': 'Treaty of Vienna',
                     'D': 'Treaty of Rome'},
        'options': 'A) Treaty of Paris   B) Treaty of Versailles   C) Treaty of Vienna   D) Treaty of Rome',
        'answer': 'B'
    }, {
        'question': 'Q5. Who discovered penicillin?',
        'options1': {'A': 'Louis Pasteur', 'B': 'Alexander Fleming', 'C': 'Robert Koch', 'D': 'Edward Jenner'},
        'options': 'A) Louis Pasteur   B) Alexander Fleming   C) Robert Koch   D) Edward Jenner',
        'answer': 'B'
    }, {
        'question': 'Q5. Which is the second-largest continent by area?',
        'options1': {'A': 'Asia', 'B': 'Africa', 'C': 'North America', 'D': 'South America'},
        'options': 'A) Asia   B) Africa   C) North America   D) South America',
        'answer': 'B'
    }]
    difficulty_f("MEDIUM", [level1, level2, level3, level4, level5])

elif difficulty=="C":

    level1 = [{
        'question': 'Q1. Which subatomic particle was discovered by J.J. Thomson?',
        'options1': {'A': 'Proton', 'B': 'Neutron', 'C': 'Electron', 'D': 'Positron'},
        'options': 'A) Proton   B) Neutron   C) Electron   D) Positron',
        'answer': 'C'
    }, {
        'question': 'Q1. What is the term for government by the wealthy called?',
        'options1': {'A': 'Aristocracy', 'B': 'Plutocracy', 'C': 'Meritocracy', 'D': 'Theocracy'},
        'options': 'A) Aristocracy   B) Plutocracy   C) Meritocracy   D) Theocracy',
        'answer': 'B'
    }, {
        'question': 'Q1. Which Indian mathematician is credited with the concept of zero?',
        'options1': {'A': 'Bhaskara', 'B': 'Aryabhata', 'C': 'Brahmagupta', 'D': 'Ramanujan'},
        'options': 'A) Bhaskara   B) Aryabhata   C) Brahmagupta   D) Ramanujan',
        'answer': 'C'
    }, {
        'question': 'Q1. Which country was formerly known as Rhodesia?',
        'options1': {'A': 'Zambia', 'B': 'Zimbabwe', 'C': 'Malawi', 'D': 'Botswana'},
        'options': 'A) Zambia   B) Zimbabwe   C) Malawi   D) Botswana',
        'answer': 'B'
    }, {
        'question': 'Q1. What is the study of handwriting analysis called?',
        'options1': {'A': 'Graphology', 'B': 'Calligraphy', 'C': 'Typography', 'D': 'Paleography'},
        'options': 'A) Graphology   B) Calligraphy   C) Typography   D) Paleography',
        'answer': 'A'
    }]

    level2 = [{
        'question': 'Q2. Which gas is primarily responsible for the depletion of the ozone layer?',
        'options1': {'A': 'Carbon Dioxide', 'B': 'Methane', 'C': 'Chlorofluorocarbons', 'D': 'Sulfur Dioxide'},
        'options': 'A) Carbon Dioxide   B) Methane   C) Chlorofluorocarbons   D) Sulfur Dioxide',
        'answer': 'C'
    }, {
        'question': 'Q2. Who was the first Governor-General of independent India?',
        'options1': {'A': 'Lord Mountbatten', 'B': 'C. Rajagopalachari', 'C': 'Lord Wavell', 'D': 'Warren Hastings'},
        'options': 'A) Lord Mountbatten   B) C. Rajagopalachari   C) Lord Wavell   D) Warren Hastings',
        'answer': 'A'
    }, {
        'question': 'Q2. Which is the longest highway in India (by common reference)?',
        'options1': {'A': 'NH 44', 'B': 'NH 48', 'C': 'NH 27', 'D': 'NH 16'},
        'options': 'A) NH 44   B) NH 48   C) NH 27   D) NH 16',
        'answer': 'A'
    }, {
        'question': 'Q2. Which ancient civilization built Machu Picchu?',
        'options1': {'A': 'Aztec', 'B': 'Maya', 'C': 'Inca', 'D': 'Olmec'},
        'options': 'A) Aztec   B) Maya   C) Inca   D) Olmec',
        'answer': 'C'
    }, {
        'question': "Q2. What is the term for the boundary of a lunar or solar eclipse's total shadow?",
        'options1': {'A': 'Penumbra', 'B': 'Umbra', 'C': 'Antumbra', 'D': 'Corona'},
        'options': 'A) Penumbra   B) Umbra   C) Antumbra   D) Corona',
        'answer': 'B'
    }]

    level3 = [{
        'question': 'Q3. Which Indian freedom fighter founded the Indian National Army (INA)?',
        'options1': {'A': 'Bhagat Singh', 'B': 'Subhas Chandra Bose', 'C': 'Chandrashekhar Azad',
                     'D': 'Lala Lajpat Rai'},
        'options': 'A) Bhagat Singh   B) Subhas Chandra Bose   C) Chandrashekhar Azad   D) Lala Lajpat Rai',
        'answer': 'B'
    }, {
        'question': 'Q3. What is the term for an abnormal fear of enclosed spaces?',
        'options1': {'A': 'Acrophobia', 'B': 'Agoraphobia', 'C': 'Claustrophobia', 'D': 'Xenophobia'},
        'options': 'A) Acrophobia   B) Agoraphobia   C) Claustrophobia   D) Xenophobia',
        'answer': 'C'
    }, {
        'question': 'Q3. Which physicist proposed the uncertainty principle?',
        'options1': {'A': 'Niels Bohr', 'B': 'Werner Heisenberg', 'C': 'Max Planck', 'D': 'Erwin Schrodinger'},
        'options': 'A) Niels Bohr   B) Werner Heisenberg   C) Max Planck   D) Erwin Schrodinger',
        'answer': 'B'
    }, {
        'question': 'Q3. Which Indian state has Thiruvananthapuram as its capital?',
        'options1': {'A': 'Tamil Nadu', 'B': 'Karnataka', 'C': 'Kerala', 'D': 'Andhra Pradesh'},
        'options': 'A) Tamil Nadu   B) Karnataka   C) Kerala   D) Andhra Pradesh',
        'answer': 'C'
    }, {
        'question': "Q3. Who wrote the 'Arthashastra'?",
        'options1': {'A': 'Kalidasa', 'B': 'Chanakya (Kautilya)', 'C': 'Panini', 'D': 'Patanjali'},
        'options': 'A) Kalidasa   B) Chanakya (Kautilya)   C) Panini   D) Patanjali',
        'answer': 'B'
    }]

    level4 = [{
        'question': 'Q1. Which country has the longest coastline in the world?',
        'options1': {'A': 'Russia', 'B': 'Canada', 'C': 'Indonesia', 'D': 'Australia'},
        'options': 'A) Russia   B) Canada   C) Indonesia   D) Australia',
        'answer': 'B'
    }, {
        'question': 'Q2. What is the term for the process by which plants lose water vapor?',
        'options1': {'A': 'Respiration', 'B': 'Transpiration', 'C': 'Photosynthesis', 'D': 'Evaporation'},
        'options': 'A) Respiration   B) Transpiration   C) Photosynthesis   D) Evaporation',
        'answer': 'B'
    }, {
        'question': "Q3. Which Mughal emperor authored his own memoir, the 'Baburnama'?",
        'options1': {'A': 'Humayun', 'B': 'Akbar', 'C': 'Babur', 'D': 'Jahangir'},
        'options': 'A) Humayun   B) Akbar   C) Babur   D) Jahangir',
        'answer': 'C'
    }, {
        'question': 'Q4. Which country was the first to grant women the right to vote?',
        'options1': {'A': 'United States', 'B': 'United Kingdom', 'C': 'New Zealand', 'D': 'France'},
        'options': 'A) United States   B) United Kingdom   C) New Zealand   D) France',
        'answer': 'C'
    }, {
        'question': 'Q5. What is the name of the theory that explains the origin of the universe?',
        'options1': {'A': 'Steady State Theory', 'B': 'Big Bang Theory', 'C': 'String Theory', 'D': 'Inflation Theory'},
        'options': 'A) Steady State Theory   B) Big Bang Theory   C) String Theory   D) Inflation Theory',
        'answer': 'B'
    }]

    level5 = [{
        'question': "Q1. Which Indian ruler is known for the 'Doctrine of Lapse'?",
        'options1': {'A': 'Robert Clive', 'B': 'Lord Dalhousie', 'C': 'Warren Hastings', 'D': 'Lord Curzon'},
        'options': 'A) Robert Clive   B) Lord Dalhousie   C) Warren Hastings   D) Lord Curzon',
        'answer': 'B'
    }, {
        'question': 'Q2. What is the term for a triangle with all sides of different lengths?',
        'options1': {'A': 'Isosceles', 'B': 'Equilateral', 'C': 'Scalene', 'D': 'Right-angled'},
        'options': 'A) Isosceles   B) Equilateral   C) Scalene   D) Right-angled',
        'answer': 'C'
    }, {
        'question': 'Q3. Which scientist formulated the periodic table of elements?',
        'options1': {'A': 'Antoine Lavoisier', 'B': 'Dmitri Mendeleev', 'C': 'John Dalton', 'D': 'Marie Curie'},
        'options': 'A) Antoine Lavoisier   B) Dmitri Mendeleev   C) John Dalton   D) Marie Curie',
        'answer': 'B'
    }, {
        'question': 'Q4. Which Indian classical text is considered the oldest of the four Vedas?',
        'options1': {'A': 'Yajurveda', 'B': 'Samaveda', 'C': 'Rigveda', 'D': 'Atharvaveda'},
        'options': 'A) Yajurveda   B) Samaveda   C) Rigveda   D) Atharvaveda',
        'answer': 'C'
    }, {
        'question': 'Q5. Who was the Roman general defeated by Julius Caesar in the civil war?',
        'options1': {'A': 'Mark Antony', 'B': 'Pompey', 'C': 'Crassus', 'D': 'Brutus'},
        'options': 'A) Mark Antony   B) Pompey   C) Crassus   D) Brutus',
        'answer': 'B'
    }]
    difficulty_f("EXTREME", [level1, level2, level3, level4, level5])
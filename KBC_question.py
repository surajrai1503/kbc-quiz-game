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
    }]
    difficulty_f("EXTREME", [level1, level2, level3, level4, level5])
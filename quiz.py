# Three point on first attempt
# Attempting all quiz bonus
# Login
# Rules
# Quit

password = '1234Pass'
trials = 3
logged_in = False
while trials > 0:
    login_password = input('Input your password: ')
    if login_password == password:
        print('Log in successful')
        logged_in = True
        break
    else:
        print('Wrong password.')
        trials -= 1

else:
    print('Account compromised, Contact your manager')

if logged_in:
    question_set = input("""
Select your pair of questions?
    1. Football
    2. Crypto
    3. Politics
    4. Health
    5. All
""")
    if int(question_set) == 1:
        print('Welcome to sports world')
        print("Where is the 2022, World cup held ")  # Qatar
        print("Which team is Cristiano Ronaldo in the world cup playing for? ")  # portugal
        print('When will the next world cup be held')  # 2026
        print('How long does first half last(Not considering the extra time)')  # 45 min
        print('Each team playing in a pitch requires 11 players')  # true

    elif int(question_set) == 2:
        print('Welcome to Crypto space')
        print("Which crypto has the largest market cap")  # bitcoin
        print("What is bitcoin ticket symbol")  # BTC
        print('Ethereum is the second worlds market cap cryptocurrency')  # True
        print('How many cryptocurrencies are there currently')  # range   21,910 +
        print('Cryptocurrency was first introduced in 2018. True or False')  # False

    elif int(question_set) == 3:
        print('Politics leads the world')
        print("Current president of USA")  # Joe Biden
        print("Elections in the usa is done after every ___ years")  # 4 Years
        print('USA is made of how many states')  # 52
        print('What does NATO stand for?')  # North Atlantic Treaty Organization
        print('What country is the world’s largest democracy?')  # India

    elif int(question_set) == 4:
        print('All lives depends on Health and healthy living')
        print("How much water do we need daily (in litters)?")  # 2 liters
        print('Corona was first discovered in the year')  # Nov. 17, 2019,
        print("Its advisable to avoid unhealthy foods. True or False")  # True
        print("""
        The following foods are unhealthy except.
        A. Deep Fried Foods
        B. Fast Food
        C. Excess Candy
        D. Dark Green Vegetables and surplus water
        """)  # D
        print('What is WHO in full')  # World Health Organisation

    elif int(question_set) == 5:
        # Execute all questions 1-4 in order
        pass

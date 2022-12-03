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
    if int(question_set)==1:
        print('Welcome to sports world')
        print("Where is the 2022, World cup held ")
        print("Which team is cristiano Ronaldo playing for? ")
        print('When will the next world cup be held')
        print('How long does first half last(Not considering the extra time)')
        print('Each team playing in a pitch requires 11 players')

    elif int(question_set) == 2:
        print('Welcome to Crypto space')
        print("Which crypto has the largest market cap")
        print("What is bitcoin ticket symbol")
        print('Ethereum is the second worlds market cap cryptocurrency')
        print('How many cryptocurrencies are there currently')
        print('Cryptocurrency was first introduced in 2018. True or False')

    elif int(question_set) == 3:
        print('Politics leads the world')
        print("Current president of USA")
        print("Elections in the usa is done after every ___ years")
        print('USA is made of how many states')
        print('What does NATO stand for?')
        print('What country is the world’s largest democracy?')

    elif int(question_set) == 4:
        print('All lives depends on Health and healthy living')
        print("How much water do we need daily (in litters)?")
        print('Corona was first discovered in the year')
        print("Its advisable to avoid unhealthy foods. True or False")
        print("""
        The following foods are unhealthy except.
        Deep Fried Foods
        Fast Food
        Excess Candy
        Dark Green Vegetables and surplus water
        """)
        print('What is WHO in full')

    elif int(question_set) == 5:
        print('Welcome to Crypto space')
        print("Which crypto has the largest market cap")
        print("What is bitcoin ticket symbol")
        print('Ethereum is the second worlds market cap cryptocurrency')
        print('How many cryptocurrencies are there currently')
        print('Cryptocurrency was first introduced in 2018. True or False')
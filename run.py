
def getInput(prompt="", cast=None, condition=None, errorMessage=None):
    """
    Valdiates our the user input
    """
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except:
            print(errorMessage or "Invalid input, Try again")


def dataCollection():
    """
    Takes input from user and puts it in a list
    """

    data = []
    age = getInput(
        prompt="Enter your age:\n",
        cast=int,
        condition=lambda x: x > 18,
        errorMessage="You have to be above 18")
    done = False 
    while not done:
        print("""
        Your gender
        (1)Male
        (2)Female
        """)

        sex = getInput(
            prompt="Choose your gender:\n",
            cast=int,
            condition=lambda x: x > 0 and x < 3,
            errorMessage= "Please type 1 for male or 2 for female")

        print("""
        Activity level
        (1) Sedentary
        (2) Light
        (3) Moderate
        (4) Active
        (5) Very Active
        """)

        activity = getInput(prompt="Choose your activity level:\n",
                            cast=int,
                            condition=lambda x: x > 0 and x < 6,
                            errorMessage="Please type in \
                                a number between 1 & 6")
        break

    weight = getInput(
        prompt="Enter your weight in kgs:\n",
        cast=float,
        condition=lambda x: x > 40,
        errorMessage="Least weight you can start with is 40kgs")

    height = getInput(
        prompt="Enter your height in cms:\n",
        cast=float, condition=lambda x: x > 100,
        errorMessage="That's not a valid height")

    data.append(sex)
    data.append(age)
    data.append(weight)
    data.append(height)
    data.append(activity)

    return data


def calories_cal(data):

    """ 
    Calculates daily calorie needs (tee)..
    1. Resting metabolic rate (rmr)
    2. Physical activity (adl) given factors 1.2 to 1.9 based on activity level
    3. Thermogenic effect of food (tef)
    """

    print(f"Calculating your estimated daily calorie needs to maintain your current weight...\n")

    age = data[1]
    weight = data[2]
    height = data[3]
    activity = data[4]

    # Calculates the resting metabolic rate

    if data[0] == 1:
        # for a male
        rmr = 10 * int(weight) + 6.25 * int(height) - 5 * int(age) + 5
    elif data[0] == 2:
        # for a female
        rmr = 10 * int(weight) + 6.25 * int(height) - 5 * int(age) - 161  

    # calculate the calorie burned based on physical activity
    if activity == 1:
        adl = rmr * 1.2    
    elif activity == 2:
        adl = rmr * 1.375
    elif activity == 3:
        adl = rmr * 1.55
    elif activity == 4:
        adl = rmr * 1.725
    elif activity == 5:
        adl = rmr * 1.9

    # thermic effect of food
    tef = (adl) * 0.1

    # tee is the totoal energy expenditure
    tee = round(tef + adl)

    print(f"Your estimated daily calorie needs to maintain your current weight is {tee}kcal\n")
    return tee


def choices():
    """
    Give options to user weather they want to lose weight, 
    gain weight 
    Calculates the new calorie intake in either a defiict or gain 
    The days it will take user to lose or gain the weight as extra information 

    """
    done = False
    while not done:

        print("""

        (1)Lose weight
        (2)Gain Weight

        """)
        
        choice = getInput(prompt="Choose an option: \n",
                          cast=int,
                          condition=lambda x: x > 0 and x < 3,
                          errorMessage="Please enter 1 or 2")
                
        data = dataCollection()
        current_cal_intake = calories_cal(data)

        if choice == 1:
            loss_goal = int(input("Enter how many kgs you would like to lose?\n"))

            print("Calculating your calorie deficit...\n")
            new_cal_intake = round(current_cal_intake - (current_cal_intake * 0.25))
            #weight to be lost in kgs in a week 
            calorie_def_week = (((current_cal_intake * 0.25) * 7) * 0.45) / 3500    
            days_it_takes = round((loss_goal * 7) / calorie_def_week)
            user_answer = print(f"You need to consume {new_cal_intake}kcal to lose {loss_goal} kgs and it will take you {days_it_takes}days.\n")

        elif choice == 2:
            gain_goal = int(input("Enter how many kgs you would like to gain?\n"))
            print("Calculating your calorie increase...\n")
            new_cal_intake = round(current_cal_intake + 1000)
            days_it_takes = round((gain_goal*7)/0.9)
            user_answer = print(f"You need to consume {new_cal_intake}kcal to gain {gain_goal} kgs and it will take you {days_it_takes}days.\n")
        
        return user_answer
        break
        
print("Welcome to Calorie Calculator\n")
print("Whether you want to gain or lose or maintain your weight, the calculator will help you to figure out the numbers\n")
choices()








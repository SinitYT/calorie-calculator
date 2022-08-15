
def getInput(prompt="",cast = None, condition= None, errorMessage=None):
    while True:
        try:
            response = (cast or str)(input(prompt))
            assert condition is None or condition(response)
            return response
        except:
            print(errorMessage or "Invalid input,Try again")

def dataCollection():

    data = []
    sex = getInput(prompt="Enter your gender(write:male or female):\n")
    age = getInput(prompt="Enter your age:\n", cast=int,condition=lambda x: x > 0)
    weight = getInput(prompt="Enter your weight in kgs:\n",cast=float,condition=lambda x: x > 0,errorMessage="That's not a valid weight")
    height = getInput(prompt="Enter your height in cms:\n", cast=float, condition=lambda x: x > 100,errorMessage="That's not a valid height")
    activity = getInput(prompt="How active are you? Type in either sedentary,light,moderate,active,very active:\n")
    
    data.append(sex)
    data.append(age)
    data.append(weight)
    data.append(height)
    data.append(activity)
    
    return data

def calories_cal(data):
    print(f"Calculating your estimated daily calorie needs to maintain your current weight as a {data[0]}")
    age = data[1]
    weight = data[2]
    height = data[3]
    activity = data[4]
    

    if data[0] == 'male' or 'm':
        rmr= 10 * int(weight)+ 6.25 * int(height) - 5 * int(age) + 5
    elif data[0] == 'female' or 'f':
        rmr= 10 * int(weight)+ 6.25 * int(height) - 5 * int(age) - 161
    

    
    if activity == 'sedentary':
        adl = rmr * 1.2
    elif activity == 'light':
        adl = rmr * 1.375
    elif activity == 'moderate':
        adl = rmr * 1.55
    elif activity == 'active':
        adl = rmr * 1.725
    elif activity == 'very active':
        adl = rmr * 1.9

    tef = ( adl) * 0.1
    
        

   
    tee = tef + adl 
    print(f"Your estimated daily calorie needs to maintain your current weight is {tee}kcal\n")
    return tee

'''Give options to user wether they want to lose weight, gain weight or how long i will take them to reach their goal'''
def choices():
    done = False
    while not done:
        print("""
        (1)Lose weight
        (2)Gain Weight
        (3)How long will it take me to lose weight
        """)
        choice = input("Choose an option: \n")
        data = dataCollection()
        current_cal_intake=calories_cal(data) 
        if choice == '1' :
            loss_goal=int(input("Enter how many kgs you would like to lose?\n"))

            print("Calculating your calorie deficit...\n")
            new_cal_intake = round(current_cal_intake - (current_cal_intake * 0.25))
            calorie_def_week = (((current_cal_intake * 0.25) * 7) * 0.45) / 3500    #weight lost in kgs
            days_it_takes = round((loss_goal * 7) / calorie_def_week)
            user_answer = print(f"You need to consume {new_cal_intake}kcal to lose {loss_goal} kgs and it will take you {days_it_takes}days.\n")

        
        elif choice == '2':
            gain_goal=int(input("Enter how many kgs you would like to gain?/n"))
            print("Calculating your calorie increase...\n")
            new_cal_intake = round(current_cal_intake + 1000)
            days_it_takes = round((gain_goal*7)/0.9 )
            user_answer = print(f"You need to consume {new_cal_intake}kcal to gain {gain_goal} kgs and it will take you {days_it_takes}days.\n")
            

        
        print(user_answer)
print(choices())







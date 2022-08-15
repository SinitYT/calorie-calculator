
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
    weight_loss = getInput(prompt="How many kgs do you want to lose?\n",cast=float)
    data.append(sex)
    data.append(age)
    data.append(weight)
    data.append(height)
    data.append(activity)
    data.append(weight_loss)
    return data




def female_calories_cal(data):
    age = data[1]
    weight = data[2]
    height = data[3]
    activity = data[4]
    weight_loss = data[5]

    if data[0] == 'female' or 'f':
        rmr= 10 * int(weight)+ 6.25 * int(height) - 5 * int(age) - 161
        adl = 0
        if activity == 'sedentary':
            adl = rmr * 1.2
        elif activity == 'light':
            adl = rmr * 1.375
        elif activity == 'moderate':
            adl = rmr * 1.55
        elif activity == 'active':
            adl = rmr * 1.725
        else:
            adl = rmr * 1.9
        tef = ( adl) * 0.1
    else:
        print("enter correct gender")
        

   
    tee = tef + adl 
    return tee






def male_calories_cal(data):
    age = data[1]
    weight = data[2]
    height = data[3]
    activity = data[4]
    weight_loss = data[5]

    if data[0] == 'male' or 'm':
        rmr= 10 * int(weight)+ 6.25 * int(height) - 5 * int(age) + 5
        adl = 0
        if activity == 'sedentary':
            adl = rmr * 1.2
        elif activity == 'light':
            adl = rmr * 1.375
        elif activity == 'moderate':
            adl = rmr * 1.55
        elif activity == 'active':
            adl = rmr * 1.725
        else:
            adl = rmr * 1.9
        tef = ( adl) * 0.1
    else:
        print("enter correct gender")
        

   
    tee = tef + adl 
    print(tee)




data = dataCollection()
female_calories_cal(data)
male_calories_cal(data)
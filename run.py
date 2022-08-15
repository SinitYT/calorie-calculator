
def get_input():
    data = []
    sex = input("Please enter your gender(write:male or female):\n")
    age = int(input("Please enter your age:\n"))
    weight = float(input("Please enter your weight in kgs:\n"))
    height = float(input("Please enter your height in cms:\n"))
    activity = input("How active are you? Type in either sedentary,light,moderate,active,very active:\n")
    weight_loss = float(input("How many kgs do you want to lose?\n"))
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
        

   
    tee = tef + adl 
    return tee


'''

if sex == 'female':
        rmr= 9.99 * int(weight)+ 6.25 * int(height) - 4.92 * int(age) + 161
    elif sex == 'male':
        rmr = 9.99 * int(weight) + 6.25 * int(height) - 4.92 * int(age) + 5
 '''
data = get_input()
female_calories_cal(data)

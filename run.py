
def rmr_calculator():
    sex = input("Please enter your gender:\n")
    age = input("Please enter your age:\n")
    weight = input("Please enter your weight in kgs:\n")
    height = input("Please enter your height in cms:\n")
    rmr = 0
    
    if sex == 'female':
        rmr= 9.99 * int(weight)+ 6.25 * int(height) - 4.92 * int(age) + 161
    else:
         rmr = 9.99 * int(weight) + 6.25 * int(height) - 4.92 * int(age) + 5

    print(f"Your RMR is {rmr}")


rmr_calculator()

   
    


 
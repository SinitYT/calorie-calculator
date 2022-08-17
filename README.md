
# Calorie Calculator

Calorie Calculator is a python terminal calculator that aids to calculate the daily calorie needs of a person whether they are trying to maintain, lose or gain weight.

## Features
* If you want to lose weight, it calculates the number of daily calories you need to consume to achieve your weight loss goal. 
* If you want to gain weight, it calculates the number of daily calories you need to consume to achieve your weight gain goal. 
* It also displays how long it will take you to reach your goal weight.

### Future features

* Add more functionality for safe weight gain instead of the fast route which is used in this instance.
* Give user the visual summary of their input and result in a form of a table.


## How to use it

* Choose weather you want to lose or gain weight by entering corresponding numbers.
* Enter your age, for accountability reasons, you have to be over 18 to use this calculator.
* Choose your gender, by entering the corresponding number.
* Choose your activity level, enter the level that applies to you by choosing corresponding number.
     * 1.2  --- No exercise
     * 1.375 --- Life style walk or 1 - 2 days/week exercise
     * 1.55 --- Moderate, 2-3 days/week exercise
     * 1.725 --- Active, 3-4 days/week exercise
     * 1.9 --- Very active, 5-6 days/week exercise or pro athlete 
* Enter your weight in kgs, again: for accountablity issues, you have to weight over 40kgs to use this calculator.
* Enter your height in cms, height has to be over 100 cms. 
* Entery the kgs you would like to gain or lose depending on your choice.

## Data Model
I chose to use the calculator presented on this  (url:https://www.forbes.com/health/body/calorie-calculator/) website as a model to imitate. 

The methodology used in this app is similar to what is used on this website except for the gain weight section. 

For the gain weight section, the extra information needed was the safte amount of calories needed to be added for gain weight, which according to this (url:https://www.omnicalculator.com/health/weight-gain) website is a minimum of 1000 kcal a day to gain 1kg a week.

* Calculator Methodlogy:
    * To maintain you current weight the calculator considers:
      1. Resting metabolic rate (RMR)
      2. Physical activity
      3. The thermogenic effect of food (the calories you burn while processing food)
    * To lose weight
      - To determine your daily calorie needs to lose weight, the calculator decreases the number  of calories you use currently by 25%, resulting in a new recommended daily calorie intake. 
    * To gain weight 
      - To determine your daily calorie needs to gain weight, the calculator increase the number  of calories you have currently by 1000, resulting in a new recommended daily calorie intake. 

## Testing
I have tested the program using the following:
* Given invalid inputs: out of bounds inputs, strs where ints are expected
* Passed it through pep8 validator and confirmed that no major problems were present
* Tested it on my terminal

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
* Create a new Heroku app
* When you create the app, you will need to add two buildpacks from the Settings tab. The ordering is as follows:

 1. heroku/python
 2. heroku/nodejs
 3. You must then create a Config Var called PORT. Set this to 8000






# UFC Fight Predictor Project

## About the Project
UFC may be the new king of the fight game, and I'm here for it. With megastars like Conor McGregor, Jorge Masvidal, Brock Lesnar, and Ronda Rousey commanding over a million PPVs each, the combat sport is cementing its place amongest the heavyweights. In the past few years the sport has undergone a transformation similar its president Dana White, going from dweeby dodgeball reject to glossy action flick star.

I can't even remember what I used to do on saturday nights, but now I crowd around the TV with my friends as we each loudly predict which fighter will win. Just when you thought UFC was for the muscle-bound monster truck bunch, you find out it is really for the nerds.

What's more nerdy that breaking down the stats and even betting money your calculations are correct.

In this project I will be creating a fight predictor so that like the UFC, I can also be king of Saturday nights.

### Project Goals
The goal of this project is to be able to read in an upcoming fight card and predict the outcome of each fight.

### Project Description:
For this particular project we will be looking at UFC 272 PPV - Colby Covington vs. Jorge Masvidal.

Colby Covington and Jorge Masvidal have a legendary fued, with the classic story of turning best friends to sworn enemies in the blink of an eye. UFC 272 will an old fashioned grudge match.

Because of this we will focus on the stats of these two fighters and how they match up against each other.

### Data Dictionary

A list of the variables in the dataframe and their meaning. 

| Variable       | Description                         |
| -------------- | ----------------------------------- |
|event_name	                | Name of the UFC event|
|fighter1 |name of the first fighter |
|fighter2 |name of the second fighter |
|outcome|fighter1, fighter2, draw, no_contest|
|win|1 = win|
|loss|1 = loss|
|draw|1 = draw|
|no_contest|1 = no contest|
|weight_f1|fighter1's weight|
|reach_f1|fighter1's reach|
|stance_f1|fighter1's stance|
|strikes_f1|fighter1's strikes|
|strike_acc_f1|fighter1's strike accuracy average|
|strikes_absorbed_f1|fighter1's strikes absorbed average|
|strike_defense_f1|fighter1's strike defense average|
|takedowns_f1|fighter1's takedown average|
|takedown_acc_f1|fighter1's takedown accuracy average|
|takedown_def_f1|fighter1's takedown defense average|
|sub_attempt_f1|fighter1's submission attempts average|
|age_days_f1|fighter1's age in days|
|age_f1|fighter1's age|
|outcome_f1|fighter1's win/loss outcome|
|height_in_f1|fighter1's height in inches|
|stance_Orthodox_f1|1 = Orthodox|
|stance_Southpaw_f1|1 = Southpaw|
|stance_Switch_f1|1 = Switch|
|weight_f2|fighter2's weight|
|reach_f2|fighter2's reach|
|stance_f2|fighter2's stance|
|strikes_f2|fighter2's strikes|
|strike_acc_f2|fighter2's strike accuracy average|
|strikes_absorbed_f2|fighter2's strikes absorbed average|
|strike_defense_f2|fighter2's strike defense average|
|takedowns_f2|fighter2's takedown average|
|takedown_acc_f2|fighter2's takedown accuracy average|
|takedown_def_f2|fighter2's takedown defense average|
|sub_attempt_f2|fighter2's submission attempts average|
|age_days_f2|fighter2's age in days|
|age_f2|fighter2's age|
|outcome_f2|fighter2's win/loss outcome|
|height_in_f1|fighter1's height in inches|
|stance_Orthodox_f2|1 = Orthodox|
|stance_Southpaw_f2|1 = Southpaw|
|stance_Switch_f2|1 = Switch|

### Steps to Reproduce

        1. You will need to import everything listed in imports used
        2. Clone this repo containing the Final_UFC_Fight_Card_predictor as well as my Wrangle_UFC.py.
        3. That should be all you need to do run the Final_UFC_Fight_Card_predictor!

### The Plan

- Wrangle
    - I want to create a df where the fighter1 and fighter2 stats are on the same row
    - To do this I'll create a column that concats the fighter1 and fighter2 columns together. I'll also do the reverse of that where the names are listed fighter2/fighter1. I'll write a for loop that prints an array of fighter1's stats and finds and prints the corresponding fighter2's stats. It will then join them together and store the data in a df.
    - Split
    - Initial Questions: 

        1) Does fighter1 having a higher striking defense average than fighter2 correlate to fighter 1 winning.

        2) Does fighter1 having a higher takedown defense average than fighter2 correlate to fighter 1 winning.

        3) How does Colby Covington and Jorge Masvidal's stats compare to the vlues with the highest correlation to winning?

        4) How does Colby Covington and Jorge Masvidal's stats compare to each other?
- Explore
    - Make new columns with the difference between the two fighter's stats
    - Do corr test to see what columns corr to the target (outcome)
    - Flush out two specific fighters to make a compelling story of what drives winning or losing
        - Covington vs Masvidal 
            - Break down their stats for their last (at least 3 fights)
            - Compare their current stats side-by-side to predict who will win their big grudge match
            - Use visuals and statits to do this
- Model
    - Scale data
    - Develop classification model that will predict the outcomes of future fight cards
        - Use the differences in stats between the two fighters and assign it to just one fighter like: fighter1 +23 average strikes, fighter1 -2 average takedown defense, etc. Then the target will be outcome (fighter1 or fighter2). The model will associate positive averages with fighter1 and negative averages with fighter2 winning.
- Refine (Report)
- Deliver
    - README.md
    - Wrangle_UFC.py
    - working notebooks
    - Trello board

## Conclusion:

In this project I found that the greatest predictors of winning are a high strike defense, takedown defense, strike accuracy, and takedown accuracy average as well as being younger than your opponent.

After comparing these stats for Covington and Masvidal I came to the conclusion that with the advantage in the first three categories and a tie in the forth, Masvidal has a better chance of winning than Covington. The only advantage Covington has according to these metrics is that he is younger by a few years.

I created a model using the features strikes_defense_diff, takedown_defense_diff, strike_acc_diff, age_diff, and takedown_acc_diff.

My model is 64 percent accurate on unseen data. With an increase from 49 to 64, I improved my model from the baseline by 30.61%

## With more time...

- Predict on fight card and add predictions to CSV.
- Scrape for most recent data. 
- Add win/loss record as a feature.
- Figure out how to add stance as a feature. 
- Once accuracy is increaed by a stisfactory amout, create a front end app that takes in two fighter and returns the predicted outcome. 

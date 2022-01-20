# UFC Fight Predictor Project

## About the Project

### Project Goals

### Data Dictionary

A list of the variables in the dataframe and their meaning. 

| Variable       | Description                         |
| -------------- | ----------------------------------- |
|                |                                     | 

### Steps to Reproduce

### The Plan

- Wrangle
    - I want to create a df where the fighter1 and fighter2 stats are on the same row
    - To do this I'll create a column that concats the fighter1 and fighter2 columns together. I'll also do the reverse of that where the names are listed fighter2/fighter1. I'll write a for loop that prints an array of fighter1's stats and finds and prints the corresponding fighter2's stats. It will then join them together and store the data in a df.
    - Split
    - Initial Questions: 
        - 
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

## With more time...
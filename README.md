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
    - Create a df for the bouts only that lists only bout stats
    - Create a df for the first fighter with all of their stats
    - Create a df for the second fighter with all of their stats
    - Merge all three dfs together
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
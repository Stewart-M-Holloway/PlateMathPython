# PlateMathPython

## Introduction
A library for calculating how many plates to put onto a powerlifting bar to make a certain weight at the gym. 
This is actually a backend logic for an Alexa Skill, in which a user can audibly interact with the voice
assistant in order to calculate what type of weights to place on the bar

## Methodology
For simplicity and the First Draft's sake, I run with a relatively simple algorithm to start.
Essentially we have a known set of weights for each denomination:
 - 45,35,25,10,5,2.5 for lbs.
 - 20,15,10,5,2,1 for kgs.

This is based on the most common weights you'd tend to see at a commercial gym.
There are some initial checks to make sure the weights are reasonable and valid.
If a weight cannot be made with the denominations listed above, the response will be
an error code.
The algorithm iterates over these plate denominations, from largest to smallest.
Each time, it recursively subtracts an integer multiple of the plate denomination (times 2
since one plate must be placed on each side of the bar) until the weight is equal to 0. The
function then returns the set of weights that equals the target weight.
The PlateMath class offers interfaces for changing units and bar weights, so that for
non-typical bars (i.e. 35 pound bars), the user can individualize their interface to
account for this.

## How it's leveraged in the Alexa Service
My homemade Alexa project sends a target weight, barbell weight, and unit denomination
to the calculate plates function, which in turn serves either a set of plates or an
error code and a message. Alexa has logic to parse the response and communicate the 
results to the user.

## Known Bugs and Desirable Next Features
There is certainly room for improvement here, and if it becomes important enough (if people
end up using the application), I may come back and address the following:

Possible Future Features

- Repeat last weight
- Calculate multiple ways to make a certain weight (i.e. 235 pounds could be 45 + 45 + 5
or it could be 45 + 25 + 25, potentially an utterance: "Give me another way")
- Update plate set (add or remove plates from default sets)
- Limit plate quantities (i.e. I only have 2 35 lb. plates)
- Better MultiModal Presentation (I used boilerplate APL)
- Read barbell weight out loud (Alexa, how much does my bar weigh?)
- Warn about placing too much weight on one side (Potentially dangerous to load more than
45 lbs on each side)

Current Bugs/Issues

- Alexa should perk up and wait if can't make specific weight
- Catch change in units (i.e., you're bar is in pounds but you ask for 100 kilograms) - 
currently this will just return the weight as if you asked it in the unit denomination
for your bar

## Questions or requests?
You can email me at Stewart.M.Holloway@gmail.com

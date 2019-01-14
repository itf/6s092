# Readings 
Recitation notes 7, 6.006 Fall 2018 on stellar.

Lecture notes 8, 6.006 Fall 2018 on stellar.

# Direct Access Array

Wumpus has encountered many different heros (and heroines) that have tried to hunt him down. None of the heroes have been successful, but Wumpus wants to keep the upperhand. The hero agency has given each hero a unique 5 element long alpha-numeric (each element can be a number 0-9 or a letter in the alphabet) ID, so Wumpus stores info related to the hero, such as their name, ID, speed, weapon of choice, and stamina in a direct access array, where the ID corresponds to an index in his array, in case they come back. Assume that there is some order to the IDs, and so that the first ID can be accessed at the 0th index.

<question expression>
    csq_prompt = "How many different IDs (and thus indexes) are there in Wumpus's direct access array? Use the carat (^) to denote exponentiation. \n \n"
    csq_show_check= True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "36^5"
    csq_nsubmits = None
    csq_name = "exp1"
</question>

<question expression>
    csq_prompt = "The hero association is constantly assigning new heros. Wumpus generalizes his direct access array to store $k$-element alphanumeric IDs. How many different IDs are in Wumpus' direct access array? Assume that Wumpus has created indexes for every ID, even if the hero association has not given a specific ID to a hero yet. \n \n"
    csq_show_check= True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "36^k"
    csq_nsubmits = None
    csq_name = "exp2"
</question>

<question expression>
    csq_prompt = "Wumpus defeats a hero that has wandered into his cave. He wants to store the information about that hero in his array, or make a note about the number of times he has deteated that hero if the hero's information already exists. How long does it take to determine whether or not he has encountered a hero with a specific ID? Assume that converting an ID to an index takes O(1) time. Give an asymptotic bound, O(something). \n \n"
    csq_show_check= True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "O(1)"
    csq_nsubmits = None
    csq_name = "exp3"
</question>

<question expression>
    csq_prompt = "Wumpus overhears a rumour that a powerful hero named Bob is coming to hunt him. How long does it take for Wumpus to determine if Wumpus has encountered a hero named Bob before, given that there are $u$ indexes in his direct access array, and he is using the same method to assign IDs to indexes as in the statement above the first question? We only know Bob's name, not his ID. Give an asymptotic bound: O(something). \n \n"
    csq_show_check= True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "O(u)"
    csq_nsubmits = None
    csq_name = "exp4"
</question>

<question expression>
    csq_prompt = "Oh no! The computer that Wumpus' array was stored on suffered a memory failure due to the humidity in the cave. Most of the entries in Wumpus' array have been deleted, leaving him with only the data from $n$ entries; he doesn't even know which entries he still has. Wumpus now has to transfer the remaining entries onto a new drive. How long does it take for the computer to transfer those entries, if there are $u$ possible indexes? Give an asympotic bound, O(something). \n \n"
    csq_show_check= True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "O(u)"
    csq_nsubmits = None
    csq_name = "exp5"
</question>


<question multiplechoice>
csq_prompt = "In which scenarios could using a direct access array be useful?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,1]
csq_options =  ['Given a list of (10 digit lottery ticket numbers, name) pairs, determine if there are duplicate tickets, which would indicate fraud, and report the names that have the same number.',
'Record the stats on $n$ players, where the $j$th player is indexed at location $10^{j-1}-1$.',
'Record the frequency of each number (including irrational numbers) randomly stated by a 5-year-old.',
'Return the number of items a user sells on emirp-nonzama (a new company that is inverting the current marketplace), where each user has a unique 6 digit user ID, which can be represented in some order, assuming that there are as many users as possible IDs.']
csq_name="mc1"
</question>


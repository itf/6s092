# Readings 
[Lecture Notes 04](https://learning-modules.mit.edu/service/materials/groups/238004/files/aad7a820-c5b5-4eba-aff2-79bbdc1355e4/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Data Structures, 6.006 Fall 2018 on Stellar.

<python>
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_nsubmits = None
</python>


# Data Structures Intuition

<question multiplechoice>
csq_prompt = "Which of these describes a 'sequence'?"
csq_renderer = "radio"
csq_soln = 'Interface'
csq_options = ['Interface', 'Algorithm', 'Data structure']
</question>

<question multiplechoice>
csq_prompt = "Which of these could be a valid data structure? Remember we are using the Word-RAM model of computation."
csq_renderer = "checkbox"
csq_soln = [1,0,0,1]
csq_options = ['An array', 'The prime numbers less than $300$', 'Afrequency table', 'An array with a counter for the total number of elements that gets updated with insertions/deletions']
csq_explanation = "Arrays are just blocks of words according to the Word-RAM model. The last one also provides an operation on the data that is stored by an array."
</question>

<question multiplechoice>
csq_prompt = "Many children are entering Wumpus's cave, and none of them ever leave. Wumpus wants to keep track of how many kids have entered so far, and how tall the tallest child seen so far is. This describes:"
csq_renderer = "radio"
csq_soln = 'An interface'
csq_options = ['An interface', 'A data structure']
</question>

<question multiplechoice>
csq_prompt = "What are some valid data structures that would solve Wumpus's problem?"
csq_renderer = "checkbox"
csq_soln = [1, 1, 0, 0]
csq_options = ["Keeping the childrens' heights in an array, with an associated length and max functions that iterate over the array", "Keep track of length and max of the inputs seen so far, increment length every time and change max if we see a taller child", "Store a linked list of tuples that have the form $(height, pointer)$, where each pointer points at the next data point", "Plot the childrens' heights on a cartesian plane and use the horizontal line method to find where the maximum height is"]
</question>

<question multiplechoice>
csq_prompt = "Now Wumpus doesn't just want the tallest kid, but occasionally some authorities will come by and ask if Wumpus has seen a kid of some height $h$. Wumpus never lies, so now Wumpus wants to modify the interface so that it can find whether any children of that height have entered the cave. Is this a set interface or a sequence interface?"
csq_renderer = "radio"
csq_soln = "Set"
csq_options = ["Set", "Sequence"]
</question>

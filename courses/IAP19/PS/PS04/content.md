# Readings 
Recitation notes 1, algorithms section, 6.006 Fall 2018 on stellar.

Lecture notes 1, 2,  6.006 Fall 2018 on stellar.

[OCW algorithmic thinking](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec01.pdf)
# Algorithmic thinking


<question multiplechoice>
csq_prompt = "Choose the options that are algorithms? (Using the word ram model of computation)"
csq_renderer = "checkbox"
csq_soln = [1,0,1,0,1]
csq_options =  [' always return True',
'What is the shortest path between points A and B?',
'Add the input numbers together, divide by the number of input numbers',
'A sorted binary tree',
'Generate a random number, 0 or 1, with 50% chance. If you generated 0, return True, if not return False.']
csq_name="qexample1"
</question>


<checkyourself>
You should have a clear understanding of what is an algorithm. A series of unambiguous instructions mapping an input to an output.

</checkyourself>


## Understanding a simple algorithm

We have the following problem: given an array, we want to find a peak, i.e. an element that is larger or equal to its neighbohrs. 

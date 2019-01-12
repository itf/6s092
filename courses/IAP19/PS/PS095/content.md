# Readings 

[Lecture Notes 4](https://learning-modules.mit.edu/service/materials/groups/238004/files/aad7a820-c5b5-4eba-aff2-79bbdc1355e4/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Section on Linked Lists, 6.006 Fall 2018 on stellar.

# Linked List Operations

Let us represent a linked list as an array of arrays that contains "<-" which represents a left pointer, a number, and a right pointer represented by "->". If there is no left, or right pointer, let the string be replaced by "None". For example, if we were to represent the numbers 1, 2, and 3 in order as a linked list, it would look like this: [["None", 1, "->"], ["<-", 2, "->"], ["<-", 3, "None"]].

<question pythonliteral>
csq_prompt= "Wumpus has a linked list storing the numbers 100, 101, 102, and 103, in order. Wumpus adds 105 to the end. What does the linked list look like now? Give the entire linked list, represented as above. \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [["None", 100, "->"], ["<-", 101, "->"], ["<-", 102, "->"], ["<-", 103, "->"], ["<-", 105, "None"]]
csq_nsubmits = None
csq_name="LLOp1"
</question>

<question expression>
csq_prompt= "How long does it take to insert or delete an element at the end of a linked list with $n$ elements? Give the asymptotic runtime: O(something) \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "O(1)"
csq_nsubmits = None
csq_name="LLOp2"
</question>

<question pythonliteral>
csq_prompt= "Wumpus now deletes the first element. What does the linked list look like now? Give the entire linked list, represented as above. \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [["None", 101, "->"], ["<-", 102, "->"], ["<-", 103, "->"], ["<-", 105, "None"]]
csq_nsubmits = None
csq_name="LLOp3"
</question>


<question expression>
csq_prompt= "How long does it take to insert or delete an element at the end of a linked list with $n$ elements? Give the asymptotic runtime: O(something) \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "O(1)"
csq_nsubmits = None
csq_name="LLOp4"
</question>

<question expression>
csq_prompt= "Wumpus now has a linked list of numbers from $0$ to $n$. What is the asymptotic runtime of finding the $j$th elment, where $j$ is a number between $0$ and $n$ How long does it take for Wumpus to find a specific number? Give an asymptotic bound: O(something) \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "O(n)"
csq_nsubmits = None
csq_name="LLOp5"
</question>

#Using Linked Lists
<question multiplechoice>
csq_prompt = "In which of these scenarios could you use a linked list?"
csq_renderer = "checkbox"
csq_soln = [1,0,1,0,1]
csq_options =  ['Storing elements in $O(1)$ time, and accessing the most recently inserted element and the first stored element in $O(1)$ time.',
'Finding the 6th, 10, and $n$th element in $O(1)$ time.',
'Implementing a FIFO (first in, first out) queue, where new elements are inserted at one end, and elements are removed in the order that they are inserted into the queue.',
'Finding the smallest value in $O(1)$ time.',
'Finding the smallest value of $n$ elements in $O(n)$ time.']
csq_name="ULLmc1"
</question>

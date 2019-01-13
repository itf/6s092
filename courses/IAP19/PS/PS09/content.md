# Readings 
[Lecture notes 4](https://learning-modules.mit.edu/service/materials/groups/238004/files/aad7a820-c5b5-4eba-aff2-79bbdc1355e4/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.

[Recitation notes 4](https://learning-modules.mit.edu/service/materials/groups/229217/files/a78ef148-8b86-4ef1-bcf1-bd99fd961120/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.
# Dynamic Arrays

Recall that arrays are blocks of memory allocated by the computer to store elements.


<question expression>
    csq_prompt = "Wumpus has an array that has been allocated enough memory to store $n$ elements. There are currently $n-1$ elements in the array. How long does it take to store the $n$th element? Give an asympotic runtime: $\\theta(something)$. Use $theta$ to denote the theta symbol. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "theta(1)"
    csq_nsubmits = None
    csq_name = "exp1"
    csq_funcs = {"T": (lambda c: c**3*0.6006+c**2, lambda  c:  f"T({', '.join(c)})" ),
    "O": (lambda c: c**3*1.6006-c**2, lambda  c:  f"O({', '.join(c)})" ),
    "theta": (lambda c: -c**3*0.06006+c**2*0.2, lambda  c:   f"\\theta({', '.join(c)})")}
    </question>

Assume that when we have a full array of size $n$, and we need to perform a new array allocation, it takes $n$ operations to copy the $n$ values (there are also additional operations like creating a new array, and deleting the old one, but let us consider that to be overhead).

<question expression>
    csq_prompt = "Wumpus now wants to add an $n+1$th element to the array. How long does that take? GGive an asympotic runtime: $\\theta(something)$. Use $theta$ to denote the theta symbol. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "theta(n)"
    csq_nsubmits = None
    csq_name = "exp2"
    csq_funcs = {"T": (lambda c: c**3*0.6006+c**2, lambda  c:  f"T({', '.join(c)})" ),
    "O": (lambda c: c**3*1.6006-c**2, lambda  c:  f"O({', '.join(c)})" ),
    "theta": (lambda c: -c**3*0.06006+c**2*0.2, lambda  c:   f"\\theta({', '.join(c)})")}
</question>

Wumpus has implemented a dynamic array that he calls $ALO^{TM}$(allocate-less-often) which allocates $n/4$ additional spaces. We will run an analysis to ensure that his array actually achieves the amortized constant bound for insertions.

<question expression>
    csq_prompt = "Wumpus' array just performed a space allocaiton. It now has $n/4$ additional spaces, compared to the original $n$ spaces before allocation, (for a total of ${5*n}/4$ total spaces). How many insertions can $ALO$ perform in constant $O(1)$ time for every new allocation of the array? Assume space allocation is a separate operation, and we can place the last element in constant time. Give a specific value, ie $2$, $n/10$, not an asymptotic bound. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "n/4"
    csq_nsubmits = None
    csq_name = "exp3"
</question>

<question expression>
    csq_prompt = "What is the total number of operations of those insertions? Give a specific value. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "n/4"
    csq_nsubmits = None
    csq_name = "exp4"
</question>

<question expression>
    csq_prompt = "Per allocation, how many times does Wumpus' dynamic array perform an $\\theta(n)$ operation? \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "1"
    csq_nsubmits = None
    csq_name = "exp5"
</question>

<question expression>
    csq_prompt = "How many operations are done per allocation, in terms of insertions and the creation of a larger array? Give a specific value. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "n+n/4"
    csq_nsubmits = None
    csq_name = "exp6"
</question>

<question expression>
    csq_prompt = "By dividing the total number of operations done per allocation cycle by the number of of insertions per allocation cycle, we can get the average amount of operations done per insertion. If each operation takes a constant amount of work and the average number of operations done per insertion is constant, then we can prove our constant amortized bound for insertions. Find the average number of operations done per insertion. Give a specific value. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "5"
    csq_nsubmits = None
    csq_name = "exp7"
</question>

<question multiplechoice>
    csq_prompt = "Which of these space allocations will allow dynamic arrays to achieve an amortized constant insertion operation?"
    csq_renderer = "checkbox"
    csq_soln = [1,0,1,1,0]
    csq_options =  ['Allocating 2n space',
    'Allocating 2 addtional spaces',
    'Allocating $n/1000$ addional spaces',
    'Allocating c*n additional space, where c is some constant non-zero number',
    'Allocating 2x, where x is a random number between 1 and 100']
    csq_name="mc1"
</question>

<checkyourself>
    Does a dynamic array, as discussed in lecture, support $\theta(1)$ insertions at the beginning of the array?
    <showhide>
        No, because there is no additional space allocated at the beginning of the array. If we want to insert an element at the beginning, we will have to move all elements right, which takes $O(n)$ time.
    </showhide>
</checkyourself>

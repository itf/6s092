# Readings 
Recitation notes 2, Master Theorem, 6.006 Fall 2018 on stellar.

Recursion and Recursion Trees problem set.

# Master Theorem


<question multiplechoice>
csq_prompt = "Question?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['option 1',
'option 2',
'option 3',
'option 4']
csq_name="qexample1"
</question>

Calculate the recursions using the Master Theorem
<question expression>
csq_prompt = """$T(n) = T(n/2) + \\theta(1)$

T(n) = """
csq_show_check = True
csq_soln = ["theta(log(n))"]
csq_explanation = "Case 2"
</question>

<question expression>
csq_prompt = """$T(n) = 2T(n/2) + O(n)$

T(n) = """
csq_soln = ["O(n*log(n))"]
csq_explanation = "Case 2"
</question>

<question expression>
csq_prompt = """$T(n) = 4T(n/2) + \\theta(n^2)$

T(n) = """
csq_soln = ["theta(n^2*log(n))"]
csq_explanation = "Case 2"
</question>


<question expression>
csq_prompt = """$T(n) = 9T(n/3) + O(n^2)$

T(n) = """
csq_soln = ["O(n^2*log(n))"]
csq_explanation = "Case 2"
</question>

<question expression>
csq_prompt = """$T(n) = 8T(n/2) + \\theta(n^3)$

T(n) = """
csq_soln = ["theta(n^3*log(n))"]
csq_explanation = "Case 2"
</question>




<question expression>
csq_prompt = """$T(n) = 2T(n/2) + \\theta(n^2)$

T(n) = """
csq_soln = ["theta(n^2)"]
csq_explanation = "Case 3"
</question>


<question expression>
csq_prompt = """$T(n) = 8T(n/3) + O(n^2)$

T(n) = """
csq_soln = ["O(n^2)"]
csq_explanation = "Case 3"

</question>




<question expression>
csq_prompt = """$T(n) = 4T(n/2) + O(n)$

T(n) = """
csq_soln = ["theta(n^2)"]
csq_explanation = "Case 1. Observe that it is theta, and not O."
</question>

<question expression>
csq_prompt = """$T(n) = 8T(n/2) + \\theta(n^2)$

T(n) = """
csq_soln = ["theta(n^3)"]
csq_explanation = "Case 1. Observe that it is theta, and not O."
</question>


<question expression>
csq_prompt = """$T(n) = 27T(n/3) + O(n^2)$

T(n) = """
csq_soln = ["theta(n^3)"]
csq_explanation = "Case 1. Observe that it is theta, and not O."
</question>




<checkyourself>
Are you understanding?
<showhide>
yeah
</showhide>
</checkyourself>


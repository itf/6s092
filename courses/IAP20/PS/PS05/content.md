# Readings 
[Recitation notes 2](https://learning-modules.mit.edu/service/materials/groups/278835/files/f387e153-76f7-43be-b01a-9c09980b4b6c/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Section on Master Theorem, 6.006 Fall 2018 on stellar.

[Recursion and Recursion Trees problem set](https://s092.xvm.mit.edu/IAP20/PS/PS02)

# Master Theorem

<question multiplechoice>
csq_prompt = "How many cases does the master theorem have?"
csq_renderer = "checkbox"
csq_soln = [0,0,1,0]
csq_options =  ['1',
'2',
'3',
'4']
csq_name="qexample1"
</question>

Calculate the recursions using the Master Theorem, and use the tightest asymptotic bound possible (i.e. if you can either put $O(n)$ or $\Theta(n)$).

<question expression>
csq_prompt = """$T(n) = T(n/2) + \\Theta(1)$

$T(n) =$ """
csq_show_check = True
csq_soln = ["Theta(log(n))"]
csq_explanation = "Case 2"
</question>

<question expression>
csq_prompt = """$T(n) = 2T(n/2) + O(n)$

$T(n) =$ """
csq_soln = ["O(n*log(n))"]
csq_explanation = "Case 2"
</question>

<question expression>
csq_prompt = """$T(n) = 4T(n/2) + \\Theta(n^2)$

$T(n) =$ """
csq_soln = ["Theta(n^2*log(n))"]
csq_explanation = "Case 2"
</question>


<question expression>
csq_prompt = """$T(n) = 9T(n/3) + O(n^2)$

$T(n) =$ """
csq_soln = ["O(n^2*log(n))"]
csq_explanation = "Case 2"
</question>

<question expression>
csq_prompt = """$T(n) = 8T(n/2) + \\Theta(n^3)$

$T(n) =$ """
csq_soln = ["Theta(n^3*log(n))"]
csq_explanation = "Case 2"
</question>




<question expression>
csq_prompt = """$T(n) = 2T(n/2) + \\Theta(n^2)$

$T(n) =$ """
csq_soln = ["Theta(n^2)"]
csq_explanation = "Case 3"
</question>


<question expression>
csq_prompt = """$T(n) = 8T(n/3) + O(n^2)$

$T(n) =$ """
csq_soln = ["O(n^2)"]
csq_explanation = "Case 3"
</question>

<question expression>
csq_prompt = """$T(n) = 4T(n/2) + O(n)$

$T(n) =$ """
csq_soln = ["Theta(n^2)"]
csq_explanation = "Case 1. Observe that it is Theta, and not O."
</question>

<question expression>
csq_prompt = """$T(n) = 8T(n/2) + \\Theta(n^2)$

$T(n) =$ """
csq_soln = ["Theta(n^3)"]
csq_explanation = "Case 1. Observe that it is Theta, and not O."
</question>


<question expression>
csq_prompt = """$T(n) = 27T(n/3) + O(n^2)$

$T(n) =$ """
csq_soln = ["Theta(n^3)"]
csq_explanation = "Case 1. Observe that it is Theta, and not O."
</question>

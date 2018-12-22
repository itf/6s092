#Asymptotics

##Big O Notation

We say that $f(n) \in O(g(n)$ if there exists $n_0$ and c such that for all $n>n_0$, $f(n) \le cg(n)$, where c is a positive constant.

It is common to write $f(n) = O(g(n))$ instead of $f(n) \in O(g(n))$. Both mean the same.

Order the following functions such that if f is to the left of g, then $f(n) \in O(g(n))$. If more than one solution exists, mark all of them.

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,1,1]
csq_options =  ['$(n),\ (n+4),\ (5n)$',
 '$(n+4),\ (5n),\ (n)$',
 '$(5n),\ (n+4),\ (n)$']
</question>

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,1,0]
csq_options =  ['$(n),\ (n+4),\ (5n),\ (n^2),\ (n^2+n),\ (5n)^2$',
 '$(n+4),\ (5n),\ (n),\ (5n)^2,\ (n^2),\ (n^2+n)$',
 '$(n^2),\ (5n)^2,\ (n^2+n),\ (5n),\ (n),\ (n+4)$']
</question>


<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [0,1,0]
csq_options =  ['$(n\log(n)),\ (n),\ (n^2)$',
 '$(n),\ (n\log(n)),\ (n^2)$',
 '$(n),\ (n^2),\ n\log(n)$']
</question>

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,0,0]
csq_options =  ['$(n\log(n)),\ (n^{1.01}),\ (n^2)$',
 '$(n^{1.01}),\ (n\log(n)),\ (n^2)$',
 '$(n^{1.01}),\ (n^2),\ n\log(n)$']
</question>

<checkyourself>
Is ${n \choose 3} \in O(n^3)$? What about  $n^3 \in O({n \choose 3})$

<showhide>
Yes and yes.
</showhide>
</checkyourself>

## Big $\Omega$

We say that $f(n) \in \Omega(g(n)$ if there exists $n_0$ and c such that for all $n>n_0$, $cf(n) \ge g(n)$, where c is a positive constant.

Order the following functions such that if f is to the left of g, then $f(n) \in \Omega(g(n))$. If more than one solution exists, mark all of them.

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,1,1]
csq_options =  ['$(n),\ (n+4),\ (5n)$',
 '$(n+4),\ (5n),\ (n)$',
 '$(5n),\ (n+4),\ (n)$']
</question>

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [0,0,1]
csq_options =  ['$(n),\ (n+4),\ (5n),\ (n^2),\ (n^2+n),\ (5n)^2$',
 '$(n+4),\ (5n),\ (n),\ (5n)^2,\ (n^2),\ (n^2+n)$',
 '$(n^2),\ (5n)^2,\ (n^2+n),\ (5n),\ (n),\ (n+4)$']
</question>


<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [0,1,0]
csq_options =  ['$(n\log(n)),\ (n),\ (n^2)$',
 '$(n^2),\ (n\log(n)),\ (n)$',
 '$(n),\ (n^2),\ n\log(n)$']
</question>

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [0,0,1]
csq_options =  ['$(n\log(n)),\ (n^{1.01}),\ (n^2)$',
 '$(n^{1.01}),\ (n\log(n)),\ (n^2)$',
 '$(n^{2}),\ (n^{1.01}),\ n\log(n)$']
</question>


## $\theta$

We say that $f(n) \in \theta(g(n)$ if $f(n) \in O(g(n)$ and $f(n) \in \Omega(n)$

Choose the groups such that for any 2 functions in the groups, $f(n)$, $g(n)$, we have $f(n) \in \theta(g(n)$

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,1,0,0,0,1,0]
csq_options =  ['$(n),\ (n+4),\ (5n)$',
 '$(n\log_2(n)),\ (n\log_3(n)),\ (n\log_{10}(n))$',
 '$(n^2),\ (n^3),\ (n^4)$',
'$(n^{2^n}),\ (n^{2^{n+1}}),\ (n^{2^{n+2}})$',
'$(n^{\log_2(5)}),\ (n^{\log_3(5)}),\ (n^{\log_5(5)})$',
'$(2^n),\ (2^{n+1}),\ (2^{n+2})$',
'$(2^{2^n}),\ (2^{2^{n+1}}),\ (2^{2^{n+2}})$']
</question>


## Recursions and recursion tree


Which of the following recursions are equivalent?

<question multiplechoice>
csq_prompt = "$T(n) =$"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['$T({n\over 2}) + T({n\over 2}) + f(n)\ = 2T({n\over 2}) + f(n)$',
'$T({n\over 2}) + T({n\over 2}) + f(n)\ = T({n}) + f(n)$',
'$T({n}) + O(n)\ = T({n}) + n$',
'$T({n}) + O(n)\ = T({n}) + \\theta(n)$']
</question>






Bob told me that he invented a sort algorithm that splits an array into 3 equal parts, sorts each one of them, and then merges in $O(n)$ the 3 parts.
What is the recursion for the algorithm 
<question expression>
csq_prompt = "$T(n)=$ "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["3*T(n/3)+O(n)"]
csq_explanation = "3 parts of 1/3 of the size + the work to join"
csq_nsubmits = None
</question>


Consider the following recursion: 

$$T(n) = aT\left(\frac{n}{b}\right) + n^c$$ 

Draw it as a recursion tree. Answer the following about the tree.

<question expression>
csq_prompt = "Number of nodes on the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a"]
csq_explanation = ""
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Number of elements in the nodes of the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["n/b"]
csq_explanation = ""
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Amount of work done in each node in the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["(n/b)^c"]
csq_explanation = ""
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Total work done in the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a*(n/b)^c"]
csq_explanation = ""
csq_nsubmits = None
</question>

<question expression>
csq_prompt = """Suppose the amount of work done in the first level is $x$ and the amount of work in the second level is $y$.

What is $\\frac{y}{x}$?
"""
csq_error_on_unknown_variable = True #make sure they get rid of n in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a/(b^c)"]
csq_explanation = ""
csq_nsubmits = None
</question>
<question expression>
csq_prompt = """Suppose the amount of work per level is constant. 

If  $\\frac{y}{x} =1$,  what is $c$ in terms of $a$ and $b$?  To write $\log_x(y)$, please write $\log(y,x)$
"""
csq_error_on_unknown_variable = True #make sure they get rid of n in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["log(a,b)", "log(a)/log(b)"]
csq_explanation = ""
csq_nsubmits = None
csq_name="question"
</question>



<question multiplechoice>


</question>


<question pythoncode>

tests = (
    ( # Student 1
        ((0, 1, 3),
         (2, 4, 6),
         (5, 7, 8)),
        3
    ),
    ( # Student 2
        ((0, 1, 4, 7),
         (1, 3, 4, 8),
         (2, 6, 6, 8),
         (6, 8, 8, 9)),
        4
    ),
    ( # Student 3
        ((1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8),
         (1, 2, 3, 5, 8)),
        5
    ),
    ( # Student 4
        ((1,  2,  5,  35, 44, 49, 50),
         (5,  10, 20, 46, 61, 61, 62),
         (8,  19, 38, 49, 65, 69, 77),
         (11, 33, 40, 65, 68, 70, 80),
         (17, 38, 42, 65, 68, 71, 89),
         (19, 42, 58, 76, 77, 80, 93),
         (30, 44, 59, 79, 86, 87, 95)),
        42
    ),
    ( # Student 5
        ((2,  6,  7,  8,  9,  15, 19, 19, 20),
         (8,  9,  19, 20, 43, 48, 50, 53, 56),
         (13, 22, 22, 25, 57, 60, 73, 75, 84),
         (23, 25, 35, 39, 58, 60, 73, 81, 89),
         (24, 26, 42, 60, 60, 65, 84, 91, 91),
         (26, 30, 42, 62, 76, 80, 87, 94, 94),
         (30, 41, 47, 69, 79, 81, 93, 95, 96),
         (52, 55, 55, 70, 81, 86, 93, 97, 97),
         (64, 67, 73, 74, 82, 88, 96, 99, 99)),
        87
    ),
    ( # Staff 6
        ((0,0,1,3,3,4,9,11,11,15),
        (1,2,4,7,8,22,34,40,41,46),
        (5,6,14,16,21,22,35,41,49,50),
        (12,15,16,17,23,23,39,56,69,76),
        (15,23,23,26,32,37,43,56,74,93),
        (19,24,25,33,38,41,44,68,75,96),
        (20,26,31,50,50,57,67,69,78,109),
        (28,40,54,54,55,65,72,76,82,135),
        (33,55,63,66,85,87,95,100,102,141),
        (35,60,67,69,86,103,112,120,122,146),
        (46,80,82,85,90,106,115,121,124,154),
        (59,93,96,96,97,116,126,133,134,159),
        (66,100,102,110,113,118,133,145,151,162),
        (87,103,104,111,129,136,152,152,160,167),
        (89,113,122,125,129,139,161,171,171,176),
        (104,113,124,125,156,158,164,172,178,179),
        (112,127,127,164,167,169,176,183,191,191),
        (116,141,154,174,176,182,182,183,193,194),
        (120,157,157,175,178,184,187,188,195,198),
        (126,165,166,181,181,187,187,195,195,199)),
        57
    ),
    ( # Staff 7
        ((0,0,4,6,10,10,11,12,12,13),
        (0,1,6,10,10,11,11,12,14,15),
        (8,11,11,14,18,21,24,26,27,28),
        (9,13,17,18,18,21,27,31,34,37),
        (10,15,18,18,31,37,38,39,41,43),
        (12,17,19,20,32,38,42,42,43,48),
        (16,17,21,28,33,38,50,53,56,58),
        (18,18,23,32,33,41,50,55,63,65),
        (18,21,28,33,34,49,50,56,70,73),
        (20,21,30,38,41,50,51,57,74,75),
        (21,23,31,42,47,55,56,63,75,77),
        (21,24,39,43,55,61,66,69,76,84),
        (34,35,40,44,61,68,70,71,76,88),
        (45,51,63,65,68,71,72,73,77,91),
        (46,55,74,77,79,80,80,80,84,91),
        (47,56,75,81,82,85,88,94,95,96),
        (51,60,75,82,83,87,91,94,95,99),
        (61,66,76,84,86,88,92,95,97,99),
        (64,70,79,87,87,88,94,97,98,99),
        (71,73,81,88,89,95,98,98,99,99)),
      60
    ),
    ( # Staff 8
        ((0,3,5,7,10,12,35,41,45,48,52,56,57,61,68,70,72,75,84,91),
        (2,5,6,8,12,18,41,46,58,65,66,77,87,96,127,129,142,142,166,167),
        (8,12,17,18,31,35,45,52,66,75,85,85,100,106,133,135,144,146,170,170),
        (9,15,18,27,35,36,66,78,79,87,89,99,103,115,134,137,147,153,177,181),
        (24,24,47,51,55,62,72,80,104,106,119,128,130,137,137,143,153,159,178,190),
        (27,33,47,55,57,67,99,100,111,122,127,138,140,144,146,147,157,162,181,191),
        (28,37,47,56,58,67,100,101,112,123,128,145,146,148,151,153,158,168,191,193),
        (34,67,69,72,84,87,107,119,119,129,133,149,150,170,170,171,171,175,194,195),
        (40,75,97,101,103,117,120,128,139,139,142,149,169,172,174,177,185,188,195,197),
        (45,76,99,103,111,123,124,145,150,166,168,170,170,173,185,188,190,192,198,198)),
        31
    ),
    ( # Staff 9
        ((0,0,1,6,6,7,14,14,15,16,16,18,21,22,22,26,27,29,35,35),
        (2,2,8,14,15,16,18,20,22,27,32,33,39,40,41,49,57,62,64,65),
        (2,3,9,17,22,25,35,37,39,40,43,46,48,48,59,64,66,68,74,81),
        (3,5,10,19,28,35,40,40,42,45,46,47,52,54,60,65,67,69,78,82),
        (5,7,16,19,32,43,43,43,44,50,54,56,61,64,68,70,71,74,80,83),
        (9,11,18,20,34,43,46,50,50,55,59,59,63,67,77,78,80,80,81,86),
        (14,21,22,24,37,45,47,58,63,66,68,69,78,80,85,86,90,91,92,94),
        (15,23,26,30,40,47,52,61,63,67,69,69,81,81,86,86,92,92,95,97),
        (15,28,34,37,47,50,55,62,66,70,72,80,81,85,89,89,93,94,96,99),
        (21,28,34,39,48,54,57,67,68,71,79,81,81,87,90,91,94,97,99,99)),
        29
    ),
    ( # Staff 10
        ((0,0,1,2,5,7,10,11,12,12,13,15,20,21,28,34,48,74,84,108),
        (3,3,6,7,7,8,17,42,47,51,53,56,60,81,84,93,97,103,114,116),
        (5,9,15,16,20,24,26,44,50,52,54,67,74,90,91,96,101,136,138,142),
        (6,11,33,41,44,45,48,59,64,76,77,85,90,93,96,128,140,159,167,189),
        (9,12,40,48,70,84,85,117,117,120,127,127,127,131,135,135,143,168,169,195),
        (12,14,46,74,79,97,98,119,125,130,134,135,138,143,146,155,160,168,173,197),
        (13,17,46,79,96,101,105,123,129,131,136,155,156,165,180,193,197,206,217,217),
        (22,22,46,96,104,109,119,144,154,158,160,170,181,203,210,213,231,244,251,263),
        (38,39,54,113,134,141,154,157,191,212,214,223,225,232,237,237,252,263,271,275),
        (38,45,55,121,135,146,165,180,196,215,218,228,232,242,266,272,286,293,300,305),
        (41,55,62,122,143,152,167,198,199,238,241,248,249,259,282,297,307,314,317,323),
        (60,63,75,134,175,194,201,201,210,254,258,261,263,276,293,302,324,327,331,332),
        (83,101,116,140,184,206,218,255,255,258,263,277,279,286,294,304,327,330,356,365),
        (86,124,146,199,203,211,239,278,278,292,295,302,304,309,324,333,339,349,357,365),
        (88,132,173,204,208,213,243,279,285,297,301,303,306,312,326,340,341,355,366,370),
        (105,137,188,207,211,219,248,284,287,297,301,306,309,318,333,341,354,370,373,381),
        (112,159,190,215,218,230,250,289,289,301,305,309,316,319,348,350,357,373,376,393),
        (113,160,193,221,250,270,272,292,309,318,322,338,339,342,353,356,357,375,383,394),
        (117,174,203,222,256,294,296,296,336,345,348,356,359,360,361,365,368,377,385,394),
        (194,202,210,249,259,306,306,309,337,346,350,360,361,364,367,373,383,385,385,395)),
        61
    )
)

csq_interface = 'ace'
csq_prompt = "Upload your `search_sorted_2D_array.py`: "
csq_show_skeleton = False
csq_soln = """
def search_sorted_2D_array(A, v): 
    return 'Solution will be posted to Stellar'
"""

def solution(A, v):
    def search_subarray(A, v, x0, y0, x1, y1):
        if (x1 < x0) or (y1 < y0):
            return None             # Base Case, no elements
        a = A[y1][x0]
        if a > v:                   # All of last row > v
            return search_subarray(A, v, x0, y0, x1, y1 - 1)
        if a < v:                   # All of first column < v
            return search_subarray(A, v, x0 + 1, y0, x1, y1)
        return (x0, y1)             # Found!

    return search_subarray(A, v, 0, 0, len(A[0]) - 1, len(A) - 1)

def is_correct(A, v, sol):
    if sol is not None:
        (x, y) = sol
        return A[y][x] == v
    return solution(A, v) is None

csq_tests = []
for i, t in enumerate(tests):
    def check(ans, soln, i = i):
        A, v = tests[i]
        return is_correct(A, v, eval(ans))
        
    csq_tests.append({
        'code': """
A = %r
v = %r
for i in range(100):
    ans = search_sorted_2D_array(A, v)
""" % t,
        'show_code': i < 5,
        'grade': True,
        'check_function': check
    })

csq_sandbox_options = {
    'BADIMPORT': ['lib601', 'numpy', 'scipy', 'matplotlib'], 
    'CLOCKTIME': 0.36, 
    # 'CPUTIME': 0.36, 
    'MEMORY':1e9
}
</question>
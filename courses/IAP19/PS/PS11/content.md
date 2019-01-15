# Readings 
Recitation notes 8, 6.006 Fall 2018 on stellar.


# Counting Sort

<question multiplechoice>
csq_prompt = """We want to perform counting sort on some of the students in 6.s092 in order to sort them by heights in inches. Given what you know about human beings, is a reasonable estimate for $u$?"""
csq_renderer = "radio"
csq_soln = '100'
csq_options = ['5', '50','100', '1000']
</question>

<question multiplechoice>
csq_prompt = """All of the 6.s092 students dropped out, so now we only have the following three students. :( Their information is formatted as `(student_id, name, height_inches)`.

We perform counting sort on them anyway, inserting them into a direct access array $d$ in the order shown below. The direct access array has size $u$ as determined in the previous problem. What is true about $d$, given that the list `[x, y]` represents a queue where `x` was inserted into the queue before `y`?

```
h = (1, Helen, 60)
j = (2, Jakob, 66)
c = (3, Courtney, 68)
g = (4, Ghost, 66)```
"""
csq_renderer = "checkbox"
csq_soln = [0,1,0,0,1,0]
csq_options = [
"`d[1] = [(1, 'Helen', 60)]`",
"`d[66] = [(2, 'Jakob', 66), (4, 'Ghost', 66)]`",
"`d[66] = [(4, 'Ghost', 66), (2, 'Jakob', 66)]`",
"`d['Ghost'] = [(4, 'Ghost', 66)]`",
"`d[60] = [(1, 'Helen', 60)]`",
"`d[0] = [(1, 'Helen', 60), (2, 'Jakob', 66), (3, 'Courtney', 68), (4, 'Ghost', 66)]`"
]
csq_explanation = "If we're sorting by height, then the key would be heights and not IDs or names."
</question>

<question expression>
csq_prompt = """Now we read from $d$ to get the list of students sorted by increasing height. What sequence would we get? Submit your answer as 4 letters, i.e. cghj"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_nsubmits = None
csq_soln = "hjgc"
csq_explanation = "Jakob was before Ghost in the queue."
</question> 



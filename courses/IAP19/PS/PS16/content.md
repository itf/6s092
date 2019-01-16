# Readings
Recitation notes 5b, 6.006 Fall 2018 on stellar.

Lecture notes 6, 6.006 Fall 2018 on stellar.
# Binary Search Trees


<question multiplechoice>
csq_prompt = "Which of the following trees are BSTs? (There may be more than one)."
csq_renderer = "checkbox"
csq_soln = [1,1,1,0]
csq_options =  [
'''
         10
        /  \\
      5      15
'''
,
'''
         5
       /  \\
     5     15
''',
'''
        5
      /  \\
    5      5
'''
,
'''
          10
        /   
      5
       \\
         15
'''
]
csq_explanation = "The first three trees satisfy the BST property. Remember that the BST property states that keys in the left subtree must be <= the key of a node, and keys in the right subtree must be >= the key of a node. The fourth tree does not satisfy the BST property because 15 > 10, but 15 is in the left subtree of the node with key 10."
</question>


<question multiplechoice>
csq_prompt = '''
We have the following BST: \n
              12 \n
            /   \\ \n
          7       16 \n
        /  \\   /   \\ \n
      A    B   C      D \n

We insert a node with key 10 into the BST. Where does it go (to satisfy the BST property)?
'''
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options =  ["A", "B", "C", "D"]
csq_explanation = "We compare 10 to 12. 10 < 12, so we go to the left subtree. We compare 10 to 7. 10 > 7, so we put 10 in the right subtree at position B."
</question>


<question multiplechoice>
csq_prompt = """
We have the following BST: \n
         8 \n
     /     \\ \n
    4        14 \n
            /    \\ \n
           10     16 \n
We delete the node with key 14. What does the tree look now? (May be more than one answer).
"""
csq_renderer = "checkbox"
csq_soln = [1,1,0,0]
csq_options =  [
'''
        8 \n
      /   \\ \n
     4      10 \n
             \\ \n
                 16 \n
''',
'''
         8 \n
       /    \\ \n
     4       16 \n
            /     \n
          10     
''',
'''
        8 \n
     /     \n
    4       
''',
'''
        8 \n
      /   \\ \n
     4      10 \n
''',
]
csq_explanation = "When we delete the node with key 14, either the node with key 10 or the node with key 16 can take its place."
</question>


<question multiplechoice>
csq_prompt = """
We have the following BST: \n
             8 \n
          /     \\ \n
         4        14 \n
       /   \\     /   \\ \n
      2      5   10     16 \n
We delete the root (node with key 8). What does the tree look now? (Follow the delete function we learned in class).
"""
csq_renderer = "checkbox"
csq_soln = [0,1,0]
csq_options =  [
'''
               14
             /   \\
           10     16
         /
        4
       /  \\
     2     5
''',
'''
          10 \n
        /     \\ \n
      4        14 \n
     /  \\        \\ \n
    2     5         16 \n
''',
'''
               4
              /  \\
            2      5
                     \\
                      14
                    /   \\
                  10      16
'''
]
csq_explanation = "We are in the case where the node being deleted has two children. We take the min of the right subtree (or the max of the left subtree), and put move it to the place of the deleted node."
</question>

<question pythonliteral>
csq_prompt = "For the BST in the above problem (before deletion), what is the result of an in-order traversal? Enter your answer as a python list of strings."
csq_soln = [2,4,5,8,10,14,16]
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_explanation = "[2,4,5,8,10,14,16] For each node, we go to the min of its subtree (all the way left), if it has a left subtree, and append that one to the sorted list. From there, we add the parent and then go to the right subtree. We repeat this process throughout the tree."
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "How long does it take to find an element in a binary search tree of height $h$ with $n$ elements?"
csq_soln = "O(h)"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_explanation = "It's not $\\theta(h)$ because our element could be the root, in which case it would take $\\theta(1)$ time to find."
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "How long does it take to perform in order traversal in a binary search tree of height $h$ with $n$ elements?"
csq_soln = ["theta(n)", "O(n)"]
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_explanation = "Even though it takes up to $O(h)$ work to find a specific value, in-order traversal performs $O(1)$ work per node, so it takes a total of $O(n)$ work."
csq_nsubmits = None
</question>

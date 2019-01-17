# Readings
[Recitation notes 5b](https://learning-modules.mit.edu/service/materials/groups/238004/files/01453835-3d27-478a-8069-4f55b2eeace6/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.

[Lecture notes 6](https://learning-modules.mit.edu/service/materials/groups/238004/files/1d824237-2789-4b76-9829-c7844c145ad5/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.

# Binary Search Trees


<question multiplechoice>
csq_prompt = "Which of the following trees are BSTs? (There may be more than one)."
csq_renderer = "checkbox"
csq_soln = [1,1,1,0,1]
csq_options =  [
'''
```
  10
 /  \\
5    15
```
'''
,
'''
```
   5
  /  \\
5    15
```
''',
'''
```
   5
  /  \\
5     5
```
'''
,
'''
```
   10
  /   
5
 \\
  15
```
'''
,
'''
```
5
 \\
   10
     \\
     15         
```
'''
]
csq_explanation = "Remember that the BST property states that keys in the left subtree must be $\\leq$ the key of a node, and keys in the right subtree must be $\\geq$ the key of a node. The fourth tree does not satisfy the BST property because $15 > 10$, but $15$ is in the left subtree of the node with key $10$."
</question>


<question multiplechoice>
csq_prompt = '''
We have the following BST: \n
              12 
            /   \\ 
          7       16 
        /  \\   /   \\ 
      A    B   C      D 

We insert a node with key $10$ into the BST. Where does it go (to satisfy the BST property)?
'''
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options =  ["A", "B", "C", "D"]
csq_explanation = "We compare 10 to 12. 10 < 12, so we go to the left subtree. We compare 10 to 7. 10 > 7, so we put 10 in the right subtree at position B."
</question>


<question multiplechoice>
csq_prompt = """
We have the following BST: \n
         8 
     /     \\ 
    4        14 
            /    \\ 
           10     16 
We delete the node with key $14$. What does the tree look now? (May be more than one answer).
"""
csq_renderer = "checkbox"
csq_soln = [1,1,0,0]
csq_options =  [
'''
        8 
      /   \\ 
     4      10 
             \\ 
              16 
''',
'''
         8 
       /    \\ 
     4       16 
            /     
          10     
''',
'''
        8 
     /     
    4       
''',
'''
        8 
      /   \\ 
     4      10      
''',
]
csq_explanation = "When we delete the node with key 14, either the node with key 10 or the node with key 16 can take its place."
</question>


<question multiplechoice>
csq_prompt = """
We have the following BST: \n
             8 
          /     \\ 
         4        14 
       /   \\     /   \\ 
      2      5   10     16 
We delete the root (node with key 8). What does the tree look now? (Follow the algorithm described in the recitation notes).
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
          10 
        /     \\ 
      4        14 
     /  \\        \\ 
    2     5         16 
''',
'''
               4
              /  \\
            2      5
                     \\
                      14
                    /   \\
                  10      16      .
'''
]
csq_explanation = "We are in the case where the node being deleted has two children. We take the min of the right subtree (or the max of the left subtree), and put move it to the place of the deleted node."
</question>

<question pythonliteral>
csq_prompt = "For the BST in the above problem (before deletion), what is the result of an in-order traversal? Enter your answer as a python list of integers."
csq_soln = [2,4,5,8,10,14,16]
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_explanation = "For each node, we go to the min of its subtree (all the way left), if it has a left subtree, and append that one to the sorted list. From there, we add the parent and then go to the right subtree. We repeat this process throughout the tree."
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "How long does it take to find an element in a binary search tree of height $h$ with $n$ elements? Give the asymptotic complexity."
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
csq_explanation = "Even though it takes up to $O(h)$ work to find a specific value, in-order traversal performs $\\theta(1)$ work per node, so it takes a total of $\\theta(n)$ work."
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "How long does it take to sort an unsorted list with $n$ elements using binary search tree in-order-traversal, if we also tell you that the BST will end up with a height of $h$?"
csq_soln = ["theta(nh)", "O(nh)"]
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_explanation = "See check yourself below."
</question>

<checkyourself>
Do you understand the time complexity for the last question?
<showhide>
We must first construct the BST from our list. It will take $\Theta(h)$ work to perform each insertion into the BST. So performing $n$ insertions will take $\Theta(nh)$ time. You can think about it in terms of the two extreme cases: one where $h = \log(n)$, and the other extreme case where $h = n$.
</showhide>
</checkyourself>

<question pythonliteral>
csq_prompt = """
We have the following BST: \n
             8
          /     \\
         4        14
       /   \\     /   \\
      2      5   10     16    
       \\
        3
Return a Python list of the nodes you encounter when you search for the minimum element in this BST, in the order that you encounter them.
"""
csq_soln = [8, 4, 2]
csq_explanation = "Start at the root, and continue to travel down the left child until there are no more left children."
</question>

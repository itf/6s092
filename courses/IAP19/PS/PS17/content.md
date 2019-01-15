# Readings
Lecture notes 7, 6.006 Fall 2018 on stellar.

Recitation notes 6, 6.006 Fall 2018 on stellar.

# AVL Trees


<question multiplechoice>
csq_prompt = "The height of an AVL tree is:"
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options =  ["$O(n)$",
                "$O(log(n))$",
                "$O(n^2)$",
                "$O(n log(n))$"]
csq_name="qexample1"
</question>

From the F2018 L07 notes:

AVL property: Sub-tree heights of a node's left and right children differ by at most one.

node height: number of edges in the longest path down. (Leaves have height zero, because there are no edges down from the leaves).

node skew $=$  height of right child - height of left child. A missing child contributes height $-1$.

AVL property restated: skew $\in \{-1, 0, 1\}$.

<question multiplechoice>
csq_prompt = '''The following is an AVL tree \n
                10
              /   \\ \n
            4      17
                  /
                 12
'''
csq_renderer = "checkbox"
csq_soln = [1,0]
csq_options =  ["True", "False"]
csq_name="qexample2"
csq_explanation = "Each node's right and left subtrees have a height difference of at most one. The nodes with keys 4 and 12 (leaves) have height 0, the node with key 17 has height 1 (for the edge between 17 and 12) and the node with key 10 has height 2 (the longest path down is 10 to 17 to 2, using two edges)."
</question>

<question multiplechoice>
csq_prompt = '''The following is an AVL tree \n
                10
'''
csq_renderer = "checkbox"
csq_soln = [1,0]
csq_options =  ["True", "False"]
csq_name="qexample3"
csq_explanation = "There are no subtrees of the root (both are 'missing children'), so the skew equals $(-1) - (-1) = 0$."
</question>

<question multiplechoice>
csq_prompt = '''The following is an AVL tree \n
                20  \n
              /    \n
            13                
'''
csq_renderer = "checkbox"
csq_soln = [1,0]
csq_options =  ["True", "False"]
csq_name="qexample4"
csq_explanation = "From the root (with key 20), the left subtree (node with key 13) has height zero (it's a leaf), and there is no right subtree (it's a 'missing child', contributing height $-1$). Skew $= (-1) - (0) = -1$."
</question>

<question multiplechoice>
csq_prompt = '''The following is an AVL tree \n
                23  \n
              /    \n
            18 \n
              \\ \n
              19

'''
csq_renderer = "checkbox"
csq_soln = [0,1]
csq_options =  ["True", "False"]
csq_name="qexample5"
csq_explanation = "The node with key 18 has height 1, and there is no right child of the root (it is a 'missing child' and contributes height $-1$). The root has a skew equal to $(-1) - (1) = -2$. The skew of an AVL tree must be $\in \{-1, 0, 1\}$."
</question>

# Readings
[Lecture notes 7](https://learning-modules.mit.edu/service/materials/groups/238004/files/da11fed6-f37b-4016-8afe-68e3bfef149f/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.

[Recitation notes 6](https://learning-modules.mit.edu/service/materials/groups/238004/files/809a5906-bace-4310-b8f2-7bdeb04d2116/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.

# AVL Trees

Some concepts to keep in mind from the F2018 L07 notes:

* **Node height**: The number of edges in the longest path from that node down to a leaf node in its subtree. (Leaves have height zero, because there are no edges down from the leaves).

* **Tree height**: The **node height** of the root of the tree.

* **AVL property**: The sub-tree heights of a node's left and right children differ by at most one.

* **Node skew**: The height of right child minus the height of left child.

* AVL property restated: node skew for all nodes in the tree $\in \{-1, 0, 1\}$.


<question pythonliteral>
csq_prompt = "How many different trees with elements ${1, 2, 3, 4, 5}$ can be constructed that satisfy both the BST property and the AVL property?"
csq_soln = 6
csq_explanation = "Try drawing the tree diagrams first, and then filling in the numbers"
</question>

<question pythonliteral>
csq_prompt = "What is the minimum possible height of an AVL tree of size $12$? Give an exact numerical answer."
csq_soln = 4
csq_explanation = "Try drawing a complete tree with $12$ elements to make the tree as dense as possible"
</question>

<question pythonliteral>
csq_prompt = "What is the maximum possible height of an AVL tree of size $12$? Give an exact numerical answer."
csq_soln = 5
csq_explanation = "Try maximizing skew for every node."
</question>

<question multiplechoice>
csq_prompt = "Does a max-heap as described in PS15 satisfy the AVL property?"
csq_soln = 'yes'
csq_renderer = 'radio'
csq_options = ['yes', 'no']
csq_explanation = ""
</question>

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

<question multiplechoice>
csq_prompt = "Can an AVL tree have a different height from a complete tree?"
csq_soln = 'yes'
csq_renderer = 'radio'
csq_options = ['yes', 'no']
csq_explanation = "Yes, for example we showed that an AVL tree with $12$ elements could have a height of $5$."
</question>

<question multiplechoice>
csq_prompt = "Can an AVL tree have a different asymptotic height from a complete tree?"
csq_soln = 'no'
csq_renderer = 'radio'
csq_options = ['yes', 'no']
csq_explanation = "No matter what, both AVL trees and complete trees with have heights of $\\Theta(\\log(n))"
</question>

As we've seen, AVL trees of $n$ elements don't all necessarily have the same tree height. Let's try to understand a little more about why it's possible for us to prove that AVL trees have $\Theta(\log(n))$ height. We showed in PS15 that a complete tree has $\Theta(\log(n))$ height. Since this is the densest format for a tree, any AVL tree has $\Omega(\log(n))$ height. Now it suffices to show that an AVL tree must have $\O(\log(n))$ height.

<question multiplechoice>
csq_prompt = "Let $T(h)$ be the minimum number of nodes in an AVL tree of height $h$. What could be the heights of its left and right subtrees, respectively?"
csq_renderer = "checkbox"
csq_options = ["$(h, h-1)$", "$(h-1, h-2)$", "$(h-2, h-1)$", "$(h-1, h-1)$", "$(h-2, h-2)$"]
csq_soln = [0,1,1,0,0]
csq_explanation = ""
</question>

<question expression>
csq_prompt = "If our tree has the minimum number of nodes possible for height $h$, then any subtree will also have the minimum number of nodes possible for its height. Can you write a recurrence formula for $T(h)$ given your answer in the previous problem? Your answer should have the following form of `1 + T(x) + T(y)`. $T(h) =$"
csq_soln = ["1 + T(h-1) + T(h-2)", "1 + T(h-2) + T(h-1)"]
csq_explanation = ""
</question>

<checkyourself>
Can you show that $T(h) \geq 2^{n/2}$?
<showhide>
Your answer in the previous question simplifies to $T(h) \geq 2T(h-2)$, because $T(h-1) \geq T(h-2)$. We use induction: we know that $T(1) \geq 2^0$. Assume that $T(h-2) \geq 2^{(h-2)/2}$. Then 
$$T(h) \geq 2T(h-2) \geq 2 \times 2^{(h-2)/2} = 2^{h/2}$$
What this means is that, given some height $h$, we have a lower-bound for the number $n$ of nodes that would be in the tree. So we have an upper-bound for $h$:
$$ \Rightarrow n \geq T(h) \geq 2^{h/2} \Rightarrow h \leq 2 \times \log_2(n)$$
</showhide>
</checkyourself>


<question multiplechoice>
csq_prompt = '''The following is an AVL tree \n
                10
              /   \\ 
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
csq_prompt = '''The following is an AVL tree 
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
                20  
              /    
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
                23  
              /    
            18 
              \\ 
              19

'''
csq_renderer = "checkbox"
csq_soln = [0,1]
csq_options =  ["True", "False"]
csq_name="qexample5"
csq_explanation = "The node with key 18 has height 1, and there is no right child of the root (it is a 'missing child' and contributes height $-1$). The root has a skew equal to $(-1) - (1) = -2$. The skew of an AVL tree must be $\in \{-1, 0, 1\}$."
</question>

<question expression>
csq_prompt = "Does this rotation maintain the BST property, sike it doesn't. Here are the actual rotations"
csq_soln = "No"
</question>

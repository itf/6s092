<python>
if cs_user_info.get('role') == 'Admin':
    cs_print('-----')
    cs_print(f'Thanks for the help, instructor {cs_user_info.get("name")}')
    cs_print('\n[Spreadsheet link](https://docs.google.com/spreadsheets/d/1GWWiszDQuBBHlHVgy95bNB8cgoFw19jLKdRP_6yNssY/edit?usp=sharing)')
    cs_print('\n[Slack](https://6s092.slack.com)')
    cs_print('\n[Github link](https://github.mit.edu/s092)')
    cs_print('\n-----')

elif cs_user_info.get('role') == 'Cool':
    cs_print('-----')
    cs_print(f'Thanks for the help writing questions and/or on piazza! You are awesome, {cs_user_info.get("name")}')
    cs_print('\n[Github link](https://github.mit.edu/s092)')
    cs_print('\n-----')
elif cs_user_info.get('role') == 'Student':
    cs_print(f'Welcome back, {cs_user_info.get("name")}')
else:
    cs_print(f'Please register using your email, and make your username your kerberos')



</python>

This is the 6.s092 IAP 2020 website. 
Submit code for each problem set here!

Websites for this course include:


* [Code Checker (this!)](#)
* [Stellar](http://stellar.mit.edu/S/course/6/ia20/6.S092/)
* [Piazza](https://piazza.com/mit/other/6s092)
* [Grades](https://s092.xvm.mit.edu/IAP20/grades)


This class is an overview of topics covered in 6.006, geared toward people who have some proofs knowledge. This might help you prepare to take the class in the Spring, review the material if you have already taken it, get some experience for algorithm questions in interviews, or satisfy your curiosity about what all the hype is around algorithms. 

6.006 is an introductory course in algorithms and data structures. It covers
elementary data structures (dynamic arrays, heaps, balanced binary search trees,
hash tables) and algorithmic paradigms (brute force, divide and conquer, greedy,
dynamic programming). The material is applied to classical motivating problems
including searching, sorting, and finding shortest paths in a graph.

This class is not a substitute for 6.006. if you enjoy it, and do well on it, you should take 6.006 afterwards.  A fair comparison would be to say that in this class we will be learning some vocabulary and then practicing those words with flash cards, while in 6.006 you would write beautiful sentences with those words. 

## Schedule and Lectures

The class will meet on Monday and Wednesdays from 8-10 at 1-190. The dates are: W 01/08, M 01/13, W 01/15, W 01/22, M 01/27, and W 01/29.

In the lectures we will very quickly cover an overview of the material, but you will be expected to read notes before and after lectures.




This class is sponsored by Course 6 and by SIPB, the student group that develops Debathena, XVM, Scripts, and many other services on campus. The website for SIPB is here: sipb.mit.edu.

Thanks Jason Ku for allowing us to use the 6.006 notes for this class! 

<!--
Hello.  This is the main page.  Maybe it has a calendar, or weekly
announcements, and links to assignments.

And now I have modified the page.

<python>
print(cs_username)
</python>
-->

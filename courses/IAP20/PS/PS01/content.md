# Readings
Asymptotic Notation and Efficiency sections of Recitation notes 1, 6.006 Fall 2018 on Stellar.


#Asymptotics

##Big O Notation

We say that $f(n) \in O(g(n)$ if there exists $n_0$ and c such that for all $n>n_0$, $f(n) \le cg(n)$, where c is a positive constant.

It is common to write $f(n) = O(g(n))$ instead of $f(n) \in O(g(n))$. Both expressions have the same meaning.

If $f(n) = O(g(n))$, then $g(n)$ is an **assymptotic upper bound** on $f(n)$

That is the same as saying that $\limsup_{x\to \infty} \left|\frac{f(x)}{g(x)}\right| < \infty.$, i.e. this limit is either 0 or a constant.

Order the following functions such that if f is to the left of g, then $f(n) = O(g(n))$. Select all orderings that are correct (there may be more than one).

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

</checkyourself>

## Big $\Omega$

We say that $f(n) \in \Omega(g(n)$ if there exists $n_0$ and c such that for all $n>n_0$, $cf(n) \ge g(n)$, where c is a positive constant.

If $f(n) = \Omega(g(n))$, then $g(n)$ is an **assymptotic lower bound** on $f(n)$

That is the same as saying that $\limsup_{x\to \infty} \left|\frac{g(x)}{f(x)}\right| < \infty.$, i.e. this limit is either 0 or a constant.

Order the following functions such that if f is to the left of g, then $f(n) \in \Omega(g(n))$. Select all orderings that are correct.

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


## $\Theta$

We say that $f(n) \in \Theta(g(n)$ if $f(n) \in O(g(n))$ and $f(n) \in \Omega(g(n)$

If $f(n) = \Theta(g(n))$, then $g(n)$ is an **assymptotic tight bound** on $f(n)$

Choose the groups such that for any 2 functions in the groups, $f(n)$, $g(n)$, we have $f(n) \in \Theta(g(n)$

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


## Small $o$ and small $\omega$

We say that $f(n) \in o(g(n))$ if there exists $n_0$ and c such that for all $n>n_0$, $f(n) < cg(n)$, where c is a positive constant.

The only difference with $O$ is that now we have a strict inequality. This is the same as saying $$f(n) \in o(g(n)) \iff  f(n) \not \in \Omega(g(n))$$


Similarly,

$$f(n) \in \omega(g(n)) \iff  f(n) \not \in O(g(n))$$

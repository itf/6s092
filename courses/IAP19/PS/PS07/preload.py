cs_long_name = 'Sorting'
cs_release_date = '2019-01-07:23:00'
cs_due_date = '2019-02-06:23:00'
#csq_allow_viewanswer = False
csq_allow_viewexplanation = True

#extra functions, to be able to do some of the problems:
csq_funcs = {"T": (lambda c: c**3*0.6006+c**2, lambda  c:  r"%s(%s)" % ("T", ", ".join(c)) ),
"O": (lambda c: c**3*1.6006-c**2, lambda  c:  r"%s(%s)" % ("O", ", ".join(c)) ),
"theta": (lambda c: -c**3*0.06006+c**2*0.2, lambda  c:  r"%s(%s)" % ("\\theta", ", ".join(c)) )}


# def csq_allow_submit(context):
#     # only allow submissions until feb 17th at 11pm
#     return context['cs_now'] < context['csm_time'].realize_time(context, '2018-02-17:23:00')

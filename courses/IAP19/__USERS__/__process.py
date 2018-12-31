staff = [
#    'edemaine',
#    'jasonku',
#    'zabel',
    #
#    'mcoulomb',
    'ivanaf',
#    'vivekm',
    'asahoo',
    'stefren',
#    'mcoulomb',
    'ivanaf',
    'ckguo',
#    'alexkatz',
#    'vivekm',
    'prekshan',
#    'pnoyola',
    'stefren',
    'rewang',
    'justinej',
]

awesomehelp = [
'levyr',
'aeg',
'gschwind'
]

# Add Staff

for s in staff:
    with open(s + '.py', 'w+') as g:
        g.write("role = 'Admin'")

for s in awesomehelp:
    with open(s + '.py', 'w+') as g:
        g.write("role = 'Admin'")



# Add Students



if False:
    with open('students.csv', 'r') as f:
        for line in f:
            email = line.split(',')[0]
            athena = email.split('@')[0]
            with open(athena + '.py', 'w+') as g:
                g.write("role = 'Student'")

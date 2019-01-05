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
'gschwind',
'ikdc'
]


piazza = [
'darnellg',
'damianb',
'skarnik',
'skandera',
'ckonicki',
'dudo',
'xmzhou',
'zanderso',
'himawan',
'austein',
'linx3',
'mzarate',
'digalaki',
'aroot222',
'ikdc',
'vilhelm',
'edwardf',
'jeffery'
]

questions = [
'skarnik',
'skandera',
'ckonicki',
'zanderso',
'himawan',
'austein',
'digalaki',
'aroot222',
'ikdc'
]

# Add cool. Cool can view all questions all the time,
# can submit questions before and after deadlines.

for s in piazza:
    with open(s + '.py', 'w+') as g:
        g.write("role = 'Cool'")

for s in questions:
    with open(s + '.py', 'w+') as g:
        g.write("role = 'Cool'")



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

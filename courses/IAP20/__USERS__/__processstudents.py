
# Add Students



if True:
    with open('students.csv', 'r') as f:
        for line in f:
            email = line.split(',')[0]
            athena = email.split('@')[0]
            with open(athena + '.py', 'w+') as g:
                g.write("role = 'Student'")




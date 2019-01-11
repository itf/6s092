<python>
if cs_user_info.get('role') == 'Admin':
    cs_print('-----')
    cs_print(f'Thanks for the help, instructor {cs_user_info.get("name")}')
    cs_print('\n[Spreadsheet link](https://docs.google.com/spreadsheets/d/1maqwzCU-fZ2zkW5ygfOdAKmC4PZA0DMtWjPlLTyyeRk/edit#gid=1123195996)')
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



</python>

This is the staging area for 6.s092. For testing things that will likely break everything


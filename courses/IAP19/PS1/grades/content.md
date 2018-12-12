<python>
from os import path as osPath
from json import dumps as jsonDumps
from urllib.parse import urlencode

users = sorted(csm_util.list_all_users(globals(), cs_course))
assignment = [cs_course, 'PS1']
q = 'q000000'

# print(cslog.read_log('parky', assignment, 'problemstate'))

# Change a Log
# 
# log = cslog.read_log('jasonku', assignment, 'problemstate')[0]
# log['scores'][q] = 0.7
# cslog.overwrite_log('jasonku', assignment, 'problemstate', log)
# cslog.overwrite_log('jgil', assignment, 'problemstate', {})
# print(cslog.read_log('jgil', assignment, 'problemstate'))

# [{'last_submit_time': '2018-02-14:11:27:26.969078', 
#   'last_submit_times': {'q000000': '2018-02-14:11:27:26.969078'}, 
#   'cached_responses': {'q000000': '\n \xa0Your score on your most recent submission was: 70.00%\n Show/Hide Detailed Results '}, 
# 'score_displays': {'q000000': '70.00%'}, 
# 'scores': {'q000000': 0.7}, 
# 'answer_viewed': {'q000000'}, 
# 'nsubmits_used': {'q000000': 210}, 
# 'explanation_viewed': set(), 
# 'checker_ids': {}, 
# 'extra_data': {'q000000': None}, 
# 'last_submit_id': {'q000000': '65c09244-49a4-4588-aad9-ee546eb2c242'}, 
# 'last_submit': {'q000000': ['find_peak_2D_bf.py', '6.006/PS1/jasonkuq0000001518625647.7789740bb18988eb36fbbf8c37592fcc5f993afind_peak_2D_bf.py']}, 
# 'timestamp': '2018-02-14:11:27:26.969078'}]

data = {
    user: {
        'role': None,
        'grade': 0, 
        'time': None, 
        'filename': None, 
        'href': None, 
        'n': None,
        'answer': 'N',
    }
    for user in users
} 
for user in users:
    data[user]['role'] = csm_util.read_user_file(globals(), cs_course, user)['role']
    log = cslog.read_log(user, assignment, 'problemstate')
    if len(log) < 1:
        continue
    log = log[0]
    if 'timestamp' in log:
        data[user]['time'] = log['timestamp']
    if 'scores' in log and log['scores'][q]:
        data[user]['grade'] = log['scores'][q]
    if 'nsubmits_used' in log and log['nsubmits_used'][q]:
        data[user]['n'] = log['nsubmits_used'][q]
    if 'answer_viewed' in log and log['answer_viewed'] == q:
        data[user]['answer'] = 'Y'
    if 'last_submit' in log and q in log['last_submit']:
        data[user]['filename'] = log['last_submit'][q]
        if 2 == len(log['last_submit'][q]):
            data[user]['filename'], loc = log['last_submit'][q]
            loc = osPath.basename(loc)
            path = urlencode({'path': jsonDumps(assignment), 'fname': loc})
            data[user]['href'] = '%s/_util/get_upload?%s' % (cs_url_root, path)

print('''<table border='1px solid black'>
<tr>
  <td><b>user</b></td>
  <td>role</td>
  <td>score</td>
  <td>weighted</td>
  <td>number submits</td>
  <td>last submission</td>
  <td>timestamp</td>
</tr>''')
for user in sorted(users, key = lambda u: data[u]['role']):
    dat = data[user]
    if dat['time']:
        print('<tr><td>')
        print('<a href="http://alg.mit.edu/fall18/PS1?as=%s">' % user)
        print('<b>%s</b>' % user)
        print('</a>')
        print('</td>')
        print('<td>%s</td>' % dat['role'])
        print('<td>%s</td>' % dat['grade'])
        print('<td>%s</td>' % int(dat['grade'] * 25))
        print('<td>%s</td><td>' % dat['n'])
        if dat['filename']:
            print('<a href="%s" download="%s">' % (dat['href'], dat['filename']))
            print('%s</a>' % dat['filename'])
        print('</td><td>%s</td>' % dat['time'])
        # print('<td>%s</td>' % dat['answer'])
        print('</tr>\n')
print('</table>\n')
for user in sorted(data.keys()):
    if data[user]['role'] == 'Student':
        late = 'none' 
        if data[user]['time']:
            late = 'late'
            if str(data[user]['time']) < '2018-09-13:23:15.000000':
                late = 'on time'
        print('%s,%s,%s<br />' % (user, int(data[user]['grade'] * 25), late))
</python>

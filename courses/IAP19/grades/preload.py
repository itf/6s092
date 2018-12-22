cs_long_name = 'Grades and Progress'

from bs4 import BeautifulSoup
from collections import defaultdict


# def csq_allow_submit(context):
#     # only allow submissions until feb 17th at 11pm
#     return context['cs_now'] < context['csm_time'].realize_time(context, '2018-02-17:23:00')


def generate_page_dispatcher():
    '''
    Decides what to do. Show all info, only show a single user infor, show summary, etc.
    '''

    perms = cs_user_info.get("permissions", [])
    if "whdw" not in perms:
        generate_page_for_user(cs_username)
    else:
        if 'user' in cs_form:
            username = cs_form['user']
            print("{user} progress page.\n".format(user=username))
            generate_page_for_user(username)
        elif 'pset' in cs_form:
            pset = cs_form['pset']
            print("{pset} progress page \n".format(pset=pset))
            generate_page_for_pset(pset)
        else:
            generate_summary_page_for_us()




def generate_page_for_student():
    print("You are not allowed to view this page yet.")


def get_pset_from_path(path):
    return '/'.join(path)

def get_path_from_pset(pset):
    return pset.split('/')

def get_pset_paths():
    ## Get list of problems. Assume all of them are in folder PS
    pset = sorted(csm_loader.get_subdirs(globals(), cs_course, ['PS']))
    pset_paths = [['PS'] + [x] for x in pset]
    return pset_paths

def get_usernames():
    usernames = csm_util.list_all_users(globals(), cs_course)
    return usernames

def get_students():
    usernames = csm_util.list_all_users(globals(), cs_course)
    users = [
        csm_util.read_user_file(globals(), cs_course, username, {})
        for username in usernames
    ]
    no_section = globals().get("cs_whdw_no_section", False) 
    students = [
        user
        for user in users
        if user.get("role", None) in ["Student", "SLA"]
        and (no_section or str(user.get("section", "default")) == section)
    ]
    return students


def get_user_score_psets(user, pset_paths):
    user_score_dict = {}
    for path in pset_paths:
        pset_name = get_pset_from_path(path)
        x = csm_tutor.compute_page_stats(globals(), user, [cs_course] + path, ['state' ])
        scores = x['state'].get("scores", {})
        user_score = sum([scores[q] for q in scores])
        user_score_dict[pset_name] = user_score
    return user_score_dict


def get_total_score_psets(pset_paths):
    pset_full_scores = defaultdict(lambda : 0)
    #Get full score of questions:
    for path in pset_paths:
        pset_name = get_pset_from_path(path)
        x = csm_tutor.compute_page_stats(globals(), cs_username, [cs_course] + path, ['question_info'])
        question_info =  x['question_info']
        for question_name, qinfo in question_info.items():
            pset_full_scores[pset_name] += qinfo['csq_npoints']
    return pset_full_scores


def print_table_user(user, pset_full_scores, user_scores_problemset):
    soup = BeautifulSoup("", "html.parser")
    table = soup.new_tag("table")
    table["class"] = "table table-bordered"
    header = soup.new_tag("tr")
    for heading in ["user", "score"]:
        th = soup.new_tag("th")
        th.string = heading
        header.append(th)
    table.append(header)

    for name, score in sorted(users_total.items()):
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        a = soup.new_tag(
            "a", href="?user={}".format(name)
        )
        a.string = name # link to user info

        td.append(a)
        td["class"] = "text-left"
        tr.append(td)

        td = soup.new_tag("td")
        td.string = "{score}/{total} ({percent:.2%})".format(
                score=score,
                total=total,
                percent=(score / total) if total != 0 else 1,
            )
        td["class"] = "text-right"
        tr.append(td)
        table.append(tr)

    soup.append(table)
    print(str(soup))


def print_user_summary_table(pset_full_scores, users_scores_problemset):

    #get total user score:
    users_total = defaultdict(lambda: 0)
    for user, problemsets in users_scores_problemset.items():
        users_total[user] = sum([score for problemset,score in problemsets.items()])

    #get total score of psets
    total = sum([score for problemset_name, score in pset_full_scores.items()])

    #Now we have to print the info. First
    soup = BeautifulSoup("", "html.parser")
    table = soup.new_tag("table")
    table["class"] = "table table-bordered"
    header = soup.new_tag("tr")
    for heading in ["user", "score"]:
        th = soup.new_tag("th")
        th.string = heading
        header.append(th)
    table.append(header)

    for name, score in sorted(users_total.items()):
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        a = soup.new_tag(
            "a", href="?user={}".format(name)
        )
        a.string = name # link to user info

        td.append(a)
        td["class"] = "text-left"
        tr.append(td)

        td = soup.new_tag("td")
        td.string = "{score}/{total} ({percent:.2%})".format(
                score=score,
                total=total,
                percent=(score / total) if total != 0 else 1,
            )
        td["class"] = "text-right"
        tr.append(td)
        table.append(tr)

    soup.append(table)
    print(str(soup))


def print_pset_summary_table(pset_full_scores, users_scores_problemset):
    #First get max_pset_score, i.e sum of points users could get
    total_users = len(users_scores_problemset)
    pset_max_scores = {pset_name: score*total_users 
            for pset_name, score in pset_full_scores.items()}

    #now get sum of students score.
    pset_user_score_sum = defaultdict(lambda: 0)

    for _, problemset_scores in users_scores_problemset.items():
        for pset_name, score in problemset_scores.items():
            pset_user_score_sum[pset_name] += score



    soup = BeautifulSoup("", "html.parser")
    table = soup.new_tag("table")
    table["class"] = "table table-bordered"
    header = soup.new_tag("tr")
    for heading in ["pset", "score"]:
        th = soup.new_tag("th")
        th.string = heading
        header.append(th)
    table.append(header)

    for name, score in sorted(pset_user_score_sum.items()):
        total = pset_max_scores[name]
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        a = soup.new_tag(
            "a", href="?pset={}".format(name)
        )
        a.string = name # link to user info

        td.append(a)
        td["class"] = "text-left"
        tr.append(td)

        td = soup.new_tag("td")
        td.string = "{score}/{total} ({percent:.2%})".format(
                score=score,
                total=total,
                percent=(score / total) if total != 0 else 1,
            )
        td["class"] = "text-right"
        tr.append(td)
        table.append(tr)

    soup.append(table)
    print(str(soup))




def print_user_table(username, pset_full_scores, user_score_problemset):
    spoof = '' #To see the psets as if it was the student
    perms = cs_user_info.get("permissions", [])
    if "whdw" in perms:
        spoof = '?as={username}'.format(username=username)


    soup = BeautifulSoup("", "html.parser")
    table = soup.new_tag("table")
    table["class"] = "table table-bordered"
    header = soup.new_tag("tr")
    for heading in ["pset", "score"]:
        th = soup.new_tag("th")
        th.string = heading
        header.append(th)
    table.append(header)

    for name, score in sorted(user_score_problemset.items()):
        total = pset_full_scores[name]
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        a = soup.new_tag(
            "a", href="COURSE/{path}{spoof}".format(path=name, spoof=spoof)
        )
        a.string = name # link to user info

        td.append(a)
        td["class"] = "text-left"
        tr.append(td)

        td = soup.new_tag("td")
        td.string = "{score}/{total} ({percent:.2%})".format(
                score=score,
                total=total,
                percent=(score / total) if total != 0 else 1,
            )
        td["class"] = "text-right"
        tr.append(td)
        table.append(tr)

    soup.append(table)
    print(str(soup))


def print_pset_table(pset, pset_full_scores, user_score_problemset):
    allow_spoof = False #To see the psets as if it was the student
    perms = cs_user_info.get("permissions", [])
    if "whdw" in perms:
        allow_spoof = True

    soup = BeautifulSoup("", "html.parser")
    table = soup.new_tag("table")
    table["class"] = "table table-bordered"
    header = soup.new_tag("tr")
    for heading in ["pset", "score"]:
        th = soup.new_tag("th")
        th.string = heading
        header.append(th)
    table.append(header)

    for name, score in sorted(user_score_problemset.items()):
        if allow_spoof:
            spoof = '?as={username}'.format(username=name)

        total = pset_full_scores[name]
        tr = soup.new_tag("tr")
        td = soup.new_tag("td")
        a = soup.new_tag(
            "a", href="COURSE/{path}{spoof}".format(path=pset, spoof=spoof)
        )
        a.string = name # link to user info

        td.append(a)
        td["class"] = "text-left"
        tr.append(td)

        td = soup.new_tag("td")
        td.string = "{score}/{total} ({percent:.2%})".format(
                score=score,
                total=total,
                percent=(score / total) if total != 0 else 1,
            )
        td["class"] = "text-right"
        tr.append(td)
        table.append(tr)

    soup.append(table)
    print(str(soup))

def generate_summary_page_for_us():

    ## Get list of problems.
    pset_paths = get_pset_paths()

    ## Get list of students / usernames if debugging
    students = get_usernames() #get_students() 


    #Get full score of questions by accessing the questions available by the current user
    pset_full_scores = get_total_score_psets(pset_paths)

    #Calculate the score of each user in each problem set
    users_score_problemsets = {}

    for user in sorted(students):
        users_score_problemsets[user] = get_user_score_psets(user, pset_paths)


    print_user_summary_table(pset_full_scores, users_score_problemsets)
    print_pset_summary_table(pset_full_scores, users_score_problemsets)
  

def generate_page_for_user(user):
    pset_paths = get_pset_paths()
    pset_full_scores = get_total_score_psets(pset_paths)
    user_score_problemset = get_user_score_psets(user, pset_paths)
    print_user_table(user, pset_full_scores, user_score_problemset)

def generate_page_for_pset(pset):
    pset_paths = [get_path_from_pset(pset)]
    pset_full_scores = get_total_score_psets(pset_paths)
    users_score_problemset = {}

    students = get_usernames()

    for user in sorted(students):
        user_scores =  get_user_score_psets(user, pset_paths)
        users_score_problemset[user] = user_scores[pset]

    print_pset_table(pset, pset_full_scores, users_score_problemset)
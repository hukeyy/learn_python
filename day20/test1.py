# -*- coding: utf-8 -*-
# Author: hkey
import shelve, datetime, hashlib, time

LOGIN_TIME_OUT = 60
db = shelve.open('user_shelve.db', writeback=True)

def newuser():
    global db
    prompt = "login desired: "
    while True:
        name = input(prompt)
        if name in db:
            prompt = "name taken, try another: "
            continue
        elif len(name) == 0:
            prompt = "name should not be empty, try another: "
            continue
        else:
            break

    pwd = input('password:')
    db[name] = {'password': pwd, 'last_login_time': time.time()}

def olduser():
    global db
    name = input('login:')
    pwd = input('password:')
    try:
        password = db.get(name).get('password')
    except AttributeError as e:
        print('\033[31;1mUsername %s doesn\'t existed\033[0m')
        return
    if pwd == password:
        login_time = time.time()
        last_login_time = db.get(name).get('last_login_time')
        if login_time - last_login_time < LOGIN_TIME_OUT:
            print('\033[31;1mYou already logged in at: <%s>\033[0m'
                  % datetime.datetime.fromtimestamp(last_login_time).isoformat())

        db[name]['last_login_time'] = login_time
        print('\033[32;1mwelcome back\033[0m', name)
    else:
        print('login incorrect')

def showmenu():
    #print '>>>', db
    global db
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice: """
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = "q"
            print("\nYou picked: [%s]" % choice)
            if choice not in "neq":
                print("invalid option, try again")
            else:
                chosen = True

        if choice == "q": done = True
        if choice == "n": newuser()
        if choice == "e": olduser()
    db.close()

if __name__ == "__main__":
    showmenu()











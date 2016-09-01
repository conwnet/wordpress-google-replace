import os, re

def dfs(f):
    if os.path.isfile(f):
        try:
            s1 = 'fonts.googleapis.com'
            s = open(f).read()
            if s1 in s:
                print(f)
                s = s.replace(s1, 'fonts.useso.com')
                with open(f, 'w') as ff:
                    ff.write(s)
        except:
            pass
    else:
        for g in os.listdir(f):
            dfs(f + '/' + g)

dfs('.')


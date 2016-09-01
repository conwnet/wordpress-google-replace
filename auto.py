import os

def dfs(f, s, t):
    if f == './auto.py':
        return
    if os.path.isfile(f):
        try:
            ss = open(f).read()
            if s in ss:
                print('find out \'' + s + '\' in ' + f + ', replace it as \'' + t + '\'')
                ss = ss.replace(s, t)
                with open(f, 'w') as ff:
                    ff.write(ss)
        except:
            pass
    else:
        for g in os.listdir(f):
            dfs(f + '/' + g, s, t)

dfs('.', 'fonts.googleapis.com', 'fonts.useso.com')
dfs('.', '\'http://%d.gravatar.com/avatar/%s\', $gravatar_server', '\'http://cn.gravatar.com/avatar/%s\'')


def ask_ok (prompt, retries=4, complaint='yes or no, please!'):
    while True:
        ok=raw_input(prompt)
        if ok in ('y','ye','yes'): return True
        if ok in ('n','no','nop','nope'): return False
        retries = retries -1
        if retries<0: raise IOError, 'refusenik user'
        print complaint
i=5
def f(arg=i):
    print arg
i=6
f()
z=ask_ok('really quit6???')

if z==False:
    print "bad"
        

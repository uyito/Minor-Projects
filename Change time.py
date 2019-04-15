import random
times = ['12:02:24PM', '12:09:23AM', '07:24:45PM', '07:44:30AM']
time = random.choice(times)


def timeConversion(s):
    t = s[0:2]
    p = s[8:10]

    if p == 'AM' and t != '12':
        y = s[0:8]
        return y
    elif p == 'AM' and t == '12':
        k = (s.replace(s[0:2], '00'))
        n = k[0:8]
        return n
    elif p == 'PM' and t == '12':
        y = s[0:8]
        return y
    else:
        b = int(t)
        z = b + 12
        m = str(z)
        k = (s.replace(s[0:2], m))
        n = k[0:8]
        return n
        # print(type(z))
        # print(z, s[2:8])


print (timeConversion(time))
from datetime import datetime, timedelta

def data():
    twoweeks_ago = timedelta(days=-14) + datetime.now()
    return twoweeks_ago.strftime('Year: %Y, Month: %B, Day: %d, Time: %X%p')

if __name__=='__main__':
    print(data())


from datetime import datetime, timedelta

def data():
    oneweek_ago = timedelta(days=-7) + datetime.now()
    return oneweek_ago.strftime('Year: %Y, Month: %B, Day: %d, Time: %X%p')

if __name__=='__main__':
    print(data())
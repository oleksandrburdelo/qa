from datetime import datetime, timedelta


def data():
    # oneweek_ago = timedelta(days=-7) + datetime.now()
    onekweek_ago = datetime.now() - timedelta(days=7)
    return oneweek_ago.strftime('Year: %Y, Month: %B, Day: %d, Time: %X%p')


if __name__=='__main__':
    print(data())

# Good

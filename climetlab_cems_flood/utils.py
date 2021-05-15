from datetime import datetime,timedelta


def get_date_index(start =[2019,1,1],end=[2019,12,31]):

    start, end = datetime(*start),datetime(*end)
    days = [start + timedelta(days=i) for i in range((end - start).days + 1)]
    index = [list(map(str.lower,d.strftime("%B-%d").split("-")))  for d in days if d.weekday() in [0,3] ] 
 
    return index



def parser():
    

class Parser:

    def 
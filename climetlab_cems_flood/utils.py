from datetime import datetime, timedelta
import typing as T
import re

M = ["%02d"%d for  d in range(1,13)]
Y = [str(d) for d in range(2000,2019)]
D = ["%02d"%d for  d in range(1,32)]

def ensure_list(l):
    if isinstance(l,list):
        return l
    else:
        return [l]

def parser_time_index(start=[2019, 1, 1], end=[2019, 12, 31]):

    start, end = datetime(*start), datetime(*end)
    days = [start + timedelta(days=i) for i in range((end - start).days + 1)]
    index = [
        list(map(str.lower, d.strftime("%B-%d").split("-")))
        for d in days
        if d.weekday() in [0, 3]
    ]

    return index


class Parser:

    def __init__(self):
        pass

    @staticmethod
    def leadtime(string):

        s = string.split("/")

        ret = []
        for chunk in s:
            start, end = chunk.split("-")
            ret.extend(list(map(str, range(int(start), int(end) + 24, 24))))

        return ret

    @staticmethod
    def period(string):

        PATTERN = {"[0-9]{8}":{}, # most frequent
                "\*[0-9]{2}[0-9]{2}":[Y,string[1:3],string[3:]],
                "[0-9]{4}\*[0-9]{2}":[string[:4],M,string[5:]],
                "[0-9]{4}[0-9]{2}\*":{"D":D},
                "[0-9]{4}\*\*":{"M":M,"D":D},
                "\*[0-9]{2}\*":{"Y":Y,"D":D},
                "\*\*[0-9]{2}":{"Y":Y,"M":M},
                "\*\*\*":{"Y":Y,"M":M,"D":D}}

        s = string.split("/")


        if "*" in string:
            years = set()
            months = set()
            days = set()     
            match = None
            for p in PATTERN:
                if re.match(p,string):
                    break
                
            years,months,days = PATTERN[p]

            return sorted(ensure_list(years)), sorted(ensure_list(months)), sorted(ensure_list(days))

        else:
            years = set()
            months = set()
            days = set()
            for chunk in s:
                start, end = chunk.split("-")
                start = datetime.strptime(start, "%Y%m%d")
                end = datetime.strptime(end, "%Y%m%d")
                period = [
                    start + timedelta(days=x) for x in range(0, (end - start).days + 1)
                ]
                years.update([i.strftime("%Y") for i in period])
                months.update([i.strftime("%m") for i in period])
                days.update([i.strftime("%d") for i in period])

            return sorted(list(years)), sorted(list(months)), sorted(list(days))



def months_num2str(months: T.List[str]):
    mapping = {"01":"january","02":"february","03":"march","04":"april","05":"may",
               "06":"june","07":"july","08":"august","09":"september","10":"october",
              "11":"november","12":"december"}
    return [mapping.get(m) for m in months if mapping.get(m)]
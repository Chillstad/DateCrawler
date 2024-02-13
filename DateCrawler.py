from googlesearch import search
from htmldate import find_date

class DateCrawler:
    _wait_time = 1
    _depth = 10
    
    def __init__(self, wait_time, depth):
        _wait_time = wait_time
        _depth = depth

    def average(arr):
        size = len(arr)
        total = 0
        for i in arr:
            total += int(i)
        if size < 1:
            return -1
        return total / size

    def median(arr):
        uniques = {}
        for item in arr:
            if not item in uniques.keys():
                uniques[item] = 0
            else:
                uniques[item] += 1

        return max(uniques)
    
    def print_data(data):
        print("Average appearance year:", DateCrawler.average(data))
        print("Most recent appearance:", max(data))
        print("Median appearance:", DateCrawler.median(data))

    def search(self, target):
        dates = []
        for site in search("\"%s\"" % target, "co.in", num=25, stop=25, pause=0.5):
            try:
                date = find_date(site, outputformat="%Y")
                if date != None:
                    dates.append(date)
            except:
                pass
        DateCrawler.print_data(dates)





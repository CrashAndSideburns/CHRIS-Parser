import re

class Author():
    def __init__(self,last_name,first_name):
        self.last_name = last_name
        self.first_name = first_name

class Date():
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

class Chris():
    def __init__(self,quote,author,date,context):
        self.quote = quote
        self.author = author
        self.date = date
        self.context = context

REGEX = re.compile(r'{\s*quote:\s*"([^"]*)"\s+author:\s*{\s*last_name:\s*"([^"]*)"\s+first_name:\s*"([^"]*)"\s*}\s+date:\s*({\s*year:\s*(\d{4})\s+month:\s*(\d{1,2})\s+day:\s*(\d{1,2})\s*})?(\s+context:\s*"([^"]*)")?\s*}')

def parse(filename):
    with open(filename,"r") as chris_file:
        groups = re.search(REGEX,chris_file.read())
        if groups:
            author = Author(groups.group(2),groups.group(3))
            date = Date(groups.group(5),groups.group(6),groups.group(7))
            return Chris(groups.group(1),author,date,groups.group(9))
        else:
            raise Exception('InvalidFile')
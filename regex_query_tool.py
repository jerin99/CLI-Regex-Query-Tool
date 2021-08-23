import re
from prettytable import PrettyTable

class search:
    def __init__(self):
        self.string = input(r'Enter your text from which you want to search : ')
        self.pattern = input('Enter your text to search : ')
        print('1. Start\n2. End\n3. Any Position')
        self.pos = int(input('Where do you want to search the pattern : '))
                
        if self.pos==1:
            self.run_search_on_start(self.string, self.pattern)
        elif self.pos==2:
            self.run_search_on_end(self.string, self.pattern)
        elif self.pos==3:
            print('1. First occurance\n2. All occurances')
            self.no = int(input('How many occurances do you want to search : '))
            self.run_search_on_anyPos(self.string, self.pattern, self.no)
        else:
            print('Invalid input')
        
    def run_search_on_anyPos(self, text, pattern, occurances):
        regex = pattern
        if occurances==1:
            table = PrettyTable()
            table.field_names = ['Start Index', 'End Index', 'Match String']
            match = re.finditer(regex, text)
            if match:
                for i in match:
                    start = i.start()
                    end = i.end()
                    table.add_row([start, end, text[start:end]])
                    print(table)
                    break
            else:
                print('No match found')

        elif occurances==2:
            table = PrettyTable()
            table.field_names = ['Start Index', 'End Index', 'Match String']
            match = re.finditer(regex, text)
            if match:
                for i in match:
                    start = i.start()
                    end = i.end()
                    table.add_row([start, end, text[start:end]])
                print(table)
            else:
                print('No match found')
                    

    def run_search_on_start(self, text, pattern):
        pattern = '\A'+pattern
        regex = re.compile(pattern)
        match = re.search(regex, text)
        if match:
            start = match.span()[0]
            end = match.span()[1]
            table = PrettyTable()
            table.field_names = ['Start Index', 'End Index', 'Match String']
            table.add_row([start, end, text[start:end]])
            print(table)
        else:
            print('No match found')
    def run_search_on_end(self, text, pattern):
        pattern = pattern+'$'
        regex = re.compile(pattern)
        match = re.search(regex, text)
        if match:
            start = match.span()[0]
            end = match.span()[1]
            table = PrettyTable()
            table.field_names = ['Start Index', 'End Index', 'Match String']
            table.add_row([start, end, text[start:end]])
            print(table)
        else:
            print('No match found')
    
        
    
s = search()
import re
import sys

def get_date(data):
    
    pattern = '((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-3]{0,1}\d,{0,1} [1|2]\d{3})|([0_3]{0,1}\d{0,1} {0,1}(January|February|March|April|May|June|July|August|September|October|November|December){0,1} [1|2]\d{3})|(\d{1,2}/\d{1,2}/[1|2]\d{3})|([1|2]\d{3}-\d{1,2}-\d{1,2})|([1|2]\d{3}-[1|2]\d{3})'
    years = []
    with open(data) as f:
        lines = f.readlines()
        ID = len(lines)
        for i,l in zip(range(ID), lines):
            match = re.search(pattern, l)
            if match:
                print (i,match.group(0))
            

if __name__ == "__main__": 
        
    if len(sys.argv) != 2:
        print ('usage:',sys.argv[0],'[filename]')
        sys.exit()

    data = sys.argv[1]
    get_date(data)

import enum
from tokenize import blank_re

comment_cnt = 0
loc_cnt = 0 
mline_cnt = 0
blankline_cnt = 0


with open( "mem_map.h",'r') as file:
    for l_no, line in enumerate(file):
        
        #search multiline comment
        if "/*" in line:
            mline_cnt = l_no
            continue

        if "*/" in line:
            mline_cnt = l_no - mline_cnt + 1
            comment_cnt += mline_cnt
            continue

        if "//" in line:
            comment_cnt += 1
            continue
        
        #check empty line
        if line.strip():
            loc_cnt += 1
            continue
        else:
            blankline_cnt +=1




print(f"Number of comments: {comment_cnt}")
print(f"Number of LOC: {loc_cnt}")
print(f"Number of blank lines: {blankline_cnt}")




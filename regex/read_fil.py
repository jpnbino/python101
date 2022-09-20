import enum
import re

comment_cnt = 0
loc_cnt = 0 
mline_cnt = 0
blankline_cnt = 0
is_multiline = 0

with open( "tsl2561_lux_calculus.c",'r') as file:
    for l_no, line in enumerate(file):
        
        #search multiline comment
        if "/*" in line:

            line = line.strip()
            match = (re.search("/\*", line))
            print(l_no, match)
            
            if ( match.start() != 0):
                loc_cnt += 1

            if "*/" in line:
                comment_cnt += 1    
            else:
                mline_cnt = l_no
                is_multiline = 1
            continue

        if "*/" in line:
            mline_cnt = l_no - mline_cnt + 1
            comment_cnt += mline_cnt
            is_multiline = 0
            continue

        if is_multiline:
            continue

        if "//" in line:
            comment_cnt += 1
            line = line.strip()
            match = (re.search("//", line))
            
            if ( match.start() != 0):
                loc_cnt += 1
                
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




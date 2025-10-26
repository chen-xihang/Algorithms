def substring_occurrence(main_string, sub_string):
    if not len(sub_string) == 3:
        return None
    n = len(main_string)
    count = 0

    for i in range(n):
        if main_string[i]==sub_string[0]:
            for j in range(i+1, n):
                if main_string[j] == sub_string[1]:
                    for k in range(j+1, n):
                        if main_string[k] == sub_string[2]:
                            count += 1
    
    return count

substring_occurrence("SSQHUL", "SHL")
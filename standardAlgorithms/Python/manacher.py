def transform_string(s):
    ans = ["^"]
    for c in s:
        ans.append("#")
        ans.append(c)
    ans.append("#$")
    return "".join(ans)

def manacher(s):
    s_transformed = transform_string(s)
    P = [0] * len(s_transformed)
    right = 0
    centre = 0

    best_radius = 0
    best_centre = 0

    for i in range(1, len(s_transformed)-1):
        if i < right:
            P[i] = min(P[2*centre-i], right - i)
        while s_transformed[i+P[i]+1] == s_transformed[i-P[i]-1]:
            P[i] +=1 
        if ((P[i] + i) > right):
            centre = i
            right = P[i]+i
        if P[i] > best_radius:
            best_radius = P[i]
            best_centre = i
        if right == len(s_transformed)-2:
            break 
    
    start = (best_centre - best_radius) // 2
    return s[start:start+best_radius]

if __name__ == "__main__":
    print(manacher("ababa"))  
    print(manacher("abacdfgdcaba"))  
    print(manacher("abacdfgdcabba"))  

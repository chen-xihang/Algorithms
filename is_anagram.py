def is_anagram(a, b):
    if not len(a) == len(b):
        return False
    count = {}
    for c in a:
        count[c] = count.get(c, 0) + 1
    
    for c in b:
        if c in count:
            count[c] = count[c]-1
            if count[c]<0:
                return False
        else:
            return False
    
    if not all(val == 0 for val in count.values()):
        return False
    
    return True
        
# Only runs when this file is executed directly
if __name__ == "__main__":
    print("✅ Basic True Cases")
    print(is_anagram("listen", "silent"))      # True
    print(is_anagram("anagram", "nagaram"))    # True
    print(is_anagram("aabb", "bbaa"))          # True
    print(is_anagram("abc", "cab"))            # True
    print(is_anagram("debitcard", "badcredit"))# True

    print("\n❌ Basic False Cases")
    print(is_anagram("rat", "car"))            # False
    print(is_anagram("hello", "bello"))        # False
    print(is_anagram("aabb", "abbb"))          # False
    print(is_anagram("abc", "abcd"))           # False
    print(is_anagram("abc", "abd"))            # False

    print("\n🧠 Edge Cases")
    print(is_anagram("", ""))                  # True
    print(is_anagram("a", "a"))                # True
    print(is_anagram("a", "b"))                # False
    print(is_anagram("aa", "a"))               # False

    print("\n🔠 Case Sensitivity")
    print(is_anagram("Listen", "Silent"))      # False
    print(is_anagram("aBc", "Cba"))            # False

    print("\n🔡 With Spaces or Symbols")
    print(is_anagram("conversation", "voices rant on"))  # False
    print(is_anagram("dormitory", "dirty room"))         # False
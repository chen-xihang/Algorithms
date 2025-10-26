def process_backspace(str):
    stack = []
    for s in str:
        if s == "#":
            if stack:
                stack.pop()
        else:
            stack.append(s)
    return ''.join(stack)

process_backspace('syz##')
process_backspace("#3")
    
def same_string_backspace(a, b):
    ans = process_backspace(a) == process_backspace(b)
    return(ans)


# test cases
if __name__ == "__main__":
    tests = [
        # examples from prompt
        (("abc#abc#", "ababb#"), True, "both reduce to 'abab'"),

        # basic positive / negative checks
        (("ab#c", "ad#c"), True, "both -> 'ac'"),
        (("ab##", "c#d#"), True, "both -> '' (empty)"),
        (("a##c", "#a#c"), True, "both -> 'c'"),

        # different results
        (("a#c", "b"), False, "'c' vs 'b'"),
        (("abc#", "abc"), False, "one ends with backspace removing 'c'"),

        # leading and excessive backspaces
        (("###abc", "abc"), True, "leading backspaces do nothing extra"),
        (("a##", ""), True, "backspacing beyond start yields empty"),
        (("######", ""), True, "only backspaces -> empty"),

        # consecutive backspaces in middle
        (("ab###c", "c"), True, "ab###c -> c"),
        (("ab##c", "c"), True, "ab##c -> c (same)"),
        (("xy#z", "xzz#"), True, "xy#z -> xz ; xzz# -> xz"),

        # long strings with no backspaces
        (("hello", "hello"), True, "identical long strings"),
        (("hello", "hell0"), False, "different characters"),

        # cases with interleaved backspaces
        (("bxj##tw", "bxj###tw"), False, "first -> 'btw', second -> 'tw'"),

        # unicode / special chars (should work the same)
        (("a#🙂b", "🙂b"), True, "unicode char treated like any char"),

        # empty strings
        (("", ""), True, "both empty"),
        (("", "#"), True, "empty and single backspace -> both empty"),
        (("#", ""), True, "single backspace and empty -> both empty"),
    ]

    for (a, b), expected, note in tests:
        result = same_string_backspace(a, b)
        ok = "OK" if result == expected else "BAD"
        print("a={!r}, b={!r} -> {} (expected {}) [{}] -- {}".format(a, b, result, expected, ok, note))
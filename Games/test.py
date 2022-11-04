import string


def isPalindrome(s: str) -> bool:
    abc = string.ascii_uppercase
    for i in range(len(s)):
        s[i] = s[i].upper()
    l = list(s)
    l = list(filter(lambda z: z in abc, s))
    return l == l[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

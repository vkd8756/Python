a="ami"
def vowel(s,n,al=[]):
    vowels=["a","e","i","o","u"]
    if n==1:
        if s[n-1] in vowels:
            al.append(s[n-1])
    else:
        vowel(s,n-1)
        if s[n-1] in vowels:
            al.append(s[n-1])
    print(al,len(a)-len(al))
    return True if len(al)>len(a)-len(al) else False
print(vowel(a,len(a)))


print("\n======\nAnother method")
def is_vowel(ch):
    return ch in ["a","e","i","o","u"]
def vowel_2(s,n):
    if n==1:
        return is_vowel(s[n-1])
    else:
        return vowel_2(s,n-1)+is_vowel(s[n-1])
print(vowel_2("amit",len("amit")))

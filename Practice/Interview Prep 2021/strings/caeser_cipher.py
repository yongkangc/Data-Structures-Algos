def caesarCipher(s, k):
    if not s: return ''
    if k == 0: return s
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_s = ''
    for i in s:
        if i.isalpha():
            if i.isupper():
                new_s += alphabet[(alphabet.find(i.lower()) + k) % 26].upper()
            else:
                new_s += alphabet[(alphabet.find(i) + k) % 26]
        else:
            new_s += i
    return new_s

assert caesarCipher('middle-Outz', 2) == 'okffng-Qwvb'
# print(caesarCipher('middle-Outz', 2))

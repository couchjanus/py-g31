s = 'foobar'
print(s[0])
print(s[2:]) # 'obar'
print(s[2:len(s)]) # 'obar'
print(s[:4] + s[4:]) # 'foobar'
print(s[:4] + s[4:] == s) # True

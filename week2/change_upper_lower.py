str = input()
new_str = ""
for chr in str:
    if chr.isupper() is True:
        new_str += chr.lower()
    else:
        new_str += chr.upper()
print(new_str)

s=input("enter string: ")
freq={}
for ch in s:
    if ch not in freq:
        freq[ch]=1
    else:
        freq[ch]=freq[ch]+1
print(freq)
max_count=0
max_char=""
for ch in freq:
    if freq[ch]>max_count:
        max_count=freq[ch]
        max_char=ch
print(max_char,max_count)

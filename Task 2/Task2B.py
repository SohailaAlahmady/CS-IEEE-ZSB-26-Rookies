word = input()
if(word.isupper() or word[1:].isupper() or len(word) == 1):
    result = ""
    for ch in word:
        if ch.isupper():
            result += ch.lower()
        else:
            result += ch.upper()
    print(result)
else:
    print(word)
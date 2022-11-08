def char_frequency(txt):
    return sorted([(char,txt.count(char)) for char in set(txt)],reverse=True,key=lambda i: i[1])

def read_textfile(filename):
    f = open(filename, "r", encoding="utf8")
    return f.read()

def write_textfile(filename,text):
    f = open(filename, "w", encoding="utf8")
    f.write(text)
    f.close()
    return True

print(read_textfile("list.py"))
pokus = "askjqe  qkerjlůwn flůekwjf"
write_textfile("frekvence.txt", str(char_frequency(read_textfile("dictionary.py"))))
print(char_frequency(read_textfile("list.py")))
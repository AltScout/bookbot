def wordcount(filewords):
    numofwords = 0
    word = filewords.split()
    numofwords = len(word)
    return numofwords

def charactercount(bookwords):
    booklower = bookwords.lower()
    charnums = {}
    for chars in booklower:
        if chars.isalpha():
            if chars in charnums:
                charnums[chars] += 1
            else:
                charnums[chars] = 1
        else:
            pass
    return charnums

def sorting(charlist):
    count = 0
    sortlist = []
    for chars in charlist:
        sortdict = {}
        sortdict["char"] = chars
        sortdict["num"] = charlist[chars]
        sortlist.append(sortdict)
    return sortlist

def sorterkey(sortlist):
    return sortlist["num"]
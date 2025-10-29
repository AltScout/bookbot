from stats import wordcount, charactercount, sorting, sorterkey
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        filecontent = file.read()
    return filecontent

def main():
    try:
        if len(sys.argv) == 2:
            book_content = get_book_text(sys.argv[1])
            wordnums = wordcount(book_content)
            reporttitle = 'BOOKBOT'
            list1title = 'Word Count'
            list2title = 'Character Count'
            reportend = "END"
            header = reporttitle.center(33,'=')
            list1 = list1title.center(33,'-')
            list2 = list2title.center(33,'-')
            ender = reportend.center(33,'=')
            print(header)
            print(f'Analyzing book found at {sys.argv[1]}')
            print(list1)
            print(f'Found {wordnums} total words')
            charnums = charactercount(book_content)
           #print(charnums)
            charnumsorted = sorting(charnums)
           #print(charnumsorted)
            print(list2)
            charnumsorted.sort(reverse=True, key=sorterkey)
            for indx in charnumsorted:
                charindex = indx["char"]
                countindex = indx["num"]
                print(f'{charindex}: {countindex}')
            print(ender)
    except:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)

main()
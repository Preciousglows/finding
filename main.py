# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word=str(input("Please enter a word:"))
    anagram=str(input("Please enter another word:"))

    sorted_word=sorted(word)
    sorted_anagr=sorted(anagram)

    if(sorted_word==sorted_anagr):  
      print("True")
    else:
        print("False")

find_anagram("elbow","below")


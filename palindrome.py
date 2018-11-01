import re

palindrome = input ("Enter phrase here!:")
palindrome = palindrome.lower()
char_pos = 0

print(palindrome.replace(" ","",))

def palindrome(words):
    if len(words) == 0 or len(words) == -1:
        print ("is a palindrome")
        return True
    elif words [0] == words [-1]:
        return palandrome(words[1:-1])
    else:
        print("is not a palindrome.")
        return False












  # while len(palindrome)/2:
#     palindrome[1:-1]
#     palindrome[0] == palindrome[-1]
#     char_pos = char_pos + 1

#   ~~~~~~~~~~~~~~~

#   idx = 0
#   eninx = -1

#   while True
#     if new_text[idx] == new_text [eninx]:
#         idx = idx+1
#         eninx -=1
  
  
  
    # while len(palindrome)/2:
    # palindrome[1:-1]

    # palindrome[0] == palindrome[-1]

    # char_pos = char_pos + 1
    # char_pos += 1
    # if palindrome[0] == palindrome[-1]:
    #     return True
    # if palindrome[0] != palindrome[-1]:
    #     return False
        








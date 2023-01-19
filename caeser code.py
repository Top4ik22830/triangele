letters = "abcdefghijklmnopqrstuvwxyz 123456789',."
que = input("Do you want to encrypt or decrypt? Yes = encrypt) No = Decrypt").lower()
if que == "yes": 
   word = str(input("what word do you want")).lower()
   key = int(input("Enter the shift key"))
   new_word = ""
          

   for i in range(len(word)):

      new_letter_key = int(letters.index(word[i]) + key)
      new_letter = letters[new_letter_key%len(letters)]
      new_word = new_word + new_letter
   ##   word.index = word.index + 1
   print(new_word)
elif que == "no":
   word = str(input("what word do you want to decrypt")).lower()
   key = int(input("Enter the shift key"))
   new_word = ""
             

   for i in range(len(word)):

      new_letter_key = int(letters.index(word[i]) - key)
      new_letter = letters[new_letter_key%len(letters)]
      new_word = new_word + new_letter
   ##   word.index = word.index + 1
   print(new_word)
else:
   print("write yes or no!!!!!!!!")

   

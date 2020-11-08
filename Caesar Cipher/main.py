import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(chosen_direction,start_text,shift_amount):
    text_to_work_with=""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if  chosen_direction=="decode":
                caesar_position=position-shift_amount
            else:
                caesar_position=position+shift_amount
            if chosen_direction=="encode" and (caesar_position)>len(alphabet):
                caesar_position-=len(alphabet)
            new_letter = alphabet[caesar_position]
            text_to_work_with += new_letter
            
        else:
                text_to_work_with+=letter
       
    print(f"The {chosen_direction} text is {text_to_work_with}")





one_more_time=True
while(one_more_time):
    print (art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while (shift > len(alphabet)):
        print (f"Number is to hight, please choose from 1 to {len(alphabet)} one more time")
        shift = int(input("Type the shift number:\n"))
    caesar(chosen_direction=direction,start_text=text,shift_amount=shift)
    user_choise = input ("Type 'yes' if you want to go againe, Otherwise type 'no'. \n").lower()
    if(user_choise)=="no":
            one_more_time=False
            print("Good bye")







# First Version 
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt (plain_text, shift_amount):
# #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     encrypt_text=""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         encrypt_position= position+shift_amount
#         if(encrypt_position)>len(alphabet):
#             encrypt_position-=len(alphabet)
#         new_letter = alphabet[encrypt_position]
#         encrypt_text += new_letter
    
#     print(f"The encoded text is {encrypt_text}")

# def decrypt(cipher_text, shift_amount): 
#     decrypt_text =""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         decrypt_position= position-shift_amount
#         new_letter = alphabet[decrypt_position]
#         decrypt_text += new_letter
#     print(f"The decoded text is {decrypt_text}")

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# if direction == "encode":
#     encrypt(plain_text=text,shift_amount=shift)
# else:
#     decrypt(cipher_text=text,shift_amount=shift)
### the encrpyt function
def encrypt(text):
  enc_text = ''
  for i in text:
    if i.isupper():
      i = i.lower()
      enc_text += '!' + en_dic[i]
    elif i in en_dic:
      enc_text += en_dic[i]
    else:
      enc_text += ('=' + i)
  enc_text += '0'
  return enc_text

### test_encrypted function; to check if text is 'Mogen' encrypted
def test_encrypted(text):
  if text[-1] != '0':
    print("\nThis text doesn't seem 'Mogen' encrypted. Test may return \"FAILED\". Do you want to continue the decryption process anyway?")
    confirmation = input('Y/N: ').lower()
    if confirmation == 'y':
      pass
    elif confirmation == 'n':
      input('\nDone. Press Enter to exit. ')
      quit()
    else:
      input('\nInvalid input...\nPress Enter to exit. ')
      quit()

### the decrypt function
def decrypt(text):
  upper = False; error = False; exact = False
  text = text[:-1]
  dec_text = ''

  for i in text:
    if upper == True:
      try:
        dec_text += (de_dic[i].upper())
        upper = False
      except:
        dec_text += i
        error = True
        upper = False
    elif exact == True: dec_text += i; exact = False
    elif i == '!': upper = True; continue
    elif i == '=': exact = True; continue
    elif i in de_dic: dec_text += de_dic[i]
    else: error = True; dec_text += i
  return dec_text

### the encryption and decryption dictionaries
en_dic = {
       'a': 'o', 'b': '&', 'c': '^', 'd': '$', 'e': 'a', 'f': '*', 'g': '@',
       'h': 'g', 'i': '|', 'j': ';', 'k': '%', 'l': 'n', 'm': 'x', 'n': 't',
       'o': '2', 'p': 's', 'q': '~', 'r': 'f', 's': 'ß', 't': '+', 'u': 'c',
       'v': 'v', 'w': 'w', 'x': '7', 'y': '8', 'z': '9', ' ': '5', '.': ':'}
de_dic = {
       'o': 'a', '&': 'b', '^': 'c', '$': 'd', 'a': 'e', '*': 'f', '@': 'g',
       'g': 'h', '|': 'i', ';': 'j', '%': 'k', 'n': 'l', 'x': 'm', 't': 'n',
       '2': 'o', 's': 'p', '~': 'q', 'f': 'r', 'ß': 's', '+': 't', 'c': 'u',
       'v': 'v', 'w': 'w', '7': 'x', '8': 'y', '9': 'z', '5': ' ', ':': '.'}

### 1001 test process function
def test_1001(text, process):
  if process == 1:
    orig_text = text
    pro1_text = encrypt(text) # encrypt
    pro2_text = decrypt(pro1_text) # decrypt
  elif process == 0:
    orig_text = text
    pro1_text = decrypt(text) # decrypt
    pro2_text = encrypt(pro1_text) # encrypt
  elif process == 1001:
    orig_text = text
    pro1_text = encrypt(text) # encrypt
    pro2_text = decrypt(pro1_text) # decrypt
    print('\nEncrypted text:', pro1_text)
    print('Decrypted text:', pro2_text)
    print('\nLength of original text:', len(orig_text))
    print('Length of encrypted text:', len(pro1_text))
    print('Length of decrypted text:', len(pro2_text))
  if (orig_text == pro2_text) and (len(orig_text) == len(pro2_text)):
    result = "=======Result: Test PASSED!======="
  else:
    result = "=======Result: Test FAILED!======="

  return result

### conclusion function
def conc(text, result, pro_text):
  file = open('pro_text.txt', 'w').write(pro_text)
  if error == True:
    print("\nFound one or more non-Mogen character(s) while decrypting, therefore decryted text might not be reliable.")

  print('\nLength of original text:', len(text))
  print('Length of processed text:', len(pro_text))
  print(result)
  print('\nA copy of processed text, pro_text.txt, has been saved to same directory of the cipher.')
  input('Done. Press Enter to exit. ')


### the main process
print("Welcome to 'The Mogen Cipher'.")
global error # the only global variable (used to check if errors occur during ciphing process)
error = False
process = None

text = input('Enter a text here: ')

while process != 1 and process != 0 and process != 1001:
  try:
    process = int(input("Press '1' to encrypt or '0' to decrypt: "))
  except:
    print('Invalid function. Try again.')
    continue

if process == 1:
  pro_text = encrypt(text) # encrypt
  result = test_1001(text, process) # 1001 test process
  print('\nEncrypted text:', pro_text)
  conc(text, result, pro_text)
elif process == 0:
  test_encrypted(text) # checks if text is 'Mogen' encrypted
  pro_text = decrypt(text) # decrypt
  result = test_1001(text, process) # 1001 test process
  print('\nDecrypted text:', pro_text)
  conc(text, result, pro_text)
else:
  print('\nYou have invoked a complete encryption and decryption test process...')
  result = test_1001(text, process) # 1001 test process
  print(result)

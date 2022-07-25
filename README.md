# the_mogen_cipher
A python program for a simple substitution cipher.

⁰⁰⁰ The Mogen Cipher. ⁰⁰⁰
Created by Xtretchy on 11th May 2020.
Mainly finished on this day, 18th May 2020 at 09:31.
And further improvements have been added.
Improvements. This reloaded version:
- takes note of character cases,
- preserves non-Mogen characters,
- saves processed text into a .txt file,
- can invoke a dual (encrypt-decrypt) process,
- code has been properly arranged into functions,
- each process now invokes a dual call, to verify output

Unless stated here, any other letter, symbol or character remains its
original self when encrypted.
Currently;  - the cipher uses 30 characters for encyption.
            - can only encrypt 28 characters.

abcdefghijklmnopqrstuvwxyz
o&^$a*@g|;%nxt2s~fß+cvw789

Additional ciphers:
    - space = '5'
    - fullstop = ':'
    - upppercase = '!~'
    - exact character = '=~'

Rules:
    - Every encrypted text must end with '0'.
        e.g to encrypt 'Now.', you would write '!t2w:0'
    - To write capital letters, you would include an exclamation mark,
      '!' before the character.
        e.g to encrypt 'gatE', you would write '@o+!a0'
    - Since some special characters and numbers are used for encryption,
      to write an exact special character or a number,
      the '=' character must be placed before the special character.
        e.g to encrypt 'Why?', you would write 'Wg8=?0'
        e.g to encrypt 'Me2U', you would write '!xa=2!c0'
        e.g to encrypt 'u@gmail.com', you would write 'c=@@xo|n:^2x0'

Other examples:
    'How are you doing?' = '!g2w5ofa582c5$2|t@=?0'
    "I'm fine." = "!|='x5*|ta:0"
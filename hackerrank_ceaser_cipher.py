"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
For example, the given cleartext  and the alphabet is rotated by . The encrypted string is .

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below. It should return the encrypted string.

caesarCipher has the following parameter(s):

s: a string in cleartext
k: an integer, the alphabet rotation factor
Input Format

The first line contains the integer, , the length of the unencrypted string. 
The second line contains the unencrypted string, . 
The third line contains , the number of letters to rotate the alphabet by.

Constraints

 
 
 is a valid ASCII string without any spaces.

Output Format

For each test case, print the encoded string.

Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb
"""
def caesarCipher(s, k):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alph_dict = dict([(let, i) for i, let in enumerate(alphabet)])
    output = ''

    for l in s:
        is_upper = False
        if not l.isalpha():
            output += l
        else:
            if l.isupper():
                is_upper = True
                l = l.lower()
            index = alph_dict[l]
            new_index = (index + k) % 26
            new_letter = alphabet[new_index]
            if is_upper:
                new_letter = new_letter.upper()
                is_upper = False
            output += new_letter
    return output

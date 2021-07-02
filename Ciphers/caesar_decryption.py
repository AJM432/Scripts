import operator
import string

letters = string.ascii_lowercase
DEFAULT_MOST_COMMON = list('etaoinsrhldcumfpgwybvkxjqz')
custom_most_common = list('eiaotnrshdlmwucgfyb.kpv,j\“\”\'\’qzx-?!')

# input
secret_msg = "Uif xpsme hpft bspvoe uif vojwfstf boe jn votvsf pg xifuifs uif qmbdf j bn tuboejoh sjhiu opx jt uif dpssfdu qmbdf up cf"


def decrypt(encrypted_msg):

    # -------------
    # this letter_frequency list is the key, alter it correctly and you will get the right decryption
    letter_frequency = list('etaoinsrhldcumfpgwybvkxjqz')   # You may need to add more words because dictionary index was out of range
    # -------------

    frequency = {}
    for letter in ''.join(encrypted_msg.split()).lower():
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
   
    frequency = dict(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)) # no idea how but it sorts the dictionary in decending order
    print(''.join(frequency.keys()))

    # for x, key in enumerate(frequency.keys()):
    #     frequency[key] = letter_frequency[x]

    # output_str = ''
    # for x in secret_msg.lower():
    #     if x.isalpha():
    #         output_str += frequency[x]
    #     else:
    #         output_str += x
    # print(output_str)

decrypt(secret_msg)

# pick a four or more letter test word and keep changing the key until a word is matched with the dictionary, use binary search
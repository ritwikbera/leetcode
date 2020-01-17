string1 = 'A man, a plan, a canal: Panama'
string2 = 'race a car'

def isPalindrome(string):
    buff = ''
    for i in range(len(string)):
        if string[i].isalnum():
            buff += string[i].lower()

    # print(buff)

    rev_buff = buff[::-1]
    if buff == rev_buff:
        return True
    return False


print(isPalindrome(string1))
print(isPalindrome(string2))
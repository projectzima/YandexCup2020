def palindromes(text):
    a = 0
    palindrome = None

    for i in range(len(text)):
        for j in range(a, i):
            chunk = text[j:i + 1]
            if chunk == chunk[::-1]:
                if not palindrome:
                    palindrome = chunk
                elif palindrome:
                    if len(chunk) < len(palindrome):
                        palindrome = chunk
                    elif len(chunk) == len(palindrome):
                        if chunk < palindrome:
                            palindrome = chunk
            a = j

    if palindrome:
        return palindrome
    else:
        return "-1"


text = input()
print(palindromes(text=text))

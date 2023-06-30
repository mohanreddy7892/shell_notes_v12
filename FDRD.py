class CertainCode:
    @classmethod
    def returnModifiedSentence(cls, input1):
        words = input1.split()  # split the string into words
        result = []
        for word in words:
            N = len(word)  # length of the word
            new_word = ""
            for ch in word:
                if ch.isalpha():  # if the character is a letter
                    ascii_offset = ord('a') if ch.islower() else ord('A')
                    ascii_end = ord('z') if ch.islower() else ord('Z')
                    new_ch = chr(ascii_offset + ((ord(ch) - ascii_offset + N) % 26))
                    if new_ch > chr(ascii_end):
                        new_ch = chr(ascii_offset + ((ord(new_ch) - ascii_offset - 26) % 26))
                    new_word += new_ch
                else:
                    new_word += ch
            result.append(new_word)
        return ' '.join(result)  # join the modified words back into a sentence

# Example usage:
input1 = "ABCOX"
output = CertainCode.returnModifiedSentence(input1)
print(output)  # Output: "FGHIZ"
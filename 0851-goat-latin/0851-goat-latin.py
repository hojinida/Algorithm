class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(" ")
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        answer = []

        for i, word in enumerate(sentence):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word += "ma" + "a" * (i + 1)
            answer.append(word)

        return " ".join(answer)
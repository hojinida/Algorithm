class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(" ")
        answer = []
        for i in range(len(sentence)):
            word = [i for i in sentence[i]]
            if word[0] not in ['a','e','i','o','u',"A","E","I","O","U"]:
                word.append(word[0])
                word = word[1:]
            word.append("m")
            word.append("a")
            for _ in range(i+1):
                word.append("a")
            answer.append("".join(word))

        return " ".join(answer)
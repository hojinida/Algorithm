class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        indexs = []
        arr = []
        
        for i in range(len(s)):
            if s[i].lower() in vowels:
                indexs.append(i)
                arr.append(s[i])
        
        answer = list(s)
        arr = list(reversed(arr))

        for ar,i in enumerate(indexs):
            answer[i] = arr[ar]

        return "".join(answer)
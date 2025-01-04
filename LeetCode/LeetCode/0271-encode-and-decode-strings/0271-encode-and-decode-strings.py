class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        position = []
        curruntPoint = 0
        
        answer = "".join(strs)
        for s in strs:
            curruntPoint += len(s)
            position.append(str(curruntPoint))
        salt = ",".join(position)+":"

        return salt + answer


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        splitArray = s.split(":",1)
        position = splitArray[0].split(',')
        array = splitArray[1]

        result = []
        beforePoint = 0
        
        for i in position:
            i = int(i)
            result.append(array[beforePoint:i])
            beforePoint = i
    
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
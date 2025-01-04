class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        dx = [0,0,-1,1,1,-1,-1,1]
        dy = [1,-1,0,0,1,-1,1,-1]

        xlength = len(img[0])
        ylength = len(img)
      
        answer = [[0 for _ in range(xlength)]for _ in range(ylength)]

        for i in range(ylength):
            for j in range(xlength):
                sumv = img[i][j]
                num = 1
                for k in range(8):
                    lx , ly = j+dx[k] , i+dy[k]
                    if 0 <= lx < xlength and 0<= ly < ylength:
                        sumv+=img[ly][lx]
                        num+=1
                answer[i][j] = sumv//num

        return answer
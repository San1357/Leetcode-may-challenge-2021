'''Problem : Find Dublicate File In System '''

#CODE :

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d={}
        res=[]
        for i in paths:
            dir = i.split(' ')
            r = dir[0]
            for j in range(1, len(dir)):
                cont = dir[j].split('(')[1][:-1]
                file = r + '/' + dir[j].split('(')[0]
                if cont not in d:
                    d[cont] = [file]
                else:
                    d[cont] += [file]
                    
        for i in d.values():
            if len(i) > 1:
                res.append(i)
        return res

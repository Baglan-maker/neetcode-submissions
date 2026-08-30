class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in mydict:
                mydict[key].append(strs[i])
            else:
                mydict[key] = [strs[i]]
        return list(mydict.values())
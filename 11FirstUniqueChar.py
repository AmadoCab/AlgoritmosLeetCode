class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = set()
        non_repeat = []
        for i in range(len(s)):
            if s[i] in letters:
                if s[i] in non_repeat:
                    non_repeat.remove(s[i])
            else:
                letters.add(s[i])
                non_repeat.append(s[i])
        if not non_repeat:
            return -1
        return s.find(non_repeat[0])

# EOF #

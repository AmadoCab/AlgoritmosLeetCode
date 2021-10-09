class Solution:
    def count(self, string):
        kvdict = dict()
        for char in set(string):
            kvdict[char] = string.count(char)
        return kvdict

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        builder = self.count(magazine)
        build = self.count(ransomNote)
        iterador = list(builder.keys()) + list(build.keys())
        for char in iterador:
            if build.get(char, 0) > builder.get(char, 0):
                return False
        return True

# EOF #

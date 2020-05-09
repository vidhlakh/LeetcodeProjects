import unittest
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        label=False
        if ransomNote=='':
            label=True
            return label
        elif ransomNote=='' and magazine == '':
            label=True
            return label
        elif magazine=='':
            label=False
            return label
        for ransom in ransomNote:
            if ransom in magazine:
                magazine = magazine.replace(ransom,'',1)
                label= True
            else:
                label=False
                break
        return label
class Test(unittest.TestCase):
    testcases  = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("", "", True),
        ("a", "", False),
        ("", "a", True),
    ]

    s = Solution()

    def test0(self):
        for testcase in self.testcases:
            ransomNote, magazine, expected = testcase[0], testcase[1], testcase[2]
            actual = self.s.canConstruct(ransomNote, magazine)
            self.assertEqual(actual, expected)

if __name__=="__main__":
    unittest.main()
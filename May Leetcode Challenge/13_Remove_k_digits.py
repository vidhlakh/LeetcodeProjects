import itertools
class Solution:
    #Time exceeded
    def removeKdigits(self, num: str, k: int) -> str:
        lst=list(num)
        if k ==len(num):
            return "0"
        data = [''.join(subset) for subset in itertools.combinations(lst, len(lst)-k)]
        print(data)
        result=min(data)
        return int(result)

    def removeKdigitsMethod2(self, num: str, k: int) -> str:
        stack=[]
        num_to_rem =k
        for cur in num:
            while num_to_rem and stack and stack[-1]>cur:
                stack.pop()
                num_to_rem=num_to_rem-1
            stack.append(cur)
            answer = "".join(stack[0:len(num)-k]).lstrip("0")
        if len(answer):
            return answer
        else:
            return "0"

s=Solution()
#print(s.removeKdigits("123456789",3))
# print(s.removeKdigitsMethod2("123456789",3))
# print(s.removeKdigitsMethod2("987654321",3))
# print(s.removeKdigitsMethod2("10",1))
# print(s.removeKdigitsMethod2("10200",1))
print(s.removeKdigitsMethod2("1234567890",9))
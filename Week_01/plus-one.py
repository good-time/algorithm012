class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 1
        res = []

        for i in range(len(digits)):
            # 出栈
            num = digits.pop() + flag
            if num >= 10:
                flag = 1
                # 入栈
                res.append(num%10)
            else:
                flag = 0
                # 入栈
                res.append(num)
                
        if flag == 1:
            res.append(flag)

        # list 反转
        res.reverse()
        return res

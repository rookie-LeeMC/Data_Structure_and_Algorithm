class Solution:
    def isValid(self, s: str) -> bool:
        #如果字符串是奇数一定不满足条件
        if len(s) % 2 != 0:
            return False
        #定义一个括号字典
        bracket_dict = {")":"(","]":"[","}":"{"}
        #定义一个栈
        stack = []
        for c in s:
            #当匹配到括号的结束符时
            if c in bracket_dict:
                #栈不能为空,并且栈顶要与结束的括号匹配
                if len(stack) > 0 and bracket_dict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
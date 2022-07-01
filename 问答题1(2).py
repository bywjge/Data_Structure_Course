class SqStack:
    def __init__(self):  # 构造方法
        self.data = []  # 存放栈中元素，初始为空

    # 栈的基本运算算法
    def empty(self):  # 判断栈是否为空
        if len(self.data) == 0:
            return True
        return False

    def push(self, e):  # 元素e进栈
        self.data.append(e)

    def pop(self):  # 元素出栈
        assert not self.empty()  # 检测栈为空
        return self.data.pop()

    def gettop(self):  # 取栈顶元素
        assert not self.empty()  # 检测栈为空
        return self.data[-1]


class ExpressClass:  # 求表达式值类
    def __init__(self, str):  # 构造方法
        self.exp = str  # 存放中缀表达式
        self.postexp = []

    def Trans(self):  # 将exp转换为postexp
        opor = SqStack()  # 定义运算符栈
        i = 0  # i作为exp的索引
        while i < len(self.exp):  # 遍历exp
            ch = self.exp[i]  # 提取str[i]字符ch
            if ch == "(":  # 判定为左括号,将左括号进栈
                opor.push(ch)
            elif ch == ")":  # 判定为右括号
                while not opor.empty() and opor.gettop() != "(":
                    e = opor.pop()  # 将栈中最近"("之前的运算符退栈
                    self.postexp.append(e)  # 退栈运算符添加到postexp
                opor.pop()  # 再将(退栈
            elif ch == "+" or ch == "-":  # 判定为加或减号
                while not opor.empty() and opor.gettop() != "(":
                    e = opor.pop()  # 将栈中不低于ch的所有运算符退栈
                    self.postexp.append(e)  # 退栈运算符添加到postexp
                opor.push(ch)  # 再将"+"或"-"进栈
            elif ch == "*" or ch == "/":  # 判定为"*"或"/"号
                while not opor.empty():
                    e = opor.gettop()
                    if e != "(" and (e == "*" or e == "/"):
                        e = opor.pop()  # 将栈中不低于ch优先级的所有运算符退栈
                        self.postexp.append(e)  # 退栈运算符添加到postexp
                    else:
                        break
                opor.push(ch)  # 再将"*"或"/"进栈
            else:  # 处理数字字符
                d = ""
                while "0" <= ch <= "9":  # 判定为数字
                    d += ch  # 提取所有连续的数字字符
                    i += 1
                    if i < len(self.exp):
                        ch = self.exp[i]
                    else:
                        break
                i -= 1  # 退一个字符
                self.postexp.append(int(d))  # 连续数字符转换为整数运算数
            i += 1
        while not opor.empty():  # 此时exp扫描完毕,栈不空时循环
            e = opor.pop()  # 将栈中所有运算符退栈并添加到postexp
            self.postexp.append(e)


if __name__ == "__main__":
    str = "1+6/(8-5)*3"
    obj = ExpressClass(str)
    obj.Trans()
    print("后缀表达式：", obj.postexp)

#定义一个空学生类
class Student():
    #此处pass，代表直接空过，不能缺psaa
    pass
class PythonStudent():
    name = None
    age = 18
    course = "python"
    #系统默认self参数
    #def doHomework的缩进层级
    def doHomework(self):
        print("i zuozuoye")
        #推荐函数末尾使用return语句
        return  None
kkk = PythonStudent()
#成员函数的调用没有传递进入参数
kkk.age
kkk.name
print(kkk.name)
print(kkk.age)
kkk.doHomework()
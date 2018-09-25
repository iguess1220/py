class Item:
    def __init__(self,type,area):
        self.type = type
        self.area = area
    def __str__(self):
        return  "家具类型: %s 家具面积: %d" % (self.type,self.area)

class Home:
    def __init__(self,address,area):
        self.address = address
        self.area = area
        self.free_area = area
    def add_Item(self,item):
        if self.free_area >= item.area:
            print("家具%s添加成功" % item.type)
            self.free_area -= item.area
        else:
            print("家具%s添加失败" % item.type)
    def __str__(self):
            return "房子地址：%s 房子总面积：%d 房子生于面积：%d " % (
                self.address,self.area,self.free_area)
shafa = Item("沙发",10)
fangzi = Home("昌平区沙河高教园恒大城5号院1单元901室",91)
fangzi.add_Item(shafa)
print(fangzi)
bed = Item("床",82)
fangzi.add_Item(bed)
print(fangzi)
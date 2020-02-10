class washer(object):
    """洗衣机图纸"""
    def __init__(self,modleName,width,height):
        """初始化
        modleName:型号名称"""
        self.modleName = modleName
        self.width = width
        self.height = height

    def print_info(self):
        print(f"洗衣机的型号是{self.modleName},高度是{self.height},宽度是{self.width}")
        # print(f"洗衣机的高度是{self.height}")
    
    def __del__(self):
        print("自动删除")
        
    def __str__(self):
        return "海尔洗衣机的说明书"
    
haier = washer('海尔',500,800)

haier.print_info()

print(haier)
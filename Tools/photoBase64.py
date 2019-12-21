#引用文件选择对话框
from tkinter.filedialog import askopenfilename,asksaveasfilename

## 图片转换包
import base64

def main():

    while True:
        menu()
        s = input()
        if  s == '1':
            picToByte()
        elif s == '2':
            byteToPic()
        elif expression:
            pass

def menu():
    print("请输入操作选项")
    print("1,图片生成二进制码")
    print("2,二进制码生成图片")

def picToByte():
    ## 选择图片地址
    picFilePath = askopenfilename()
    # 用二进制方式打开图片文件
    picFile =  open(picFilePath,'rb')
    # 读取文件内容,转换为base64编码
    bs = base64.b64encode(picFile.read())

    picFile.close()

    print("=" * 20)
    print(bs)
    print("=" * 20)

def byteToPic():
    bs = input('请输入base64字符串:')

    picdata = base64.b64decode(bs)

    picFilePath = asksaveasfilename()

    picFile = open(picFilePath,'wb')
    picFile.write(picdata)
    picFile.close()

    
main()
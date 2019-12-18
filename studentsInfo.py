

info_list = [] ##学生信息列表

#菜单
def print_menu():
    print("=" * 10)
    print("1.增加")
    print("2.删除")
    print("3.修改")
    print("4.查询")
    print("5.显示")
    print("6.退出")
    print("=" * 10)

#1添加学生信息
def add_new_info():
    #global info_list
    new_name = input("请输入姓名:")
    new_tel = input("请输入手机号码:")
    new_qq = input("请输入QQ:")
    for temp_info in info_list:
        if temp_info["name"] == new_name:
            print("此用户名已经被占用,请重新输入:")
            return

    info = {} #空字典
    info["name"] = new_name
    info["tel"] = new_tel
    info["qq"] = new_qq
    info_list.append(info)#将字典加入到列表中

#2删除学生信息
def del_info():
    #global info_list
    del_num = int(input("请输入要删除的序号:"))
    if 0 <= del_num <len(info_list):
        del_flag = input("你确定要删除吗?(yes or no)")
        if del_flag == "yes":
            del info_list[del_num]
    else:
        print("输入序号有误,请重新输入:")
#3修改
def modify_info():
    #global info_list
    modify_num = int(input("请输入要改的序号:"))
    if 0<= modify_num <len(info_list):
        info = info_list[modify_num]
        print("要修改的信息是:")
        print("name:%s,tel%s,qq%s" % (info["name"],info["tel"],info["qq"]))
        info["name"] = input("请输入新的名称:")
        info["tel"] = input("请输入新的电话:")
        info["qq"] = input("请输入新的qq:")

    else:
        print("输入序号有误,请重新输入")

#4查找信息
def search_info():
    search_name = input("输入查询姓名:")
    for temp_info in info_list:
        if temp_info["name"] == search_name:
            print("查询到的信息如下:")
            print("name:%s,tel:%s,qq:%s" % (temp_info["name"],temp_info["tel"],temp_info["qq"]))
            break
        else:
            print("没有你的信息")
#5显示
def print_all_info():
    print("序列\t 姓名 \t\t 手机号 \t\t qq")
    i= 0
    for temp in info_list:
        print("%d\t %s \t\t %s \t\t %s" % (i,temp["name"],temp["tel"],temp["qq"]))
        i += 1

def main():
    while True:
        print_menu()
        num = input("请输入要操作的数字:")
        if num == "1":
            add_new_info()
        elif num == "2":
            del_info()
        elif num == "4":
            search_info()
        elif num == "3":
            modify_info()
        elif num == "5":
            print_all_info()
        elif  num == "6":
            exit_flag = input("你确定退出吗(yes or no)?")
            if exit_flag == "yes":
                break
        else:
            print("输入有误,请重新输入")

main()
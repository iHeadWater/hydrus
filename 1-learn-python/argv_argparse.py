import sys
import argparse

def cmd():
    args = argparse.ArgumentParser(description = 'Personal Information ',epilog = 'Information end ')
    #必写属性,第一位
    args.add_argument("name",         type = str,                  help = "Your name")
    #必写属性,第二位
    args.add_argument("birth",        type = str,                  help = "birthday")
    #可选属性,默认为None
    args.add_argument("-r",'--race',  type = str, dest = "race",   help = u"民族")
    #可选属性,默认为0,范围必须在0~150
    args.add_argument("-a", "--age",  type = int, dest = "age",    help = "Your age",         default = 0,      choices=range(150))
    #可选属性,默认为male
    args.add_argument('-s',"--sex",   type = str, dest = "sex",    help = 'Your sex',         default = 'male', choices=['male', 'female'])
    #可选属性,默认为None,-p后可接多个参数
    args.add_argument("-p","--parent",type = str, dest = 'parent', help = "Your parent",      default = "None", nargs = '*')
    #可选属性,默认为None,-o后可接多个参数
    args.add_argument("-o","--other", type = str, dest = 'other',  help = "other Information",required = False,nargs = '*')

    args = args.parse_args()#返回一个命名空间,如果想要使用变量,可用args.attr
    print ("argparse.args=",args,type(args))
    print ('name = %s'%args.name)
    d = args.__dict__
    for key,value in d.items():
        print ('%s = %s'%(key,value))

if __name__=="__main__":
    cmd()
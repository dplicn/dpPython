#引用文件选择对话框
from tkinter.filedialog import askopenfilename,asksaveasfilename,askopenfilename

def main():
    print("this program creates a file of username from a")
    print("file of names")
    #get the file names
    infileName = askopenfilename()
    outfileName = asksaveasfilename()

    #open the files
    infile = open(infileName,'r')
    outfile = open(outfileName,'w')
    #
    for line in infile:
        first,last = line.split()
        userName = first[0].upper() + last[0:7].lower()
        print(userName,file = outfile)

    #close file
    infile.close()
    outfile.close()

main()

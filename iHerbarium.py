# -*- coding: utf-8 -*-
# Based on python 3

import os
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename
import _locale
import Kingdonia
from ipybd import KingdoniaPlant, Occurrence, CVH, Label

_locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

#os.system("") #解决windows 10 cmd 命名行无法显示彩色文本的问题，神经质的一个方式竟然可行！


def main():
    print("iHerbarium 由中国科学院生物标本馆(博物馆)工作委员会资助\n")

    start = "y"
    while start == "y":
        opr = input(
            "\n请输入对应的数字，回车后选定所要进行的操作：\n\n\
        【1】图片条码识别并命名\t\t【2】按文件名提取图片\t\t【3】标本标签打印\n\n\
        【4】Excel 数据表转 Kingdonia 输入格式\t\t【5】Excel 数据表转 CVH 格式\n\n\
        【6】Excel 数据表转 DarwinCore 格式\t\t【7】Excel 数据表转标签打印格式\n\n")
        if opr == "1":
            print("\n请选择图片所在的文件夹，可以包括多层子文件夹，程序会自动忽略非图片文件\n")
            dir = askdir()
            if dir == "":
                continue
            Kingdonia.rename(dir)
        elif opr == "2":
            print("\n请选择包含文件名列表的 Excel 文件\n\n")
            excel = askfile()
            if excel == "":
                continue
            print(excel)
            print("\n请选择进行匹配的图片文件夹路径：\n\n")
            dir = askdir()
            while dir == "":
                dir = askdir()
            print(dir)
            print("\n请选择被提取图片的存储路径：\n\n")
            dst = askdir()
            print(dst)
            Kingdonia.extract_file(excel, dir, dst)
        elif opr == "3":
            print("\n请选择需要打印的 excel 文件\n\n")
            excel = askfile()
            if excel == "":
                continue
            print(excel)
            repeat = int(input("\n请输入每条记录要打印的标签份数，若输入 0 程序会自动按照表格中表示标本份数的字段数值进行打印：\n\n"))
            style = int(input("\n请输入要打印的标签样式：\n\n\
        【1】种子植物标签（带条形码）\t\t【2】隐花植物标签（带条形码）\n\n\
        【3】中文植物通用标签（无条形码）\t\t【4】英文植物通用标签（无条形码）\n\n"))
            if style == 1:
                style = 'flora_code'
            elif style == 2:
                style = 'cryptoflora_code'
            elif style == 3:
                style = 'plant'
            elif style == 4:
                style = 'plant_en'
            else:
                style = 'plant'
            columns = int(input("\n请输入每页内标签的列数，比如 2 或 1：\n\n"))
            raws = int(input("\n请输入每页内标签的行数，比如 3 或 4：\n\n"))
            height = int(input("\n请输入纸张高度（单位为 mm，比如是 A4 纸张纵向打印，请输入 297，横向打印请输入 210，其他纸型请自行查阅纸质尺寸）：\n\n"))
            if style == 'plant' or style == 'plant_en':
                barcode = None
            elif input("\n是否要自动编排条形码编号（y/n）：\n\n") == "y":
                barcode = input("\n请输入起始条形码，程序会根据打印数量自动编排条形码:\n\n")
            else:
                barcode = None
            printer = Label(excel, repeat=repeat)
            printer.write_html(columns=columns, rows=raws, start_code=barcode, page_height=height, template=style)
            print("\n已在文件原路径同名文件夹下生成 Labels.html 文件，请用浏览器打开，按 Ctrl+P 打印，打印时可设置边距为'无'，以保证排版正确\n\n")
        elif opr == "4":
            print("\n请选择需要核查的 excel 文件\n\n")
            excel = askfile()
            if excel == "":
                continue
            print(excel)
            table = KingdoniaPlant(excel)
            dir = os.path.splitext(excel)[0] + '_kingdonia.xlsx'
            table.save_data(dir)
        elif opr == "5":
            print("\n请选择需要核查的 excel 文件\n\n")
            excel = askfile()
            if excel == "":
                continue
            print(excel)
            occ = CVH(excel)
            dir = os.path.splitext(excel)[0] + '_CVH.xlsx'
            occ.save_data(dir)
        elif opr == "6":
            print("\n请选择需要核查的 excel 文件\n\n")
            excel = askfile()
            if excel == "":
                continue
            print(excel)
            occ = Occurrence(excel)
            dir = os.path.splitext(excel)[0] + '_occurrence.xlsx'
            occ.save_data(dir)
        elif opr == "7":
            print("\n请选择需要核查的 excel 文件\n\n")
            excel = askfile()
            if excel == "":
                continue
            print(excel)
            occ = Label(excel)
            dir = os.path.splitext(excel)[0] + '_label.xlsx'
            occ.save_data(dir)
        else:
            input("\n您的输入内容不匹配...\n\n")
        start = input("\n\n执行已完成，请问是否继续其他操作（y/n）\n\n")


def askdir():
    root = Tk()
    root.withdraw()
    return askdirectory()


def askfile():
    root = Tk()
    root.withdraw()
    return askopenfilename()


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
# Based on python 3

from os import popen as os_popen
from os import rename as os_rename
from os import walk as os_walk
from os.path import dirname as os_path_dirname
from os.path import join as os_path_join
from os.path import splitext as os_path_splitext
from re import compile as re_compile
from shutil import copy as shutil_copy
from pandas import read_excel
from PIL import Image
from tqdm import tqdm
from pyzxing import BarCodeReader


Image.MAX_IMAGE_PIXELS = 1000000000


class BlockError(Exception):
    pass


def extract_file(excel, dir, dst):
    while True:
        title = input("\n请输入提取图片所依据的列名：\n\n")
        try:
            table = read_excel(excel, converters={title: str})
            barcode = list(table[title])
            break
        except KeyError:
            print("\n输入的列名不在当前 Excel 表格之中，请重新输入\n")
            continue
    rdf = os_walk(dir)
    file_dict = {}
    for root, _, files in rdf:
        for file in files:
            name_ext = os_path_splitext(file)
            if name_ext[1].lower() in (".jpg", ".jpeg", ".tiff", ".tif", ".png", ".pdf"):
                img_path = os_path_join(root, file)
                file_dict[name_ext[0]] = img_path
            else:
                continue
    no_img_barcode = []
    print("\n")
    for b in tqdm(barcode, desc="文件提取", ascii=True):
        try:
            shutil_copy(file_dict[b], dst)
        except KeyError:
            no_img_barcode.append(b)
            continue
        #except OSError:
        #   print(b + "数据重复！\n")
        #   continue

    print("\n以下条形码未找到照片：\n")
    for n in no_img_barcode:
        print(n, end=", ")


def rename(dir):
    """
    dir:图片文件的目录地址，并不强制为图片文件的根目录
    return：返回 None，函数只会识别图片中的条形码，并以该条形码重命名图片文件名
    care：该程序会将同一目录下相应图片文件的 Nikon nef 文件一并重命名，但尚不支持其他raw格式文件，条码识别引擎来自于 zbar
    """
    bar_error = []
    repeat_error = []
    cnt_ident = 0
    cnt_error = 0
    cnt_repeat = 0
    zxing_installed = 1
    pdf = os_walk(dir)

    def ident(raw_img_path):
        nonlocal cnt_ident
        nonlocal cnt_error
        nonlocal cnt_repeat
        nonlocal zxing_installed
        tmp_img = os_path_dirname(__file__) + "/./zbar/tmp.jpg"
        zbarimg = os_path_dirname(__file__) + "/./zbar/bin/zbarimg.exe"
        bar_pattern = re_compile(r":([A-Z0-9]+)\n")
        zxing_reader = BarCodeReader()
        try:
            if " " in raw_img_path:
                raise BlockError
            else:
                img = open(raw_img_path, "rb")
                im = Image.open(img)
                x, y = im.size
                if x > 3000:
                    rm = im.resize((3000, int(3000*y/x)), Image.ANTIALIAS)
                    with open(tmp_img, "w") as pic:
                        rm.save(pic)
                    try:
                        barcode_name = bar_pattern.findall(
                            os_popen("%s %s %s" % (zbarimg, "-q", tmp_img)).read())[0]
                    except IndexError:
                        if zxing_installed:
                            try:
                                barcode_name = zxing_reader.decode(tmp_img)[0]['parsed'].decode('UTF-8')
                            except IndexError:
                                zxing_installed = 0
                                print("\n手动安装 openjdk8 有可能提高你的条码识别率，openjdk 下载地址：\n\
https://www.openlogic.com/openjdk-downloads\n\
请选择和你 Windows 系统相匹配的 msi 文件安装\n\n")
                                raise KeyError
                        else:
                            raise KeyError
                else:
                    try:
                        barcode_name = bar_pattern.findall(
                            os_popen("%s %s %s" % (zbarimg, "-q", raw_img_path)).read())[0]
                    except IndexError:
                        if zxing_installed:
                            try:
                                barcode_name = zxing_reader.decode(raw_img_path)[0]['parsed'].decode('UTF-8')
                            except IndexError:
                                zxing_installed = 0
                                print("\n手动安装 openjdk8 有可能提高你的条码识别率，openjdk 下载地址：\n\
https://www.openlogic.com/openjdk-downloads\n\
请选择和你 Windows 系统相匹配的 msi 文件安装\n\n")
                                raise KeyError
                        else:
                            raise KeyError
                img.close()
                new_img_path = os_path_join(path, barcode_name)
                os_rename(raw_img_path, new_img_path + file_format)
                try:
                    raw_img_path = os_path_join(path, os_path_splitext(file)[0]+".nef")
                    os_rename(raw_img_path, new_img_path+".nef")
                except:
                    pass
                cnt_ident += 1
        except KeyError:
            bar_error.append(raw_img_path)
            cnt_error += 1
        except FileExistsError:
            repeat_error.append(raw_img_path)
            cnt_repeat += 1
            #barcode_name = bar_pattern.findall(os_popen("%s %s %s" % (
            #    zbarimg, "-q", raw_img_path)).read())[0] + "_" + str(cnt_repeat) + ".jpg"
            #new_img_path = os_path_join(path, barcode_name)
            #os_rename(raw_img_path, new_img_path)
            cnt_ident += 1

        return cnt_ident, cnt_error, cnt_repeat

    for path, dirs, files in pdf:
        #print(path, dirs, files)
        for file in tqdm(files, desc="图片条形码识别", ascii=True):
            file_format = os_path_splitext(file)[1].lower()
            if file_format in (".jpg", ".jpeg", ".tiff", ".tif", ".png"):
                raw_img_path = os_path_join(path, file)
                try:
                    ident(raw_img_path)
                except BlockError:
                    tmp_img_path = raw_img_path.replace(" ", "")
                    os_rename(raw_img_path, tmp_img_path)
                    ident(tmp_img_path)
            else:
                continue

    print("\n结束识别，正在输出识别报告：")
    rate = cnt_ident / (cnt_ident + cnt_error)
    print("\n成功识别 %d 张，%d 张照片无法识别条形码，%d 张照片的条形码重复,识别率为 %.2f" %
          (cnt_ident, cnt_error, cnt_repeat, rate))
    if cnt_repeat != 0:
        print("\n以下照片条形码号在其文件夹下存在重复，已经对其进行增量命名，请进一步核实：\n")
        for r in repeat_error:
            print(r)
    if cnt_error != 0:
        print("\n以下照片无法识别，请手动命名：\n")
        for err in bar_error:
            print(err)


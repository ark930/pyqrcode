# -*- coding: utf-8 -*-
from pyzbar import pyzbar
import cv2


# from error import BarcodeNotFoundError
# from error import FileNotFoundError


def parse(image_path):
    # 加载图像
    image = cv2.imread(image_path)

    if image is not None:
        # 找到图像中的条形码并进行解码
        barcodes = pyzbar.decode(image)

        if len(barcodes) >= 1:
            # 取出第一个二维码
            first_barcode = barcodes[0]
            barcode_data = first_barcode.data.decode("utf-8")
            barcode_type = first_barcode.type
            return True, barcode_type, barcode_data
        else:
            return False, None, None
    else:
        raise ImageParseError


def capture(image_path):
    from os import system
    system('raspistill -t 500 -n -o ' + image_path)
    # system('raspistill -t 500 -n -o ' + image_path)


class BarcodeNotFoundError(Exception):
    pass


class ImageParseError(Exception):
    pass

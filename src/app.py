# -*- coding:utf-8 -*-
from barcode import scanner
import resource
import os
import argparse
import threading


def play_by_barcode():
    try:
        image_path = '../image/barcode.jpg'
        if os.path.isfile(image_path) and os.access(image_path, os.R_OK):
            os.remove(image_path)

        for i in range(10):
            # 获取二维码图片
            scanner.capture(image_path)

            # 识别二维码图片
            result, barcode_type, barcode_data = scanner.parse(image_path)
            if result is True:
                print("[INFO] Found barcode: type->{}, text->{}".format(barcode_type, barcode_data))
                break
        else:
            raise scanner.BarcodeNotFoundError

        # 查找资源文件
        resource_id, resource_type = resource.search(barcode_data)
        print("[INFO] Found resource: id->{}, type->{}".format(resource_id, resource_type))

        # 播放资源文件
        print("[INFO] Play resource")
        resource.play(resource_id, resource_type)
    except scanner.BarcodeNotFoundError:
        print("[ERROR] Barcode not found")
    except scanner.ImageParseError:
        print("[ERROR] Image parse error")
    except resource.ResourceNotFound:
        print("[ERROR] Resource not found")
    except resource.ResourcePlayError:
        print("[ERROR] Resource play error")
    finally:
        print("[INFO] finish")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', help='command type')
    parser.add_argument('url', help='an integer for the accumulator')
    args = parser.parse_args()
    if args.type is None or args.type == 'cmd':
        # 查找资源文件
        meta_data = resource.search(args.url)
        print(meta_data)
        # resource.fetch(meta_data)
        t1 = threading.Thread(target=resource.fetch, args=[meta_data])
        t1.start()
        print('run thread 1')
        # media = resource['default']
        # for URL in media['URLs']:
        #     print(URL['URL'])
    elif args.type == 'tts':
        import tts
        import os
        file_path = tts.sentence_to_audio('我们一起学猫叫，一起往汪汪往汪喵嗷呜')
        resource.play(file_path)
    else:
        play_by_barcode()

from barcode import scanner
import resource
import os

try:
    image_path = '../image/barcode.jpg'
    if os.path.isfile(image_path) and os.access(image_path, os.R_OK):
        os.remove(image_path)

    for i in range(5):
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

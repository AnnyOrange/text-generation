from PIL import Image
import os

def center_crop_images(base_folder, target_size=(65, 84)):
    # 获取base_folder中的所有文件名
    base_files = os.listdir(base_folder)

    for base_file in base_files:
        # 构建完整的文件路径
        base_path = os.path.join(base_folder, base_file)

        # 打开图像
        base_image = Image.open(base_path)

        # 获取图像的尺寸
        image_size = base_image.size

        # 计算裁剪框的左上角坐标
        left = (image_size[0] - target_size[0]) // 2
        top = (image_size[1] - target_size[1]) // 2

        # 计算裁剪框的右下角坐标
        right = left + target_size[0]
        bottom = top + target_size[1]

        # 居中裁剪
        base_image_cropped = base_image.crop((left, top, right, bottom))

        # 保存裁剪后的图像
        base_image_cropped.save(base_path)

if __name__ == "__main__":
    # 指定文件夹路径
    base_folder = "D:\\AI\\text-re\\text-generation\\data_preparation\\cropped_images"

    # 执行居中裁剪
    center_crop_images(base_folder)

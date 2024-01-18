import os
from shutil import copyfile

def organize_images(folder1, folder2, output_parent_folder):
    # 获取两个文件夹中的所有文件名
    files_folder1 = os.listdir(folder1)
    files_folder2 = os.listdir(folder2)

    # 计数器，从1开始
    counter = 1

    # 遍历两个文件夹中的文件
    for file1 in files_folder1:
        for file2 in files_folder2:
            # 如果两个文件名相同
            if file1 == file2:
                # 构建完整的文件路径
                path_folder1 = os.path.join(folder1, file1)
                path_folder2 = os.path.join(folder2, file2)

                # 创建子文件夹的路径，以计数器命名
                output_folder = os.path.join(output_parent_folder, str(counter))

                # 确保子文件夹存在
                os.makedirs(output_folder, exist_ok=True)

                # 复制文件到子文件夹
                copyfile(path_folder1, os.path.join(output_folder, "style_image.jpg"))
                copyfile(path_folder2, os.path.join(output_folder, "init_image.jpg"))

                # 计数器加1
                counter += 1

if __name__ == "__main__":
    # 指定文件夹路径
    folder1 = "D:\\AI\\text-re\\text-generation\\data_preparation\\cropped_images_xing"
    folder2 = "D:\\AI\\text-re\\text-generation\\data_preparation\\cropped_images"

    # 输出父文件夹路径
    output_parent_folder = "D:\\AI\\text-re\\text-generation\\data_preparation\\organized_images"

    # 执行整理
    organize_images(folder1, folder2, output_parent_folder)

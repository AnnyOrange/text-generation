from PIL import Image

# 输入图像路径和输出目录
input_image_path = r'D:\AI\text-re\text-generation\data_preparation\data\63.png'
output_directory = r'D:\AI\text-re\text-generation\data_preparation\cropped_images_xing'

# 打开图像
image = Image.open(input_image_path)

# 获取图像宽度和高度
width, height = image.size

# 定义每个字的宽度和高度s
num_rows = 3
num_cols = 11

char_width = width // num_cols
char_height = height // num_rows

# 遍历裁剪
for row in range(num_rows):
    for col in range(num_cols):
        left = col * char_width
        upper = row * char_height
        right = (col + 1) * char_width
        lower = (row + 1) * char_height

        # 裁剪并保存每个字
        char_image = image.crop((left, upper, right, lower))
        char_image.save(f'{output_directory}/char4_{row}_{col}.png')

print('裁剪完成！')

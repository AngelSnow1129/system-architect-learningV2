import re
import os
import shutil

markdown_files = [
    "01_计算机硬件.md",
    "02_操作系统知识.md",
    "03_数据库系统.md",
    "04_嵌入式技术.md",
    "05_计算机网络.md",
    "06_其他计算机系统基础知识.md",
    "07_系统配置与性能评价.md",
    "08_信息系统基础知识.md",
    "09_系统安全.md",
    "10_软件工程.md",
    "11_面向对象技术.md",
    "12_项目管理.md",
    "13_系统架构设计.md",
    "14_软件可靠性基础.md",
    "15_软件架构的演化和维护.md",
    "16_未来信息综合技术.md",
    "17_补充-数学与经济管理.md",
    "18_补充-知识产权与标准化.md",
]

image_pattern = re.compile(r'!\[.*?\]\((.*?)(?:\s+".*?")?\)')

for md_file in markdown_files:
    print(f"Processing file: {md_file}")
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        updated_content = content
        found_images = image_pattern.findall(content)
        
        if found_images:
            base_name = os.path.splitext(md_file)[0]
            target_image_dir = os.path.join("images", base_name)

            # 确保目标目录存在
            os.makedirs(target_image_dir, exist_ok=True)
            print(f"  Ensured target directory exists: {target_image_dir}")

            # 初始化图片序号
            image_index = 1
            for original_image_path in found_images:
                # 如果原始图片路径是外部链接，则下载图片
                if original_image_path.startswith("http"):
                    import urllib.request
                    try:
                        print(f"    Downloading image from: {original_image_path}")
                        # 从 URL 中提取文件名
                        original_filename = os.path.basename(original_image_path)
                        # 构造新文件名
                        new_filename = f"{base_name}-{image_index}.png"
                        destination_path = os.path.join(target_image_dir, new_filename)
                        # 下载图片
                        urllib.request.urlretrieve(original_image_path, destination_path)
                        print(f"    Downloaded '{original_image_path}' to '{destination_path}'")
                    except Exception as e:
                        print(f"    Error downloading {original_image_path}: {e}")
                        continue
                # 如果原始图片路径是绝对路径，则复制图片
                elif os.path.isabs(original_image_path):
                    if not os.path.exists(original_image_path):
                        print(f"    Warning: Original image file not found at {original_image_path}. Skipping.")
                        continue
                    original_filename = os.path.basename(original_image_path)
                    # 构造新文件名
                    new_filename = f"{base_name}-{image_index}.png"
                    destination_path = os.path.join(target_image_dir, new_filename)
                    if not os.path.exists(destination_path) or \
                       os.path.getsize(original_image_path) != os.path.getsize(destination_path) or \
                       os.path.getmtime(original_image_path) > os.path.getmtime(destination_path):
                        shutil.copy2(original_image_path, destination_path)
                        print(f"    Copied '{original_image_path}' to '{destination_path}'")
                    else:
                        print(f"    Image '{original_filename}' already exists and is up-to-date in '{target_image_dir}'. Skipping copy.")

                # 对于外部链接，original_filename 和 destination_path 已经在下载时设置
                # 对于绝对路径和相对路径，需要在这里设置
                if not original_image_path.startswith("http"):
                    original_filename = os.path.basename(original_image_path)
                    # 构造新文件名
                    new_filename = f"{base_name}-{image_index}.png"
                    destination_path = os.path.join(target_image_dir, new_filename)
                    
                    # 复制图片
                    if not os.path.exists(destination_path) or \
                       os.path.getsize(original_image_path) != os.path.getsize(destination_path) or \
                       os.path.getmtime(original_image_path) > os.path.getmtime(destination_path):
                        shutil.copy2(original_image_path, destination_path)
                        print(f"    Copied '{original_image_path}' to '{destination_path}'")
                    else:
                        print(f"    Image '{original_filename}' already exists and is up-to-date in '{target_image_dir}'. Skipping copy.")


                # 更新 Markdown 文件中的图片路径为相对路径
                new_image_path = os.path.join("./images", base_name, new_filename).replace("\\", "/")
                
                # 使用 re.sub 进行替换，确保只替换括号内的路径
                # 构造一个更精确的正则表达式来匹配原始路径
                # 查找原始图片路径所在的完整 Markdown 图片语法
                # 需要找到 `![]()` 结构中的 `original_image_path`
                # 这里的替换逻辑需要非常小心，以避免替换错误的文本
                # 我们可以先找到完整的图片语法，然后只替换其中的路径部分
                
                # 找到所有匹配的图片语法
                matches = list(re.finditer(image_pattern, updated_content))
                for match in reversed(matches): # 从后往前替换，避免索引问题
                    full_match = match.group(0)
                    current_path_in_md = match.group(1)
                    if current_path_in_md == original_image_path:
                        # 替换路径部分
                        new_full_match = full_match.replace(original_image_path, new_image_path)
                        updated_content = updated_content[:match.start()] + new_full_match + updated_content[match.end():]
                        print(f"    Updated image path from '{original_image_path}' to '{new_image_path}' in '{md_file}'")
                        break # 假设一个原始路径只对应一个图片语法，如果不是，需要调整逻辑
                
                # 图片序号递增
                image_index += 1
            
            # 将更新后的内容写回 Markdown 文件
            if updated_content != content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"  Successfully updated '{md_file}' with new image paths.")
            else:
                print(f"  No changes needed for '{md_file}'.")

        else:
            print("  No images found.")

    except FileNotFoundError:
        print(f"Error: File {md_file} not found.")
    except Exception as e:
        print(f"An error occurred while processing {md_file}: {e}")

# 收集所有被引用的图片路径
used_images = set()

for md_file in markdown_files:
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        found_images = image_pattern.findall(content)
        base_name = os.path.splitext(md_file)[0]
        target_image_dir = os.path.join("images", base_name)
        
        # 生成预期的图片文件名
        for i, img_path in enumerate(found_images, start=1):
            expected_filename = f"{base_name}-{i}.png"
            used_images.add(os.path.join(target_image_dir, expected_filename))
    except Exception as e:
        print(f"Error reading {md_file}: {e}")

# 遍历 images 目录，删除未使用的图片
images_dir = "images"
removed_count = 0
if os.path.exists(images_dir):
    for root, dirs, files in os.walk(images_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # 使用正斜杠进行比较，确保跨平台兼容
            normalized_path = file_path.replace("\\", "/")
            if normalized_path not in {img.replace("\\", "/") for img in used_images}:
                try:
                    os.remove(file_path)
                    print(f"  Removed unused image: {file_path}")
                    removed_count += 1
                except Exception as e:
                    print(f"  Error removing {file_path}: {e}")

print(f"\n--- Cleaned up {removed_count} unused images ---")
print("--- Image Processing Complete ---")
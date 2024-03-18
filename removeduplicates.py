import os

if __name__ == "__main__":
    txt_files = [f for f in sorted(os.listdir()) if f.endswith('.txt') and f != 'all.txt']
    print(txt_files)

    # 记录每个ID及其首次出现的文件
    id_to_files = {}
    # 保留所有读取的ID顺序
    ordered_ids = []

    # 第一次遍历：读取并记录ID
    for file_name in txt_files:
        print(f"Reading {file_name}")
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                id_ = line.strip()
                # 检查ID长度，如果不足8位则跳过
                if len(id_) < 8:
                    continue
                if id_ not in id_to_files:
                    id_to_files[id_] = [file_name]
                    ordered_ids.append(id_)  # 仅当ID首次出现时才添加到顺序列表中
                else:
                    if file_name not in id_to_files[id_]:
                        id_to_files[id_].append(file_name)

    # 向 'all.txt' 写入所有唯一的ID，保持原始读取顺序
    with open('all.txt', 'w', encoding='utf-8', errors='ignore') as file:
        for id_ in ordered_ids:
            file.write(id_ + '\n')  # 写入ID并添加换行符

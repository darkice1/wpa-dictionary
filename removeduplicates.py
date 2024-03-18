import os

if __name__ == "__main__":
    txt_files = [f for f in os.listdir() if f.endswith('.txt')]

    # 记录每个ID及其出现的文件
    id_to_files = {}

    # 第一次遍历：读取并记录ID
    for file_name in txt_files:
        print(f"Reading {file_name}")
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                id_ = line.strip()
                if id_ not in id_to_files:
                    id_to_files[id_] = [file_name]
                else:
                    if file_name not in id_to_files[id_]:
                        id_to_files[id_].append(file_name)

    # 创建一个字典来记录需要保留的ID和它们应该保留在哪个文件中
    keep_id_in_file = {}
    for id_, files in id_to_files.items():
        keep_id_in_file[id_] = files[0]  # 仅在第一次出现的文件中保留ID

    # 第二次遍历：删除其他文件中的重复ID
    for file_name in txt_files:
        print(f"Writing {file_name}")
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()

        # 用于确保文件内ID的唯一性
        seen_ids = set()
        with open(file_name, 'w', encoding='utf-8', errors='ignore') as file:
            for line in lines:
                id_ = line.strip()
                # 如果这个ID应该在当前文件中保留，且未在当前文件中写入过，则写入
                if keep_id_in_file.get(id_) == file_name and id_ not in seen_ids:
                    file.write(line)  # 确保添加回换行符
                    seen_ids.add(id_)

    # 打印每个ID被保留的文件供审核
    print({id_: file for id_, file in keep_id_in_file.items() if len(id_to_files[id_]) > 1})

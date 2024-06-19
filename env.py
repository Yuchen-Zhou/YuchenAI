import os
import sys
import re

def modify_env_file(project_dir, new_ip):
    env_file_path = os.path.join(project_dir, '.env')

    if not os.path.exists(env_file_path):
        print(f"文件 {env_file_path} 不存在。")
        return

    with open(env_file_path, 'r') as file:
        lines = file.readlines()

    with open(env_file_path, 'w') as file:
        for line in lines:
            # 使用正则表达式匹配以 _HOST= 开头的行并替换IP地址
            modified_line = re.sub(r'(_HOST=)[0-9.]+', r'\g<1>' + new_ip, line)
            file.write(modified_line)

    print(f"{env_file_path} 中所有 _HOST 后的IP地址已修改为 {new_ip}。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python env.py <项目目录>")
        sys.exit(1)

    project_directory = sys.argv[1]

    new_ip = input("请输入新的IP地址: ")
    modify_env_file(project_directory, new_ip)


# Day 7:

import re
import input_load as load
from typing import Tuple


def main(input_filepath: str) -> None:
    # Parse Text File Identifying Supply Crate Stack Drawing & Rearrangement Procedures List
    input_file = load.txt_to_str(input_filepath)

    # print(input_file)
    # print()

    class Dir:
        def __init__(self, path, name):
            self.path = path
            self.name = name
            self.contents = []
            self.size = 0


    dirs = {}
    dir_names = ['/']
    dir_contents = {}

    # Split into command blocks
    delimiter = '$'
    command_groups = [delimiter+l[:-1] for l in input_file.split(delimiter) if l]

    cwd = '/'
    # Establish list of file paths
    for group in command_groups:
        group = group.split('\n')
        # print(group)
        if group[0][2:4] == 'cd':
            # print(cwd)
            split_group = group[0].split(' ')
            if cwd == split_group[-1]:
                pass
            else:
                if cwd == '/':
                    cwd = cwd + split_group[-1]
                    # print('Change Dir command...')
                    # print(cwd)
                    if cwd in dir_names:
                        pass
                    else:
                        dir_names.append(cwd)
                elif split_group[-1] == '..':
                    if len(cwd[:-2]) > 1:
                        cwd = cwd[:-2]
                        if cwd in dir_names:
                            pass
                        else:
                            dir_names.append(cwd)
                        # print('exit Dir command...')
                        # print(cwd)
                    else:
                        cwd = '/'
                        # print('exit Dir command...')
                        # print(cwd)
                else:
                    cwd = cwd+'/'+split_group[-1]
                    # print('Change Dir command...')
                    # print(cwd)
                    if cwd in dir_names:
                        pass
                    else:
                        dir_names.append(cwd)
                    # Dir()
        if group[0][2:4] == 'ls':
            dir_contents[cwd] = group[1:]
            # print('List command...')
        # print()

    print("FilePaths:", dir_names)
    print()


    # Create Directory Objects from path list
    for d in dir_names:
        dirs[d] = Dir(name=d[-1], path=d)
        dirs[d].contents = dir_contents.get(d)

    print()

    ans = 0
    sub_count = -1
    for k in sorted(dirs.keys(), key=len, reverse=True):
        folder_size = 0
        sub_count += 1
        print(k)
        for c in dirs[k].contents:
            file_size = c.split(' ')[0]
            file_name = '/'+c.split(' ')[1]
            if file_size == 'dir':
                # print(file_name, file_size)
                dirs[k[:2]].size += dirs[k].size
                folder_size += dirs[k].size
            else:
                # print(file_name, file_size)
                dirs[k].size += int(file_size)
                folder_size += int(file_size)
                if len(k) > 2:
                    # parent = k[:len(k) // 2]
                    # dirs[parent].size += int(file_size)
                    folder_size += int(file_size)
        # print()
        # print(sub_count)
        print(folder_size)
        if folder_size <= 100000:
            ans += folder_size
        # print('Root Size: ', (ans - dirs.get('/').size - dirs.get(sorted(dir_names, key=len, reverse=True)[0]).size*(sub_count)))

    for k in sorted(dirs.keys(), key=len, reverse=True):
        print(f'{k} file size: {dirs[k].size}')
    print()
    return print(ans)

main('test_input.txt')

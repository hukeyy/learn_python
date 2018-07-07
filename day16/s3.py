# -*- coding: utf-8 -*-
# Author: hkey
import os

def file_handle(backend_data, src=None, type='fetch'):
    if type=='fetch':
        with open('haproxy.cfg', 'r') as file:
            find_list = []
            Flag = False
            for line in file:
                if line.strip() == backend_data:
                    # print(line)
                    Flag = True
                    continue
                if Flag == True and line.startswith('backend'):
                    break
                if Flag:
                    print('\33[42;1m%s\33[0m' % line, end='')
                    find_list.append(line)
        return find_list
    elif type=='change':
        with open('haproxy.cfg', 'r') as read_f, open('haproxy.conf', 'w') as write_f:
            Flag = False
            has_write = False
            for read_line in read_f:  # server
                if read_line.strip() == backend_data:
                    Flag = True
                    continue

                if Flag and read_line.startswith('backend'):
                    Flag = False
                if not Flag:
                    write_f.write(read_line)
                else:
                    if not has_write:
                        for record in src:
                            write_f.write(record)
                        has_write = True
        os.rename('haproxy.cfg', 'haproxy.cnf_bak')
        os.rename('haproxy.conf', 'haproxy.cfg')
        os.remove('haproxy.cnf_bak')

def fetch(data):
    print('\33[43;1m这是查询功能。\33[0m')
    backend_str = 'backend %s' % data
    return file_handle(backend_str, type='fetch')
def add():
    pass

def change(modify_data):
    print('\33[43;1m这是修改功能.\33[0m')
    backend = modify_data[0]['backend'] # 主机名
    backend_data = 'backend %s' % backend # backend 主机名
    #    {'server': '10.0.10.1', 'weight': 20, 'maxconn': 21}
    old_super = '%sserver %s weight %s maxconn %s\n' % ( ' ' *4,  modify_data[0]['record']['server'],
                                            modify_data[0]['record']['weight'],
                                                       modify_data[0]['record']['maxconn'])

    new_super = '%sserver %s weight %s maxconn %s\n' % (' ' * 4, modify_data[1]['record']['server'],
                                                        modify_data[1]['record']['weight'],
                                                        modify_data[1]['record']['maxconn'])
    src_data = fetch(backend)
    if not src_data or old_super not in src_data:
        return '修改的记录不存在。'
    else:
        index = src_data.index(old_super)
        src_data[index] = new_super
        src_data.insert(0, '%s\n' % backend_data)

    return file_handle(backend_data, src=src_data, type='change')

def delete():
    pass



if __name__ == '__main__':
    msg = '''
    1. 查询
    2. 新增
    3. 修改
    4. 删除
    5. 退出
    '''

    msg_dict = {
        '1': fetch,
        '2': add,
        '3': change,
        '4': delete,
    }

    while True:
        print(msg)
        choice = input('>>>').strip()
        if not choice: continue
        if choice == '5': break
        find_str = input('请输入你的数据：').strip()
        if choice != '1':
            find_str = eval(find_str)
        res = msg_dict[choice](find_str)
        print(res)




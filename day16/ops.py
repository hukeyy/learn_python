# -*- coding: utf-8 -*-
# Author: hkey
import os

def file_handle(backend_data, src=None, type='fetch'):
    '''解耦函数'''
    if type == 'fetch':
        with open('haproxy.cfg', 'r') as read_f:
            ret = []
            Flag = False
            for read_line in read_f:
                if backend_data == read_line.strip():
                    Flag = True
                    continue
                if Flag == True and read_line.startswith('backend'):
                    break
                if Flag:
                    print('\33[42;1m%s\33[0m' % read_line, end='')
                    ret.append(read_line)
        return ret

    elif type == 'change':
        with open('haproxy.cfg', 'r') as read_f, open('haproxy.conf', 'w') as write_f:
            flag = False
            has_write = False
            for read_line in read_f:
                if read_line.strip() == backend_data:
                    flag = True
                    continue
                if flag and read_line.startswith('backend'):
                    flag = False
                if not flag:
                    write_f.write(read_line)
                else:
                    if not has_write:
                        for record in src:
                            write_f.write(record)
                        has_write = True
        os.rename('haproxy.cfg', 'haproxy.cfg_bak')
        os.rename('haproxy.conf', 'haproxy.cfg')
        os.remove('haproxy.cfg_bak')


def fetch(find_str):
    '''查询功能'''
    backend_str = 'backend %s' % find_str
    return file_handle(backend_str)

def add(backend):
    '''新增功能'''
    print('这是新增功能.')
    backend_list = fetch(backend)
    if not backend_list:
        return '\33[41;1mbackend不存在。\33[0m'
    new_server = input('输入新增server:')
    backend_data = 'backend %s' % backend
    backend_list.insert(0, '%s\n%s\n' % (backend_data, new_server))
    return file_handle(backend_data, src=backend_list, type='change')


def change(modify_data):
    '''修改功能'''
    print('这是修改功能.')
    modify_data = eval(modify_data)
    backend = modify_data[0]['backend']
    backend_data = 'backend %s' % backend
    backend_list = fetch(backend)
    old_server = '%sserver %s weight %s maxconn %s\n' %(' ' *4, modify_data[0]['record']['server'],
                                           modify_data[0]['record']['weight'], modify_data[0]['record']['maxconn'])
    new_server = '%sserver %s weight %s maxconn %s\n' %(' ' *4, modify_data[1]['record']['server'],
                                           modify_data[1]['record']['weight'], modify_data[1]['record']['maxconn'])

    if not backend_list and old_server not in backend_list:
        return '修改的记录不存在。'
    else:
        index = backend_list.index(old_server)
        backend_list[index] = new_server
        backend_list.insert(0, '%s\n' % backend_data)
        return file_handle(backend_data, src=backend_list, type='change')

def delete(backend):
    '''删除功能'''
    print('这是删除功能.')
    backend_list = fetch(backend)
    if not backend_list:
        return '\33[41;1mbackend 【%s】不存在。\33[0m' % backend
    del_server = input('输入要删除的server:') + '\n'
    if del_server not in backend_list:
        return '\33[41;1m输入的server不存在。\33[0m'
    else:
        backend_data = 'backend %s' % backend
        backend_list.insert(0, '%s\n' %backend_data)
        backend_list.remove(del_server)
        return file_handle(backend_data, src=backend_list, type='change')


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
        res = msg_dict[choice](find_str)
        print(res)





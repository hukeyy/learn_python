# -*- coding: utf-8 -*-
# Author: hkey

def fetch(find_str):
    backend_str = 'backend %s' % find_str
    with open('haproxy.cfg', 'r') as read_f:
        ret = []
        Flag = False
        for read_line in read_f:
            if backend_str == read_line.strip():
                Flag = True
                continue
            if Flag == True and read_line.startswith('backend'):
                break
            if Flag:
                # print('\33[42;1m%s\33[0m' % read_line, end='')
                ret.append(read_line)
    return ret


def add():
    pass

def change(modify_data):
    print('这是修改功能.')
    modify_data = eval(modify_data)
    backend = modify_data[0]['backend']
    backend_list = fetch(backend)
    old_server = '%sserver %s weight %s maxconn %s' %(' ' *4, modify_data[0]['record']['server'],
                                           modify_data[0]['record']['weight'], modify_data[0]['record']['maxconn'])
    new_server = '%sserver %s weight %s maxconn %s' %(' ' *4, modify_data[1]['record']['server'],
                                           modify_data[1]['record']['weight'], modify_data[1]['record']['maxconn'])
    for old_server in backend_list:
        print(old_server)

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
        msg_dict[choice](find_str)




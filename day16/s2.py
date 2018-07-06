# -*- coding: utf-8 -*-
# Author: hkey

def fetch():
    print('\033[43;1m这是查询功能\033[0m')
    select_str = input('请输入要查询的内容：').strip()
    backend_str = 'backend %s' % select_str
    ret = []
    with open('haproxy.cfg', 'r') as file:
        Flag = False
        for line in file:
            if line.strip() == backend_str:
                Flag = True
                continue
            if Flag == True and line.startswith('backend'):
                break
            if Flag:
                print('\33[42;1m%s\33[0m' % line, end='')
                ret.append(line)
    return ret

def add():
    pass

def change():
    pass

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
        '4': delete
    }

    while True:
        print(msg)
        choice = input('>>>').strip()
        if not choice: continue
        if choice == '5': break
        ret = msg_dict[choice]()
        print(ret)



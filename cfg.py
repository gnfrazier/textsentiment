#!/usr/bin/python3

import json


def read_cfg(file='config.json'):
    with open(file, 'r') as f:

        c = json.loads(f.readall())

    return c


def write_log(data, file='log.json'):
    with open(file, 'a') as f:
        f.write(json.dumps(data))
    return True


def main():
    read_cfg()
    write_log('no data')

if __name__ == '__main__':
    main()

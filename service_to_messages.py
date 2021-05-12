import re
import sys


def main():
    filename = sys.argv[1]

    bufs = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            handle_rpc_line(line, bufs)

    if bufs:
        print('\n'.join(bufs))


rpc_line_regex = re.compile(r'rpc (\w+)\((\w+)\) returns \((\w+)\) {}$')


def handle_rpc_line(line, bufs):
    rv = rpc_line_regex.search(line)
    if not rv:
        return
    method, request, response = tuple(rv.groups())
    #print(f'{request=} {response=}')
    bufs.append(f'message {request} {{\n}}\n')
    bufs.append(f'message {response} {{\n}}\n')


if __name__ == '__main__':
    main()

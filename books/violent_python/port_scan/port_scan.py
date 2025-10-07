import argparse

def get_opts():
    parser = argparse.ArgumentParser(description="scan ports")
    parser.usage="%prog --host  <target_host> --port  <target_port>"
    parser.add_argument('-H', '--host', type=str, help='Target host')
    parser.add_argument('-p', '--port', type=int, help='Target port')
    args = parser.parse_args()
    target_host = args.host
    target_port = args.port

    if ((target_host == None) | (target_port == None)):
        print(parser.usage)
        exit()
    else:
        return (target_host, target_port)


if __name__ == '__main__':
    host, port = get_opts()

    print(f"host: {host}, port: {port}")

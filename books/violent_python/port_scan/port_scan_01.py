import optparse

def get_opts():
    parser = optparse.OptionParser('Usage %prog -H  <target_host> -p  <target_port>')
    parser.add_option('-H', dest='tgt_host', type='string', help='Target host')
    parser.add_option('-p', dest='tgt_port', type='int', help='Target port')
    (options, args) = parser.parse_args()
    target_host = options.tgt_host
    target_port = options.tgt_port

    if ((target_host == None) | (target_port == None)):
        print(parser.usage)
        exit()
    else:
        return (target_host, target_port)


if __name__ == '__main__':
    host, port = get_opts()

    print(f"host: {host}, port: {port}")

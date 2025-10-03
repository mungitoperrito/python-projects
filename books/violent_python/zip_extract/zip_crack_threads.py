import zipfile
from threading import Thread


# Only returns password it it is correct. Otherwise returns nothing
def extract_file(zip_file, password):
    try:
        # Python3 needs to encode pwd as byte string
        zip_file.extractall(pwd=password.encode())

        print(f"PWD: {password}")
    except Exception as e:
        # # Uncomment to debug
        # print(f"Exception: {e}")
        pass


def main():
    try:
        zip_file = zipfile.ZipFile('zipped_file.zip', 'r')
    except Exception as e:
        print(f"Can't get zip_file: {e}")
        exit()

    with open('password_file.txt') as password_file:
        for line in password_file.readlines():
            password = line.rstrip('\n')
            t = Thread(target=extract_file(zip_file, password))
            t.start()
            # # Uncomment to confirm multiple threads
            # print(f"t PID: {t.native_id}")

if __name__ == '__main__':
    main()
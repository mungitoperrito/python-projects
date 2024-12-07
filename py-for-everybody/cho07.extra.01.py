# Files

EXISTS = 'mbox.txt'
DOESNT_EXIST = 'not-a-file.txt'

# # No guards
# fh_01 = open(EXISTS)      # Works
# print(fh_01)
# fh_02 = open(DOESNT_EXIST)  # Blows up
# print(fh_02)

# try block
try:
    fh_02 = open(DOESNT_EXIST)
    print(fh_02)
except Exception as e:
    print("File not found")
    print(e)
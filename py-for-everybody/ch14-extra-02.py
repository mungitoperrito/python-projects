# objects - constructors

class Sample:

    def __init__(self):
        self.x = 0
        print("Constructor")

    def inc(self):
        self.x += 1
        print("Method")
    
    def __del__(self):
        print(locals())
        print("Destructor")

print("\ns01")
s01 = Sample()
s01.inc()


print("\ns02")
s02 = Sample()
del s02    # Only one ref to s02

print("\ns03")
s03 = Sample()
s04 = s03
del s03    # Two refs to s03, del decrements obj counter by 1

# auto-delete
print("\nNo code after here")


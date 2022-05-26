#哈希函数
#直接定值法
def my_hash(x):
    return (x%7)

def hash():
    print(my_hash(1))
    print(my_hash(9))
    print(my_hash(25))
    print(my_hash(100))
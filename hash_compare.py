import hashlib

file1 = 'hash_test_files/a.txt'
file2 = 'hash_test_files/b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f"O arquivo {file1} é diferente do arquivo {file2}.")
    print(f"O hash do arquivo {file1} é {hash1.hexdigest()}")
    print(f"O hash do arquivo {file2} é {hash2.hexdigest()}")
else:
    print(f"O arquivo {file1} é igual ao arquivo {file2}.")
    print(f"O hash do arquivo {file1} é {hash1.hexdigest()}")
    print(f"O hash do arquivo {file2} é {hash2.hexdigest()}")


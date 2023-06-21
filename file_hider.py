import os
import stat

file = "./hide.txt"
st = os.stat(file)

os.chflags(file, st.st_flags ^ stat.UF_HIDDEN)
if st.st_flags ^ stat.UF_HIDDEN:
    print(f"O arquivo está oculto")
else:
    print(f"O arquivo não está oculto")


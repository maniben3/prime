import time
import gmpy2
start=time.time()
for x in  range(10**6):
    m=(2**400)+x
    if gmpy2.is_fermat_prp(m,2)==1:
       pass
print(time.time()-start)

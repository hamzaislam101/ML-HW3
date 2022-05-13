from os import stat
import time
import matplotlib.pyplot as plt

plt.figure(1)
plt.show()
plt.savefig('foo.png')

start = time.time()

for i in range(10):
    time.sleep(5)
    continue

end = time.time()
print(str(end-start)+" took time")



import threading
from time import sleep
import time 

start = time.time()

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")

# rewrite everything inside this main function and keep others untouched
def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target = do_job, args=(i,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

main()

end = time.time()
print("Finished in {} second(s)".format(round(end - start,2)))
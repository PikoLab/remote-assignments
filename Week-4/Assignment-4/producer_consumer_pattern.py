import time
import threading
import queue

job_queue = queue.Queue()
for job_index in range(1, 10): # We create 9 jobs with job_index 1 ~ 9
    job_queue.put(job_index)

class Worker(threading.Thread):
    def __init__(self, worker_num):
        threading.Thread.__init__(self)
        self.worker_num = worker_num
    
    def run(self):
        while job_queue.qsize():
            index = job_queue.get()
            self.do_job(index)

    def do_job(self, index):
        # Simulate a job (you can image it as doing something which need to take 1 second)
        print(f"worker {self.worker_num} start job {index}")
        time.sleep(1)
        print(f"worker {self.worker_num} finish job {index}")

workers = []
worker_count = 3 # We have 3 workers
for i in range(worker_count):
    worker = Worker(i+1)
    workers.append(worker)

# Do the job
for worker in workers:
    worker.start()

for worker in workers:
    worker.join()

print("Done.")




# import threading, queue

# q = queue.Queue()

# def worker():
#     while True:
#         item = q.get()
#         print(f'Working on {item}')
#         print(f'Finished {item}')
#         q.task_done()

# # turn-on the worker thread
# threading.Thread(target=worker, daemon=True).start()

# # send thirty task requests to the worker
# for item in range(30):
#     q.put(item)
# print('All task requests sent\n', end='')

# # block until all tasks are done
# q.join()
# print('All work completed')
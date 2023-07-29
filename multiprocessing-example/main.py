# https://developers.redhat.com/articles/2023/07/27/how-use-python-multiprocessing-module#

#!/usr/bin/env python
import os
import multiprocessing

def child_process(id):
    print(f"Hi! I'm a child process {os.getpid()} with id#{id}")

if __name__ == "__main__":
    print(f"Hi! I'm process {os.getpid()}")
    list_of_processes = []

    # Loop through the number 0 to 10 and create processes for each one of
    # them.
    for i in range(0, 10):
        # Here we create a new instance of the Process class and assign our
        # `child_process` function to be executed. Note the difference now that
        # we are using the `args` parameter now, this means that we can pass
        # down parameters to the function being executed as a child process.
        process = multiprocessing.Process(target=child_process, args=(i,))
        list_of_processes.append(process)

    for process in list_of_processes:
        # We then start the process
        process.start()

        # And finally, we join the process. This will make our script to hang
        # and wait until the child process is done.
        process.join()

    print("All done")

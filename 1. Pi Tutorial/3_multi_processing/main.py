from multiprocessing import Process, Queue, Pool
import time
from names import countries

def print_func(country='Australia'):
    print('The name of country is : ', country)

# Multiprocessing Function
def mp_demo(names):
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    start_time = time.time()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()
    end_time = time.time()
    time_run = end_time-start_time
    return time_run

# Single Processing Function
def sing_demo(names):
    start_time = time.time()
    for name in names:
        print_func(name)
    end_time = time.time()
    time_run = end_time-start_time
    return time_run

# Function for task 2 Recursive Square
def square3(number):
    return number^7 + number^6 + number^5 + number^3 + number^2 + number 

def sing_demo2(numbers):
    start_time = time.time()
    all_squares = []
    for number in numbers:
        number_sq = square3(number)
        all_squares.append(number_sq)
    end_time = time.time()
    time_run = end_time - start_time
    return time_run, all_squares


def mp_demo3(numbers):
    start_time = time.time()
    with Pool(processes=4) as pool:
        all_squares = pool.map(square3, numbers)
    end_time = time.time()
    time_run = end_time - start_time
    return time_run, all_squares


if __name__ == "__main__":  # confirms that the code is under main function
    names = countries
    numbers = list(range(300000))
    #time_run_mp = mp_demo(names)
    #time_run_sp = sing_demo(names)
    #print("Total Time for Multiprocessing to run is:" + str(time_run_mp))
    #print("Total Time for Single to run is:" + str(time_run_sp))
    
    time_run_mp3, all_squares2= mp_demo3(numbers)
    time_run_sp2, all_squares_sp= sing_demo2(numbers)
    print(time_run_mp3)
    print(time_run_sp2)
    #print(all_squares)
    #print(all_squares_sp)
    
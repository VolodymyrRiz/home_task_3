import time
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor

def factorize(number):
   
    return [i for i in range(1, number + 1) if number % i == 0]

def factorize_sync(numbers):
    
    return [factorize(number) for number in numbers]

def factorize_parallel(numbers):
    
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        return list(executor.map(factorize, numbers))

numbers = [128, 255, 99999, 10651060]

start_time = time.time()
sync_result = factorize_sync(numbers)
sync_time = time.time() - start_time
print(f"Synchronous factorization took {sync_time:.2f} seconds.")

start_time = time.time()
parallel_result = factorize_parallel(numbers)
parallel_time = time.time() - start_time
print(f"Parallel factorization took {parallel_time:.2f} seconds.")

assert sync_result == parallel_result
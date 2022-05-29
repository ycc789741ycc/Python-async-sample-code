import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor
import time

def func1(obj: str):
    time.sleep(3)
    print(f'Function 1 with {obj}')
    return obj

def func2(obj: str):
    time.sleep(3)
    print(f'Function 2 with {obj}')
    return obj


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    max_workers = 2
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        exec_func1 = functools.partial(func1, obj="hello")
        exec_func2 = functools.partial(func2, obj="dick")
        the_future1 = loop.run_in_executor(executor=executor, func=exec_func1)
        the_future2 = loop.run_in_executor(executor=executor, func=exec_func2)
        done, pending = loop.run_until_complete(asyncio.wait([the_future1, the_future2]))
    
        for each_done in done:
            print(each_done.result())

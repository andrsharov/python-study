import multiprocessing as mp

q = mp.Queue()

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()

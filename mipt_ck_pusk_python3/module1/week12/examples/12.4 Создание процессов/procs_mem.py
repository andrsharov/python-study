import multiprocessing

a = []

def f():
    a.append(1)

def main():
    procs = []
    for i in range(10):
        p = multiprocessing.Process(target=f)
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
    print(a)  # []

if __name__ == '__main__':
    main()

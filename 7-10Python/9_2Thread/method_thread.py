import logging
from time import ctime, sleep
import _thread

logging.basicConfig(level=logging.INFO)
loops = [2, 4]


def loop(nloop, nsec, lock):
    logging.info("start loop" + str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + "at" + ctime())
    lock.release()


def main1():
    logging.info("start all at" + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass
    logging.info("end all at" + ctime())


def loop0():
    logging.info("start loop0 at" + ctime())
    sleep(4)
    logging.info("end loop0 at" + ctime())


def loop1():
    logging.info("start loop1 at" + ctime())
    sleep(2)
    logging.info("end loop1 at" + ctime())


def main():
    logging.info("start all at" + ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(5)
    logging.info("end all at" + ctime())


if __name__ == '__main__':
    # main()
    main1()

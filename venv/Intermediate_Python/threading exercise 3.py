import logging
import threading
import concurrent.futures

l = logging.getLogger()
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


class Bakery:
    def __init__(self):
        self.storage = 0
        self.__lock = threading.lock()

    def baker(self):
        for i in range(10):
            with self.__lock:
                l.info(f"Storage : {self.storage}")
                threading.sleep(0.1)
                self.storage += 1
                threading.sleep(1)

    def customer(self):
        for i in range(10):
            with self.__lock:
                l.info(f"Storage : {self.storage}")
                threading.sleep(0.2)
                if self.storage >= 2:
                    self.storage -= 2
                threading.sleep(1)

if __name__ == "__main__":
    bakery = Bakery()
    with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as executor:
            executor.submit(bakery.baker)
            executor.submit(bakery.customer)
            executor.submit(bakery.customer)
import random

def main(msg):
    i = 0
    while (i := i+1):
        yield 'SYS_write', msg, i
        yield 'SYS_sched',



class OperatingSystem:
    def __init__(self, procs):
        self._procs = procs
        self._current = procs[0]
    def run(self):
        while True:
            syscall, *args = self._current.__next__()
            match syscall:
                case 'SYS_write':
                    print(*args)
                case 'SYS_sched':
                    self._current = random.choice(self._procs)

OperatingSystem([main('ping'), main('pong')]).run()


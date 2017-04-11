# -*- coding: utf-8 -*-
import signal

TTW_SLOW = [0.5, 1.5]
TTW_FAST = [0.0, 0.1]


class SignalManager(object):
    """Manages POSIX signals."""

    kill_now = False
    time_to_wait = TTW_SLOW

    def __init__(self):
        signal.signal(signal.SIGTSTP, self.exit_gracefully)
        signal.signal(signal.SIGUSR1, self.speed_up)
        signal.signal(signal.SIGUSR2, self.slow_down)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True

    def speed_up(self, signum, frame):
        self.time_to_wait = TTW_FAST

    def slow_down(self, signum, frame):
        self.time_to_wait = TTW_SLOW

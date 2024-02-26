import time


class PerfTimer:
  def __init__(self):
    self._start_time = 0
    self._elapsed_time = 0

  def start(self):
    self._start_time = time.perf_counter()

  def stop(self):
    self._elapsed_time = (time.perf_counter() - self._start_time) * 1000
    print(f"{self._elapsed_time:.2f} milliseconds")

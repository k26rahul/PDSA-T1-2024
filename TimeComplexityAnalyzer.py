import time
import matplotlib.pyplot as plt


class TimeComplexityAnalyzer:
  def __init__(self, test_function):
    self.test_function = test_function
    self.input_sizes = []
    self.execution_times = []

  def run(self, input_parameter):
    start_time = time.perf_counter()
    self.test_function(input_parameter)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    self.input_sizes.append(input_parameter)
    self.execution_times.append(execution_time)

  def plot(self):
    plt.plot(self.input_sizes, self.execution_times, marker='o', linestyle='-')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Time Complexity Analysis')
    plt.grid(True)
    plt.show()

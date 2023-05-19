import time

class timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time

    def __repr__(self):
        return f"Execution time: {round(self.elapsed_time*1000, 2)} mili seconds"
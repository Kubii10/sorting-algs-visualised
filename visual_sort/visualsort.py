import random
import sort_algs as sa

class Dataset:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def randomize(size, min_val, max_val):
        """Tworzy Dataset z losowymi wartościami"""
        data = [random.randint(min_val, max_val) for _ in range(size)]
        return Dataset(data)

    def append(self, value):
        return self.data.append(value)
    
    def get_data(self, index=None):
        if index is not None:
            return self.data[index]
        return self.data
    
    def power(self, exponent):
        return [x ** exponent for x in self.data]
    
    def division(self, divisor):
        return [x / divisor for x in self.data]
    
    def multiply(self, factor):
        return [x * factor for x in self.data]  
    
    def add(self, addend):
        return [x + addend for x in self.data]
    
    def subtract(self, subtrahend):
        return [x - subtrahend for x in self.data]

    def visualise(self, delay=0.05, highlight=None, sort='bubble'):
        if sort == 'bubble':
            sa.bubble_sort(
                self.data,
                visual_fn=lambda n, arr, highlight=None: sa.visualise(
                    n, arr, delay=delay, highlight=highlight
                ),
                delay=delay
            )
        elif sort == 'insert':
            sa.insert_sort(
                self.data,
                visual_fn=lambda n, arr, highlight=None: sa.visualise(
                    n, arr, delay=delay, highlight=highlight
                ),
                delay=delay
            )
        elif sort == 'radix':
            sa.radix_sort(
                self.data,
                visual_fn=lambda n, arr, highlight=None: sa.visualise(
                    n, arr, delay=delay, highlight=highlight
                ),
                delay=delay
            )
        else:
            raise ValueError(f"Nieznany typ sortowania: {sort}")
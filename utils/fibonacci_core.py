from dataclasses import dataclass

"""
This is the class that the fibonacci turtle calls to calculate
the fibonacci sequence, thanks to:
https://www.programiz.com/python-programming/examples/fibonacci-sequence
"""


@dataclass
class FibonacciSeq(object):
    current: int = 0
    next: int = 1
    nterms: int = 1000

    def __post_init__(self):
        self.count = 0

    def counter(self):
        """
        Step the sequence by set number.
        """
        while self.count < self.nterms:
            self.step()

    def step(self):
        """
        Step the sequence forward by 1.
        """
        self.nth = self.current + self.next
        self.current = self.next
        self.next = self.nth
        self.count += 1

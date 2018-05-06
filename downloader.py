class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0,1,2,..
    """
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new_value."""
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self

    def print_progression(self,n):
        """Print next n value of the progression"""
        print(' '.join(str(next(self)) for j in range(n)))
        

class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        """Create a new arithematic progression.

        increment the fixed constant to add to each term
        start     the first term of the progression
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first=0, second=1):

        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current
        

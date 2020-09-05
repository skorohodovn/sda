"""
Given function random_exception which raises a random exception every time,
write a try-except block which handles each of the possible exceptions by
counting their occurrences. Print the tally.
"""
import random

possible_exceptions = [OSError, IndexError, ZeroDivisionError]


def random_exception():
    raise random.choice(possible_exceptions)


if __name__ == "__main__":
    OSerrorcount = 0
    IndexErrorcount = 0
    ZeroDivisionErrorcount = 0
    for _ in range(20):
        try:
            random_exception()
        except OSError:
            OSerrorcount = OSerrorcount + 1
        except IndexError:
            IndexErrorcount = IndexErrorcount + 1
        except ZeroDivisionError:
            ZeroDivisionErrorcount = ZeroDivisionErrorcount + 1
    print(f"The tallies are for OSerror: {OSerrorcount}, for IndexError: {IndexErrorcount}, for Zero Division: {ZeroDivisionErrorcount}")
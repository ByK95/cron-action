import sys
import re


class CaptureTheFlag:

    def __init__(self):
        self.captures = set()

    def scan(self, terrain):
        _n_destroy = r"ENG-\d{0,6}"
        capture = re.search(_n_destroy, terrain)
        self.captures.add(capture.group())

    def get_captures(self):
        return self.captures


# is_upcoming_features_enabled('ENG-12345')

if __name__ == '__main__':
    soap = CaptureTheFlag()
    for line in sys.stdin:
        soap.scan(terrain=line)
    for capture in soap.captures:
        sys.stdout.write(f"{capture}\n")

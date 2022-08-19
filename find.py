import sys
import re


class CaptureTheFlag:

    def __init__(self, matcher):
        self.captures = set()
        self.matcher = matcher

    def scan(self, terrain):
        _n_destroy = self.matcher
        capture = re.search(_n_destroy, terrain)
        self.captures.add(capture.group())

    def get_captures(self):
        return self.captures


# is_upcoming_features_enabled('ENG-12345')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Missing matcher argument")
        sys.exit(2)
    matcher = sys.argv[1]
    soap = CaptureTheFlag(matcher)
    for line in sys.stdin:
        soap.scan(terrain=line)
    for capture in soap.captures:
        sys.stdout.write(f"{capture}\n")

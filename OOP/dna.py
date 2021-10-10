# Testing super class

class RNA():
    def __init__(self, sequence):
        self.sequence = sequence
        self.length = len(sequence)
        self.counts = {'A': 0, 'U': 0, 'C': 0, 'G': 0}
        for nt in sequence:
            self.counts[nt] += 1
        self.gc_content = (self.counts['G'] + self.counts['C']) / self.length


class DNA(RNA):
    def __init__(self, sequence):
        super().__init__(sequence)
        self.counts['T'] = self.counts['U']
        del self.counts['U']
        self.counts['A'] = self.counts['T']
        del self.counts['T']
        self.rna = RNA(self.sequence)

#!/usr/bin/env python3

from scale import Scale

import const

class Note():
    def __init__(self, root, accidentals='')
        self.root = self.set_root()
        self.accidentals = self.set_accidentals()

    def __str__(self):
        return f"{self.root}{self.accidental}"

    def set_root(self, root):
        self.root = root.lower()

    def set_accidental(self, accidentals):
        self.accidentals = accidentals or ''

    def get_accidentals_semitone_shift(self):
        return self.accidentals.count('#') - self.accidentals.count('b')

    def get_root_semitones(self):
        return const.notes.index(self.root)

    def chromatic_transpose(self, semitones):
        """
        Transpose note in chromatic scale
        """
        scale = Scale(root='C', notes=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
        return self.diatonic_transpose(semitones, scale)

    def diatonic_transpose(self, semitones, scale):
        starting_semitones = self.get_root_semitones + self.get_accidentals_semitone_shift()


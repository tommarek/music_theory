#!/usr/bin/env python3

from math import pow

from scale import Scale

import const

class Note():

    def __init__(self, root, accidentals='', octave=None):
        self.root = self.set_root(root)
        self.accidentals = self.set_accidentals(accidentals)
        self.octave = self.set_octave(octave)

    def __str__(self):
        return f"{self.root}{self.accidentals}{self.octave}"

    def set_root(self, root):
        return root.upper()

    def set_accidentals(self, accidentals):
        return accidentals or ''

    def set_octave(self, octave):
        assert isinstance(octave, int), 'Pitch has to be int'
        assert octave >= 0, 'Pitch has to be >= 0'

        return octave

    @property
    def frequency(self):
        if not self.octave:
            return None

        note_index = self.get_note_semitones()
        absolute_note_index = note_index + ((self.octave) * 12)
        return const.C0_FREQ * pow(2, (absolute_note_index) / 12)

    def get_accidentals_semitone_shift(self):
        return self.accidentals.count('#') - self.accidentals.count('b')

    def get_root_semitones(self):
        return const.NOTES.index(self.root)

    def get_note_semitones(self):
        return self.get_root_semitones() + self.get_accidentals_semitone_shift()

    def chromatic_transpose(self, semitones):
        """
        Transpose note in chromatic scale
        """
        scale = Scale(root='C', notes=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
        return self.diatonic_transpose(semitones, scale)

    def diatonic_transpose(self, semitones, scale):
        starting_semitones = self.get_note_semitones()

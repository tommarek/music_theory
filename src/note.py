#!/usr/bin/env python3

import re

from math import pow

import const

from scale import Scale


class Note():
    def __init__(self, name=""):
        parsed = self._parse_note_name(name)
        if parsed:
            self.root = self.set_root(parsed[0])
            self.accidentals = self.set_accidentals(parsed[1])
            self.octave = self.set_octave(int(parsed[2]))

    def _parse_note_name(self, name):
        parsed = re.findall(r'^([a-gA-G])([#|b]*)(\d?)$', name)
        return parsed[0] if parsed else (None, None, None)

    def __str__(self):
        return f"{self.root}{self.accidentals}{self.octave}"

    def set_root(self, root):
        assert isinstance(root, str), "Root has to be a string"
        assert root.upper() in const.NOTES

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

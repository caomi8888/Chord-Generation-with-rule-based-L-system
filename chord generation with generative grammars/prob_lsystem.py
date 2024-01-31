from music21 import chord, metadata, stream
from music21 import environment
import random

#set the musesocre environment
path_to_musescore = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"

us = environment.UserSettings()
us['musescoreDirectPNGPath'] = path_to_musescore
us['musicxmlPath'] = path_to_musescore

class ProbabilisticLSystem:
    """
    A basic L-system class that provides functionality for generating sequences
    based on initial axiom and production rules.
    """

    def __init__(self, axiom, rules, probabilities):
        """
        Initialize the L-system with an axiom and production rules.

        Parameters:
        - axiom (str): The initial symbol.
        - rules (dict): A dictionary where keys are symbols and values are
            the corresponding replacement strings. For example, {"A": "ABC"}
        """
        self.axiom = axiom
        self.rules = rules
        self.output = axiom
        self.probabilities = probabilities

    @property
    def alphabet(self):
        """
        Get the alphabet of the L-system.

        Returns:
        - set: The alphabet of the L-system.
        """
        return set(self.axiom + "".join(self.rules.values()))

    def iterate(self, n):
        """
        Apply the production rules to the current output n times.

        Parameters:
        - n (int): Number of times the rules are to be applied.

        Returns:
        - str: The output after applying the rules n times.
        """
        final_output =[]
        final_output.append(self.output)
        for i in range(n):
            next_output = self._iterate_once(final_output[-1])
            final_output.append(next_output)
            print(f"Output after {i + 1} iteration(s): {final_output}")

        #self._reset_output()
        return "".join(final_output)

    def _iterate_once(self,final_output):
        """
        Apply the production rules to the current output once.

        Returns:
        - str: The output after applying production rules once.
        """
        next_symbol = self._apply_rule(final_output[-1])
        return next_symbol[0]


    def _apply_rule(self, symbol):
        """
        Apply production rules to a given symbol.

        Parameters:
        - symbol (str): The symbol to which rules are to be applied.

        Returns:
        - str: The transformed symbol or original symbol if no rules apply.
        """
        if symbol in self.rules:
            # Use probabilities to select the next symbol
            next_symbols = self.rules[symbol]
            next_symbol_probabilities = self.probabilities[symbol]
            next_symbol = random.choices(next_symbols, weights=next_symbol_probabilities, k=1)#[0]
            return  next_symbol
        else:
            return symbol

    def _reset_output(self):
        """Reset the output to the initial axiom."""
        self.output = self.axiom


def l_system_to_music21_chords(chord_sequence):
    """
    Translate the L-system generated chord sequence into a list of music21
    chords.

    Parameters:
    - chord_sequence (str): The L-system generated chord sequence.

    Returns:
    - list of music21.chord.Chord: The corresponding chord progression in music21 format.
    """
    chord_dict = {
        "C": ["C", "E", "G"],  # Cmaj
        "D": ["D", "F", "A"],  # Dmin
        "E": ["E", "G", "B"],  # Emin
        "F": ["F", "A", "C"],  # Fmaj
        "G": ["G", "B", "D"],  # Gmaj
        "A": ["A", "C", "E"],  # Amin
        "B": ["B", "D", "F"],  # Bdim
    }
    return [chord.Chord(chord_dict[chord_name]) for chord_name in
            chord_sequence if chord_name in chord_dict]


def create_and_show_music21_score(music21_chords):
    """
    Create and display a music score using the music21 library.

    This function takes a list of music21 chord objects and creates a score
    with them. It then displays this score. The score is titled "L-System Chord Progression".

    Parameters:
    - music21_chords (list): A list of music21 chord objects.
    """

    # Create a new music21 stream.Score object
    score = stream.Score()

    # Set the metadata for the score with a title
    score.metadata = metadata.Metadata(title="L-System Chord Progression")

    # Create a new music21 stream.Part object
    part = stream.Part()

    # Loop through each chord in the music21_chords list
    for chord in music21_chords:
        # Append each chord to the Part object
        part.append(chord)

    # Append the Part object containing chords to the Score object
    score.append(part)

    # Display the score
    score.show()


def main():
    """
    Main function to demonstrate the generation of chord progression using L-system.
    """
    # Axiom: "C"
    # Production rules: e.g."C": ['C','D','E','F','G','A','B']
    axiom = "C"
    rules = {"C": ['C','D','E','F','G','A','B'],
             "D": ['F','G','B'],
             "E": ['D','F','A'],
             "F": ['C','E','G','B'],
             "G": ['C'],
             "A": ['D','F','G','C'],
             "B": ['C','E']}

    probabilities = {
        "C": [1, 1, 1, 1, 1, 1, 1],  # Probabilities for each symbol in rules["C"]
        "D": [1, 1, 1],  # Probabilities for each symbol in rules["D"]
        "E": [1, 1, 1],
        "F": [1, 1, 1, 1],
        "G": [1],
        "A": [1, 1, 1, 1],
        "B": [1, 1]
    }

    l_system = ProbabilisticLSystem(axiom, rules, probabilities)

    chord_sequence = l_system.iterate(
        20
    )  # The number determines how many times the rules will be applied
    music21_chords = l_system_to_music21_chords(chord_sequence)

    create_and_show_music21_score(music21_chords)


if __name__ == "__main__":
    main()

# L-System Chord Generation

This README explains how to use an L-system for generating chord progressions and how to use the `music21` library in combination with MuseScore 4 to display and play the generated score.

## Starting Chord

The initial chord chosen for the progression is C major, but you can choose any starting point depending on your musical preference or requirements.

## Chord Generation Rules

Two different sets of rules are provided for generating chord progressions:

### Version 1: Arbitrary Rules

The first version uses arbitrary rules to construct the chord progression. This method does not necessarily follow traditional music theory but can generate unique and experimental progressions.

### Version 2: Music Theory-Based Rules

The second version constructs chord progressions based on music theory. This approach has more practical significance as it adheres to common practices in music composition, resulting in progressions that are more likely to sound harmonious and pleasing.

## Connecting to MuseScore 4

Generated chord progressions can be connected to MuseScore 4 via the `music21` library. This allows for the progression to be visualized in standard musical notation and played back using MuseScore's playback features.

### Installation

Ensure you have MuseScore 4 installed on your system and `music21` installed in your Python environment.

### Configuration

Set up `music21` to use MuseScore 4 for displaying scores by configuring the path to the MuseScore executable in your Python script:

```python
path_to_musescore = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"
from music21 import environment
us = environment.UserSettings()
us['musescoreDirectPNGPath'] = path_to_musescore
us['musicxmlPath'] = path_to_musescore
```

### Usage

Once configured, you can use `music21` to create a score object from the generated chord progression and then display it using MuseScore 4:

```python
# Assuming `music21_chords` is a list of music21 chord objects generated from the L-system
score = music21.stream.Score()
part = music21.stream.Part()
for chord in music21_chords:
    part.append(chord)
score.append(part)
score.show()
```

Enjoy experimenting with L-systems to create unique chord progressions and exploring them musically with MuseScore 4.


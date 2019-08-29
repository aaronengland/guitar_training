# guitar_training

## chord_trainer<br />
A function to aid in chord progression training by looping through a key of chords in a progression for an amount of time at a frequency.

Example:

```from guitar_training import chord_trainer```<br />

```# list of chords in G-major scale```<br />
```list_of_chords = ['G','A-minor','B-minor','C','D','E-minor','F-diminished']```<br />

```# desired progression```<br />
```progression = [1, 4, 5, 1]```<br />

```# start training for 30 seconds with a 2 second delay between chords```<br />
```chord_trainer(list_of_chords, progression, seconds=30, delay=2)```<br />


To install, use: ```pip install git+https://github.com/aaronengland/guitar_training.git```

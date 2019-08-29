# guitar trainer
import time
import datetime

# define function
def chord_trainer(list_of_chords, progression, seconds=30, delay=2):
    """
    Example:
    
    # list of chords
    list_of_chords = ['G','A-minor','B-minor','C','D','E-minor','F-diminished']

    # progression
    progression = [1, 4, 5, 1]

    chord_trainer(list_of_chords, progression, seconds=30, delay=2)
    """
    # find the chords belonging to the progression
    list_chords_in_progression = [list_of_chords[x-1] for x in progression]
    # set elapsed time to 0
    elapsed_time = 0
    # start timer
    start_time = datetime.datetime.now()
    while elapsed_time < seconds:
        for i in range(len(list_chords_in_progression)):
            # get current chord
            current_chord = list_chords_in_progression[i]
            print(current_chord)
            # get next chord
            if i == (len(list_chords_in_progression)-1):
                next_chord = list_chords_in_progression[0]
            else:
                next_chord = list_chords_in_progression[i+1]
            print('Next up: {}'.format(next_chord))
            # delay n seconds
            time.sleep(delay)
            # get current time
            end_time = datetime.datetime.now()
            # get elapsed time
            elapsed_time = (end_time - start_time).seconds
        
import datetime
import time_as_words_german
import wordclock_tools.wordclock_colors as wcc

class plugin:
    '''
    A class displaying the current time on a german WCA as real words...
    '''

    def __init__(self, config):
        '''
        Initializations for the startup of the current wordclock plugin
        '''
        self.name = 'time_as_words_german'
        self.taw = time_as_words_german.time_as_words_german()
        self.bg_color_index     = 0 # default background color: black
        self.word_color_index   = 2 # default word color: warm white

    def run(self, wcd):
        '''
        Displays time in words.
        User interaction on pin button_return needs to be implemented on demand.
        '''
        # Set background color
        wcd.setColorToAll(wcc.colors[self.bg_color_index], includeMinutes=True)
        # Set current time
        now = datetime.datetime.now()
        wcd.showText(self.taw.get_time(now))



from time import sleep
import pygame   # python3 -m pip install pygame
from array import array
import sys
from pygame.locals import QUIT


# admin stuff 
USING_CIRCUITRY = False

if USING_CIRCUITRY:
    import RPi.GPIO as GPIO
else:
    GPIO = '' # stub out the errors

# constants
MIXER_FREQ = 44100 # 44.1 KHz
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

# pygame setup
pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

if USING_CIRCUITRY == False:
    pygame.display.set_mode((500, 500))

# note class
class Note(pygame.mixer.Sound):

    def __init__(self, frequency, volume):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, buffer=self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        # calculate the period of the note's wave

        # if the note freq is  261.6 (c), then we get int(round(44100/261.6)) -> 169 
        period = int(round(MIXER_FREQ/self.frequency))

        # calculate the amplitude for the note
        # gives values between -32768 and 32767
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1

        # setup samples array
        # h is for signed integer 2 bytes (16 bits)
        samples = array("h", [0]*period)

        # generate the samples

        # for the square wave
        for t in range(period):
            if (t < (period / 2)):  # its piecewise!
                samples[t] = amplitude  # this is the output of the function!
            else:
                samples[t] = -1 * amplitude # this is also the output

        return samples


# piano class
class Piano:
    C4 = Note(261.6, 1)
    E4 = Note(329.6, 1)
    G4 = Note(392.0, 1)
    C5 = Note(523.3, 1)

    # for the pi
    input_pins = [20, 16, 12, 26]
    notes = [C4, E4, G4, C5]

    # functions for the pi
    @staticmethod
    def wait_for_note_start():
        while True:
            for index in range(len(Piano.input_pins)):
                if GPIO.input(Piano.input_pins[index]):
                    return index
            sleep(0.01)
    
    @staticmethod
    def wait_for_note_stop(input_pin):
        while GPIO.input(input_pin):
            sleep(0.1)

# a little more setup
if USING_CIRCUITRY:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Piano.input_pins, GPIO.IN, GPIO.PUD_DOWN)


# main program
print("Welcome to PIano!")
print("Press ctrl+c to exit...")

try:
    while True:
        if USING_CIRCUITRY:
            index = Piano.wait_for_note_start()
            Piano.notes[index].play(-1) # play infinitely (-1)
            Piano.wait_for_note_stop(Piano.input_pins[index])
            Piano.notes[index].stop()
        else:
            # use the pygame event loop
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        Piano.C4.play(-1)
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        Piano.C4.stop()
        pygame.display.update()  

except KeyboardInterrupt:
    if USING_CIRCUITRY:
        GPIO.cleanup()
    else:
        exit()
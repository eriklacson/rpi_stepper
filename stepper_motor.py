#
# Import required libraries
#
import sys
import time
import RPi.GPIO as GPIO

class StepperMotor():
  """A class for controlling a stepper motor from a Raspberry Pi"""

  def __init__(self):
    self.stepPins = [17,22,23,24]
    self.seq = [[1,0,0,1],
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1]]
    self.stepCount = len(self.seq)
    self.setPins()

  def setPins(self):
    """Initialize Stepper Motor Settings """
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    for pin in self.stepPins:
      print "Setup pin: " + str(pin)
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, False)

  def turn(self, wait, steps, stepdir):
    # Set turn rate
    WaitTime = int(wait)/float(1000) 
    
    #initialize StepCounter to 0
    StepCounter = 0

    # Start main loop
    while (steps >= 0):

      print StepCounter,
      print self.seq[StepCounter]

      for pin in range(0, 4):
        xpin = self.stepPins[pin]

        if self.seq[StepCounter][pin]!=0:
          print " Enable GPIO %i" %(xpin)
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      
      StepCounter += stepdir

      # If we reach the end of the sequence
      # start again
      if (StepCounter >= self.stepCount):
        StepCounter = 0
      if (StepCounter < 0):
        StepCounter = self.stepCount + stepdir

      steps = steps - 1  
      # Wait before moving on
      time.sleep(WaitTime)    


  def spin(self, wait, stepdir):
    # Read 
    WaitTime = int(wait)/float(1000)
    StepCounter = 0

    # Start main loop
    while True:

      print stepdir
      print StepCounter,
      print self.seq[StepCounter]

      for pin in range(0, 4):
        xpin = self.stepPins[pin]

        if self.seq[StepCounter][pin]!=0:
          print " Enable GPIO %i" %(xpin)
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      
      StepCounter += stepdir

      # If we reach the end of the sequence
      # start again
      if (StepCounter >= self.stepCount):
        StepCounter = 0
      if (StepCounter < 0):
        StepCounter = self.stepCount + stepdir

      # Wait before moving on
      time.sleep(WaitTime)

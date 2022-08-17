def run_me():
  print('hello world')
  from machine import Pin
  # create an output pin on pin #0
  p0 = Pin(0, Pin.OUT)

  # set the value low then high
  p0.value(0)
  p0.value(1)

  # create an input pin on pin #2, with a pull up resistor
  p2 = Pin(2, Pin.IN, Pin.PULL_UP)

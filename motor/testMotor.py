#!/usr/bin/env python

import RPIO

RPIO.setup(18,RPIO.OUT, initial=RPIO.LOW);
RPIO.output(18,True);

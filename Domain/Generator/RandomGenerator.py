# -*- coding: utf-8 -*-

from DomainInterface.DomainBehavior import DomainBehavior
from DomainInterface.Object import Message

import random

class RandomGenerator(DomainBehavior):
    """
        @author: Bastien POGGI
        @organization: University Of Corsica
        @contact: bpoggi@univ-corse.fr
        @since: 2010.12.1
        @version: 1.0
    """

    def __init__(self, minValue=0, maxValue=10, minStep=1, maxStep=1, start=0, choice=[]):
        """ Constructor.

            @param minValue: minimum value
            @param maxValue: maximum value
            @param minStep: minimum step
            @param maxStep: maximum step
			@param start: time start
			@param choice: list of items 

        """
        DomainBehavior.__init__(self)

        self.minValue = minValue
        self.maxValue = maxValue
        self.minStep = minStep
        self.maxStep = maxStep
        self.choice = choice

        self.msg = Message(None, None)

        self.initPhase('START',float(start))

    def outputFnc(self):
        """ lambda DEVS function
        """
        numberMessage = random.randint(1, len(self.OPorts))  # Number message to send
        portsToSend = random.sample(self.OPorts, numberMessage)  # The port with number message

        for port in portsToSend:
            if self.choice:
                value = random.choice(self.choice) 
            else:
                value = random.randint(self.minValue, self.maxValue)
            self.msg.value = [value, 0.0, 0.0]
            self.msg.time = self.timeNext
            ### adapted with PyPDEVS
            return self.poke(port, self.msg)

    def intTransition(self):
        """ DEVS Transition function
        """
        self.state['sigma'] = random.randint(self.minStep, self.maxStep)
        ### adapted with PyPDEVS
        return self.getState()

    def __str__(self):
        """ str function
        """
        return "RandomGenerator"

    def timeAdvance(self):
        """ Time advance function
        """
        return self.getSigma()
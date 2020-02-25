#!/usr/bin/env python
""" Created by Morten Mjelva on 10/10/2017.
Copyright (C) 2017 Morten Mjelva. All rights reserved."""

__author__      = "Morten Mjelva"
__copyright__   = "Copyright (C) 2017 Morten Mjelva"
__license__     = "BSD"
__version__     = "1.0"
__all__         = []

import actionlib
import rospy
from cyborg_controller.msg import StateMachineAction, EmotionalFeedback

class IdleServer():
    """IdleServer"""

    # Initialization
    def __init__(self):
        self._publisher = rospy.Publisher("/cyborg_controller/emotional_feedback", EmotionalFeedback, queue_size=100)
        self._action_name = rospy.get_name() + "/idle"
        self._as = actionlib.SimpleActionServer(self._action_name, StateMachineAction, execute_cb=self.execute_cb, auto_start=False)
        self._as.start()
        rospy.loginfo("IdleServer: Activated")

    # Called when the controller (state machine) sets the idle state as active
    def execute_cb(self, goal):
        r = rospy.Rate(1)
        rospy.loginfo("IdleServer: Executing idle state...")

        while True:
            # Check that preempt hasn't been requested by the client
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                break

            # Sleep for a while
            r.sleep()

            # Increase "boredom" by lowering PAD values
            msg = EmotionalFeedback()
            val = -0.05
            msg.delta_pleasure  = val
            msg.delta_arousal   = val
            msg.delta_dominance = val

            self._publisher.publish(msg)


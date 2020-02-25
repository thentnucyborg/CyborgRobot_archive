#!/usr/bin/env python
""" Created by Morten Mjelva on 10/10/2017.
Copyright (C) 2017 Morten Mjelva. All rights reserved."""

__author__      = "Morten Mjelva"
__copyright__   = "Copyright (C) 2017 Morten Mjelva"
__license__     = "BSD"
__version__     = "1.0"
__all__         = []

import rospy
from idleserver import IdleServer

def main():
    rospy.init_node("cyborg_idle")
    idle_server = IdleServer()
    rospy.spin()

if __name__ == "__main__":
    print("Cyborg Idle: Starting Program...")
    main()
    print("Cyborg Idle: End of Program...")


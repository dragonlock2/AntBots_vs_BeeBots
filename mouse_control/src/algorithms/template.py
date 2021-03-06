#!/usr/bin/env python3
import rospy

from mouse_description.msg import MouseCommand

# constants
WORLD_HEIGHT = rospy.get_param('/WORLD_HEIGHT')
WORLD_WIDTH = rospy.get_param('/WORLD_WIDTH')

# code to run before node even starts
print('Hello! I\'m the template algorithm!')

# private variables
myFlag = None
enemyFlag = None
reconMap = [[' ' for j in range(WORLD_HEIGHT)] for i in range(WORLD_WIDTH)]

# helpers
def computeFlags(rmap):
	global myFlag, enemyFlag
	for x in range(WORLD_WIDTH):
		for y in range(WORLD_HEIGHT // 2):
			if rmap[x][y] == 'F':
				if ISANT:
					myFlag = (x,y)
				else:
					enemyFlag = (x,y)
	for x in range(WORLD_WIDTH):
		for y in range(WORLD_HEIGHT // 2, WORLD_HEIGHT):
			if rmap[x][y] == 'F':
				if ISANT:
					enemyFlag = (x,y)
				else:
					myFlag = (x,y)

# standard interface functions
def initAlg(isant, numMice):
	global ISANT, NUM
	ISANT = isant
	NUM = numMice

def computeMoves(miceMoves, score, miceData, omniMap):
	# miceMoves - modify this with the moves u wanna do
	# score - current score, see mouse_control/msg/Score.msg

	# Level 1: Omniscient - available data
	# omniMap - xy-indexed, see mouse_control/msg/Omniscience.msg (also can print out in god node leakMap)

	# Level 2: Hivemind - available data
	# omniMap - just use your half and ignore the rest
	# miceData - telemetry data from each mouse, see mouse_description/msg/MouseData.msg

	# First call should not have any flags captured, so can grab flag locations from there
	# keep in mind these are base locations, need to re-search if flag is stolen
	if not (myFlag and enemyFlag):
		computeFlags(omniMap)

	# Compute some moves
	# keep in mind ants go first, then bees, but tag and point logic doesn't apply until bees are done
	for i in range(NUM):
		computeMouseMove(i, miceMoves, score, miceData, omniMap, reconMap, myFlag, enemyFlag)

def computeMouseMove(idx, miceMoves, score, miceData, omniMap, reconMap, myFlag, enemyFlag):
	# standard interface to merge 1v1 strats or even larger
	# compute move for one mouse

	# Level 1: Omniscient
	# use all the info u need, but only change one mouse pls

	# Level 2: Hivemind
	# use reconMap instead of omniMap

	# Level 3: Minion
	# ignore omniMap and only use ur own miceData[idx]

	if ISANT:
		miceMoves[idx].type = MouseCommand.LEFT
	else:
		miceMoves[idx].type = MouseCommand.RIGHT
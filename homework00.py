#!/usr/bin/python2
import rospy
if __name__=='__main__':
	rospy.init_node('Net_kak')
	inp = int(input())
	fi = int(input())
	se = int(input())
	if inp == 1:
		print('%.2f'%(fi+se))
	if inp == 2:
		print('%.2f'%(fi-se))

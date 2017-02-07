import pygame
from pygame.locals import * 
from sys import exit
import time
pygame.init()
def OpeningText():
	print "***********************"
<<<<<<< HEAD
	print "**  SCORING SYSTEM   **"
	print "**   triwandha16     x*"
=======
	print "**  SCORING SYSTEM   *s*"
>>>>>>> testing
	print "***********************"
	pygame.joystick.init()
	joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

def reRead(aValue, aAxis, aStik):
	for eventX in pygame.event.get(): 
		if eventX.type == JOYAXISMOTION:
			bValue = eventX.value
			bAxis = eventX.axis
			if not eventX:
				pass
			if aStik != eventX.joy: 
				if aAxis == bAxis:
					if aValue == bValue:
						return True
	return False
		
def main():	
	 
	OpeningText()
	joysticks = []
	for joystick_no in range(pygame.joystick.get_count()):
		stick = pygame.joystick.Joystick(joystick_no)
		stick.init()
		joysticks.append(stick);
	print joysticks
	while True: 
		try:
			
			event = pygame.event.wait()
			if event.type == JOYAXISMOTION:
				if event.value != 0:
					aValue = event.value
					aAxis = event.axis
					i = 1;
					for i in range(4):
						r = reRead(aValue, aAxis, event.joy)
						if r:
							if aValue == 1.0 and aAxis==1:
								print "Scoring = 1"
							if aValue == 1.0 and aAxis==0:
								print "Scoring = 2"
							break
						else :
							print "no input for .. ", i
						i+=1
						time.sleep(0.1)
						
									
			if event.type==QUIT:
				pygame.quit()
				exit()
				
			
		except KeyboardInterrupt:
			print("\n" "Interrupted")
			exit(0)
		
	

if __name__ == "__main__":
    main()
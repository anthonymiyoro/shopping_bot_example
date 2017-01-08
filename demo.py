import gym
import universe
import random

def determine_turn(turn, j, total_sum, reward, prev_total_sum, observation_n)


def main():

	# initialise environment
	env = gym.make('flashgames.CoasterRacer-v0')
	observation_n = env.reset()

	# init variables
	# iterations
	n = 0
	j = 0

	# sum of observations
	total_sum = 0
	prev_total_sum = 0
	turn = False

	# define key events
	left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent',
	         'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)],
    right = [('KeyEvent', 'ArrowUp', True) ,('KeyEvent', 'ArrowLeft', False) ,('KeyEvent', 'ArrowRight', True)]
    forward = [('KeyEvent', 'ArrowUp', True) ,('KeyEvent', 'ArrowLeft', False) ,('KeyEvent', 'ArrowRight', False)]

    while True:
    	# add iterations
    	n+=1

    	if(n > 1):
    	# check for first feedback
	    	if(observation_n[0] != None):
	    		# put the reward in prev_score
	    		prev_score = reward_n[0]

	    		# if turn is true, pick a random event
	    		if(turn):
	    			event = random.choice([left, right])
	    			# perform an action
	    			action_n = [event for ob in observation_n]
	    			# return turn to false
	    			turn = False

		# if no turn is needed go forward
		elif(~turn):
			action_n = [forward for ob in observation_n]

		# if there is feedback then check if you need to make a turn
		if(observation_n[0] != None):
			turn, j, total_sum, prev_total_sum = determine_turn(turn, j, total_sum, reward, prev_total_sum, observation_n[0])

		#save new values after implementation
		observation_n, reward_n, done_n, info = env.step(action_n)

		env.render()

	if __name__ == '__main__':
		main()
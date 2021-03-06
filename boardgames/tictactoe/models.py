from django.db import models
from django.contrib.auth.models import User

# Create your models here.	
GAME_STATUS_CHOICES = (
	('A', 'Active'),
	('F', 'First Player Wins'),
	('S', 'Second Player Wins'),
	('D', 'Its a Draw')
)

class Game(models.Model):
	first_player 	= models.ForeignKey(User, related_name = "games_first_player")
	second_player 	= models.ForeignKey(User, related_name = "games_second_player")
	next_to_move 	= models.ForeignKey(User, related_name = "games_to_move")
	start_time 		= models.DateTimeField(auto_now = True)
	last_active		= models.DateTimeField(auto_now = True)
	status 			= models.CharField(max_length=1, default='A', choices = GAME_STATUS_CHOICES)	#A = active

	def __str__(self):
		return "{0} vs {1}".format(self.first_player, self.second_player)
 
class Move(models.Model):
	x 		= models.IntegerField()
	y 		= models.IntegerField()
	comment = models.CharField(max_length = 300)
	game 	= models.ForeignKey(Game)
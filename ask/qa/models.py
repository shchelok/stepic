from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Model):
        def new():
                new = Question.objects
                new = new.order_by('added_at')
                return new[:5]
        def popular():
                pop = Question.objects
                pop = pop.order_by('rating')
                return pop[:]

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank = True, auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.OneToOneField(User)
	likes = models.ManyToManyField(User, related_name='question_like_user')
	objects = QuestionManager()
'''	
	class QuestionManager:
		def new():
	questions = = models.ManyToManyField(Question)
	def new():
		return 

	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return '/post/%d/' % self.pk
	class Meta:
		db_table = 'blogposts'
		ordering = ['-creation_date']
'''

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	question = models.OneToOneField(Question, on_delete=models.CASCADE)
	author = models.OneToOneField(User)


'''
class Likes(models.Model):
    question = models.ForeignKey(Question,related_name="like_question")
    user = models.ForeignKey(User,related_name="like_user")
'''

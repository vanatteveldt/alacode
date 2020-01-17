from django.contrib.auth.models import User
from django.db import models

Q5_CHOICES = [
    (0, 'The source does not contain a discernible opinion on vaccines'),
    (1, 'Strongly Against'),
    (2, 'Against'),
    (3, 'Neutral'),
    (4, 'In Favor'),
    (5, 'Strongly In Favor')
]

Q6_CHOICES = [
    (0, 'The tweet does not contain a discernible opinion on vaccines'),
    (1, 'Strongly Against'),
    (2, 'Against'),
    (3, 'Neutral'),
    (4, 'In Favor'),
    (5, 'Strongly In Favor')
]

Q7_CHOICES = [
    (0, 'The tweet does not contain a discernible opinion towards the source'),
    (1, 'Strongly disagrees'),
    (2, 'disagrees'),
    (3, 'Neutral'),
    (4, 'Agrees'),
    (5, 'Strongly agrees')
]

Q8_CHOICES = [
    (0, 'The tweet does not contain a discernible opinion towards the source'),
    (1, 'Very Negative'),
    (2, 'Negative'),
    (3, 'Neutral'),
    (4, 'Positive'),
    (5, 'Very positive')
]

EMOTION_CHOICES = [
    (0, 'No'),
    (1, 'Yes')
]

class Tweet(models.Model):
    tweet = models.CharField(max_length = 280)
    url = models.CharField(max_length = 280)

    def __str__(self):
        return self.tweet

class Code(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    q1 = models.BooleanField("q1", help_text="ERROR 1: the tweet has nothing to do with the societal discussion around vaccines (tick box & continue to next tweet)")
    q2 = models.BooleanField("q2", help_text="ERROR 2: the link is not working / does not refer to a news article or blog (tick box & continue to next tweet")
    q3 = models.BooleanField("q3", help_text="Tick the box if the tweet doesn't contain any text next to the link")
    q4 = models.BooleanField("q4", help_text="Tick the box if the tweet only contains the title/header of the shared article")
    q5 = models.IntegerField("q5", help_text= "To what extent would you describe the shared article as in favor or against the use of vaccines?", choices=Q5_CHOICES, default=0)
    q6 = models.IntegerField("q6", help_text= "To what extent would you describe the text in the tweet as in favor or against the use of vaccines?", choices=Q6_CHOICES, default=0)
    q7 = models.IntegerField("q7", help_text= "To what extent does the text in the tweet (dis)agree withqi the source?", choices=Q7_CHOICES, default=0)
    q8 = models.IntegerField("q8", help_text= "To what extent would you describe the text in the tweet as positive or negative towards the source?", choices=Q8_CHOICES, default=0)
    q9 = models.IntegerField("q9", help_text= "Does the tweet express feelings of enthusiasm?", choices=EMOTION_CHOICES, default=0)
    q10 = models.IntegerField("q10", help_text="Does the tweet express feelings of anger?", choices=EMOTION_CHOICES, default=0)
    q11 = models.IntegerField("q11", help_text="Does the tweet express feelings of fear?", choices=EMOTION_CHOICES, default=0)
    q12 = models.CharField("q12", help_text="Notes", max_length=500, default='no notes')


    #tweet = models.ForeignKey('tweet', on_delete=models.CASCADE)
    class Meta:
        unique_together = ["tweet", "user"]

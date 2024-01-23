from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    department = models.CharField(max_length=100)
    answer_the_question = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    own = models.ManyToManyField(Question)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class VoteResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Choice, on_delete=models.CASCADE)
    correct_answer = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}: {self.question}'

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'


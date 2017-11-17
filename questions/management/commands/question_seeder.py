from django.core.management import BaseCommand
from questions.models import *
import random
import time
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    help = "Seeding database with test question data"

    # A command must define handle()
    def handle(self, *args, **options):
        for question in Question.objects.all():
            question.delete()
        for tag in Tag.objects.all():
            tag.delete()

        tags = [
            Tag(title='python',color="info"),
            Tag(title='django',color="success"),
            Tag(title='php',color="danger"),
            Tag(title='java',color="info"),
            Tag(title='c++',color="danger")
        ]
        for tag in tags:
            tag.save()
        for i in range(1,25):
            question = Question(
                title='Python question '+str(i),
                description='Python question`s description '+str(i),
                rating=i,
            )
            question.save()
            question.tags.add(tags[i % 5])
            question.tags.add(tags[((i+1) % 5)])

            correct_answer = Answer(
                description='Python quesion`s correct answer'+str(i),
                correctness=1,
                rating=i,
                question=question,
            )
            correct_answer.save()
            incorrect_answer = Answer(
                description='Python quesion`s incorrect answer' + str(i),
                correctness=0,
                rating=i,
                question=question,
            )
            incorrect_answer.save()

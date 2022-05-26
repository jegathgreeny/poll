import os, random

# Permission to modify data.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poll.settings")

import django
# Initialzie django
django.setup()


from faker import Faker
from polls.models import Question, Choice


fakegen = Faker()


def add_questions():
    fake_ques = fakegen.name()
    ques = Question.objects.get_or_create(
        text=fake_ques)[0]
    ques.save()
    return ques


def populate(n):

    for i in range(n):

        question = add_questions()
        fake_choices = fakegen.url()
        fake_votes = fakegen.pyint(min_value=0, max_value=100)
        choice = Choice.objects.get_or_create(question=question, text=fake_choices, votes=fake_votes)


if __name__ == "__main__":
    print("Populating script!")
    populate(20)
    print("Populating complete...")

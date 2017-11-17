from .models import *
from .paginator import Paginate


def get_questions_list(page=1):
    questions = Question.objects.order_by('pub_date').all()
    questions_paginator = Paginate(questions, 5)
    return questions_paginator.paginate(int(page))


def get_question_by_id(question_id=1):
    return Question.objects.get(pk=question_id)


def add_answer(msg, question_id=1):
    question = Question.objects.get(pk=question_id)
    answer = Answer(
        description='Python quesion`s users answer: '+msg,
        correctness=0,
        rating=0,
        question=question,
    )
    answer.save()


def get_tags_cloud():
    return Tag.objects.all()


def get_tag(tag_id):
    return Tag.objects.get(pk=tag_id)


def get_page_env():
    return {
        'tags' : get_tags_cloud()
    }


def get_list_by_tag(tag_id=1, page=1):
    questions = Question.objects.filter(tags=tag_id).order_by('pub_date').all()
    questions_paginator = Paginate(questions, 5)
    return questions_paginator.paginate(int(page))
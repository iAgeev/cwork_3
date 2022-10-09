# Functions for app
import json


def get_posts_all():
    """Возвращает посты"""
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_all():
    """Возвращает комментарии"""
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя. Функция должна вызывать ошибку `ValueError`
    если такого пользователя нет и пустой список, если у пользователя нет постов"""
    posts = get_posts_all()
    posts_user = []
    for post in posts:
        if user_name.lower() not in post['poster_name']:
            return "нет такого пользователя"
        elif post['poster_name'].lower() == user_name.lower():
            posts_user.append(post)
        return posts_user


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста.
    Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов"""
    comments_id = []
    comments = get_comments_all()
    for comment in comments:
        if comment['post_id'] == post_id:
            comments_id.append(comment)
    return comments_id


def get_comments_count(pk):
    """Возвращает количество комментариев к определенному посту"""
    comments = get_comments_all()
    count = 0
    for comment in comments:
        if comment['post_id'] == pk:
            count += 1
    return count


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    posts_query = []
    for post in posts:
        if query in post:
            posts_query.append(post)
    return posts_query


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post
        else:
            return "нет такого поста"


# Напишите к каждой функции юнит тесты, расположите тесты в отдельной папке `/tests`.
# Организуйте тесты в виде классов или функций, на ваше усмотрение.


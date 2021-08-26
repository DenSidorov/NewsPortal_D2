# py manage.py shell --> Запуск shell

# from newapp.models import * --> импортируем модели
# User1 = User.objects.create(username='Den', first_name ='Sid') --> Создаём юзера
# Author.objects.create(Author.User=User1) --> Делаем юзера автором
# User2 = User.objects.create(username='Max', first_name ='Sid') --> Создаём 2 юзера
# Author.objects.create(Author.User=User2) --> Делаем юзера автором
# Category.objects.create(name='Python') --> Создаём категорию
# Category.objects.create(name='Django') --> Создаём категорию
# Category.objects.create(name='JS') --> Создаём категорию
# Category.objects.create(name='OOP') --> Создаём категорию
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Den')), categoryType='NW', title='aergknearklgn', text='ktjhgnwe;rlhnew;lkhnwe;lhkne;hlkwenh;l') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Max')), categoryType='AR', title='11122233444555', text='9998887776665444') --> Создаём пост
# Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Max')), categoryType='AR', title='serthgwer3444555', text='999888sdrhgserhtdfhre7776665444') --> Создаём пост
# post1 = Post.objects.get(pk=1) --> Получаем пост через primary key
# post2 = Post.objects.get(pk=2)
# post3 = Post.objects.get(pk=3)
# cat1 = Category.objects.get(name='Python') --> Получаем категорию через name
# cat2 = Category.objects.get(name='Django')
# post1.postCategory.add(cat1) --> Добавляем связи
# post1.postCategory.add(cat1, cat2) --> Добавляем связи. Т.к. many to many можно связывать несколько
# post1.postCategory.add(cat2)
# Comment.objects.create(commentUser=User.objects.get(username='Den'), commentPost=Post.objects.get(pk=1), text='comment text1') --> Создаем комментарий
# Comment.objects.create(commentUser=User.objects.get(username='Den'), commentPost=Post.objects.get(pk=2), text='srtlhjwr;lhkjwr;hjwr;lhj;j')
# Comment.objects.create(commentUser=User.objects.get(username='Max'), commentPost=Post.objects.get(pk=3), text='1111111111111')
# Post.objects.get(pk=1).like() --> Ставим лайки постам
# Post.objects.get(pk=2).like()
# Post.objects.get(pk=3).dislike() --> Ставим дизлайки
# Comment.objects.get(pk=1).like() --> Ставим лайки комментам
# Comment.objects.get(pk=2).dislike() --> Ставим дизлайки комментам
# Author.objects.get(authorUser=User.objects.get(username='Den')). update_rating() --> Обновляем рейтинг Den
# Author.objects.get(authorUser=User.objects.get(username='Max')). update_rating() --> Обновляем рейтинг Max
# a = Author.objects.get(authorUser=User.objects.get(username='Den'))
# a.ratingAuthor --> смотрим обновленный рейтинг
# best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor')[0] --> username автора, рейтинг. Индекс первого объекта. [0:5] Весь рейтинг до 5 индекса
# print(best)
# d = User.objects.all().order_by('id').values('username', 'date_joined')[0:5] --> даты добавления, username 
# print(d)
# 

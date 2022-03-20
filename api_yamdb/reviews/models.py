from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    USERS_ROLE = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )
    password = models.CharField(
        verbose_name='password',
        max_length=128,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        blank=True,
        max_length=254,
    )
    confirmation_code = models.CharField(
        verbose_name='confirmation code',
        max_length=16,
        blank=True,
        null=True
    )
    role = models.CharField(
        verbose_name='users role',
        max_length=16,
        choices=USERS_ROLE,
        default=USER,
        blank=True,
        null=True
    )
    bio = models.TextField(
        verbose_name='biography',
        blank=True,
        null=True
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=150,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=150,
        verbose_name='last name'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('username', 'email',),
                name='unique_user'
            ),
        )
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='category name',
        db_index=True
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='genre name',
        db_index=True
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200, verbose_name='title')

    year = models.IntegerField(verbose_name='creation year')

    description = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='description'
    )

    genre = models.ManyToManyField(
        'Genre',
        through='GenreTitle',
        related_name='genre',
        verbose_name='genre'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='category',
        verbose_name='category'
    )

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    title = models.ForeignKey('Title', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.genre}'


class Review(models.Model):
    text = models.TextField()
    score = models.PositiveSmallIntegerField(validators=(
        MaxValueValidator(10),
        MinValueValidator(0), ))
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True, null=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_review'),
        )
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.text[:15]


class Comments(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True, null=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text[:15]

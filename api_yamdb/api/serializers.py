from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .validators import validate_year
from reviews.models import Category, Comment, Genre, Review, Title, User


class TokenSerializer(serializers.ModelSerializer):
    """Сериализатор для получения токена"""

    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class SignUpSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации"""

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" не разрешено.'
            )
        return value


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category"""

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre"""

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Title"""

    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    year = serializers.IntegerField(
        validators=[validate_year, ]
    )

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ('rating',)


class TitleSerializerReadOnly(serializers.ModelSerializer):
    """Сериализатор для модели Category для GET запроса"""

    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ('category', 'rating')


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Review"""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    score = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date',)
        model = Review

    def validate(self, data):
        request = self.context["request"]
        title_id = self.context["view"].kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        if request.method == "POST":
            if Review.objects.filter(
                    title=title, author=request.user
            ).exists():
                raise ValidationError(
                    "Можно оставить только один отзыв на произведение.")
        return data


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment"""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'pub_date')


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""

    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        max_length=150,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" не разрешено.'
            )
        return value

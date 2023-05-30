# Generated by Django 2.2.19 on 2023-05-27 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='following',
            field=models.ForeignKey(help_text='Выберите автора, на которого подписываются', on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='user',
            field=models.ForeignKey(help_text='Выберите пользователя, который подписывается', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(help_text='Выберите автора рецепта', on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(help_text='Выберите продукты рецепта', related_name='recipes', through='recipes.IngredientRecipe', to='recipes.Ingredient', verbose_name='Продукты в рецепте'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(help_text='Выберите тег рецепта', through='recipes.TagRecipe', to='recipes.Tag', verbose_name='Тег рецепта'),
        ),
        migrations.AddField(
            model_name='ingredientrecipe',
            name='ingredient',
            field=models.ForeignKey(help_text='Добавить продукты рецепта в корзину', on_delete=django.db.models.deletion.CASCADE, related_name='ingredientrecipes', to='recipes.Ingredient', verbose_name='Продукты рецепта'),
        ),
        migrations.AddField(
            model_name='ingredientrecipe',
            name='recipe',
            field=models.ForeignKey(help_text='Выберите рецепт', on_delete=django.db.models.deletion.CASCADE, related_name='ingredientrecipes', to='recipes.Recipe', verbose_name='Рецепт'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='recipe',
            field=models.ForeignKey(help_text='Выберите рецепт', on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='recipes.Recipe', verbose_name='Рецепт'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(help_text='Выберите пользователя', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='cart',
            name='recipe',
            field=models.ForeignKey(help_text='Выберите рецепты для добавления в корзины', on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='recipes.Recipe', verbose_name='Рецепты'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(help_text='Выберите пользователя', on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddConstraint(
            model_name='tagrecipe',
            constraint=models.UniqueConstraint(fields=('tag', 'recipe'), name='unique_tagrecipe'),
        ),
        migrations.AddConstraint(
            model_name='subscribe',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_subscribe'),
        ),
        migrations.AddConstraint(
            model_name='ingredientrecipe',
            constraint=models.UniqueConstraint(fields=('ingredient', 'recipe'), name='unique_ingredientrecipe'),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_favorite'),
        ),
        migrations.AddConstraint(
            model_name='cart',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_cart'),
        ),
    ]

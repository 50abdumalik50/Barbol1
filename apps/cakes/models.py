from django.db import models
import os
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from utils.image_path import upload_products
from mptt.models import MPTTModel, TreeForeignKey


class Cakes(MPTTModel):
    title = models.CharField(
        max_length=50,
        verbose_name="Название",
    )
    description = RichTextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True,
        verbose_name="Картинка",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание",
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
        verbose_name="Наследование"
    )

    def __str__(self):
        return self.title





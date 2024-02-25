from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='courses/', verbose_name='изображение', **NULLABLE)
    descrition = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lessons/', verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Quantity(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    quantity = models.IntegerField(verbose_name='количество')


    def __str__(self):
        return f'{self.course} - {self.quantity}'

    class Meta:
        verbose_name = 'количество'
        verbose_name_plural = 'количество'
        ordering = ('-quantity',)





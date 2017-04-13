from django.db import models
from django.utils import timezone


class Marca(models.Model):
    """
    Representa o fabricante de uma viatura
    """
    nome = models.CharField(
        max_length=100,
        unique=True,
        help_text="Marca ou fabricante (ex.: Ford, GM, Volkswagen, ...)")

    def save(self, *args, **kwargs):
        self.nome = self.nome.capitalize()
        super(Marca, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ["nome"]


class Modelo(models.Model):
    """
    Representa o modelo de uma viatura
    """
    nome = models.CharField(
        max_length=100,
        unique=True,
        help_text="Modelo da viatura")

    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE,
        help_text="Marca da viatura")

    foto = models.ImageField(
        null=True,
        blank=True,
        help_text="Foto da viatura")

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True)

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em")

    def save(self, *args, **kwargs):
        self.nome = self.nome.capitalize()
        super(Modelo, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Modelos"
        ordering = ["nome"]
        get_latest_by = "updated_at"


class Viatura(models.Model):
    """
    Representa uma viatura específica
    """

    placa = models.CharField(
        max_length=8)

    prefixo = models.CharField(
        max_length=8)

    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.SET_NULL,
        null=True)

    STATUS = (
        ('d', 'Disponível'),
        ('b', 'Baixada'),
        ('m', 'Manutenção'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default='d',
        help_text="Situação da viatura")

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True)

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizada em")

    def get_absolute_url(self):
        """
        Returns the url access to a particular viatura instance
        """
        return reverse('viatura-detalhes', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.placa = self.placa.upper()
        super(Viatura, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.prefixo, self.modelo)

    class Meta:
        ordering = ["prefixo"]

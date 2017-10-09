#coding: utf-8    
from django.db import models


# Create your models here.

class DadosPessoais(models.Model):
	class Meta:
		verbose_name = 'Dados Pessoais'
		verbose_name_plural = 'Dados Pessoais'
	def __str__(self):
		return  '%s '% (self.name)

	name = models.CharField(max_length=50, verbose_name='Nome')
	adress = models.CharField(max_length=100, verbose_name='Endereço')
	city = models.CharField(max_length=50, verbose_name='Cidade')
	cep = models.CharField(max_length=50, verbose_name='Cep')
	phone = models.CharField(max_length=20, blank=True ,verbose_name='Telefone')
	mobile = models.CharField(max_length=20, blank=True ,verbose_name='Celular')

	about = models.TextField(max_length=255, verbose_name='Sobre')
	data_nascimento = models.CharField(max_length=255, default='01 de janeiro de 2000', verbose_name='Data Nascimento')
	email = models.EmailField(verbose_name='Email')

	conhecimentos = models.TextField(max_length=255, verbose_name='Conhecimentos')
	github = models.CharField(max_length=100, default='http://gitbut.com/SeuGit', verbose_name='GitHub')
	current_position = models.CharField(max_length=100, verbose_name='Cargo Atual')
	empresa = models.CharField(max_length=100, verbose_name='Empresa')


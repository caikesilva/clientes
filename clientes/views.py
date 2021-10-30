import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
import pandas as pd
from clientes.forms import UploadForm
from django.core.files.storage import default_storage
import os
from django.contrib import messages
from clientes.models import Cliente
import time


# Create your views here.
class UploadFileView(CreateView):

    template_name = 'clientes/upload_file.html'
    form_class = UploadForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    #Converte col nascimento in obj date
    '''def to_date(self, nascimento_col):
        data_nascimento = time.localtime(nascimento_col)
        return time.strftime('%Y-%m-%d', data_nascimento)
    '''

    #formata numeros da coluna em str em formato de data (Ano-Mes-Dia)
    def to_date(self, nascimento_col):
        if len(nascimento_col) < 8:
            day = nascimento_col[6:7]    
        year = nascimento_col[:4] 
        month = nascimento_col[4:6]
        day = nascimento_col[6:8]
        return f'{year}-{month}-{day}'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():
            file = form.cleaned_data.get("file")
            file_name = default_storage.save(file.name, file)
            file_excel = pd.read_excel(default_storage.open(file_name))
            
            for lines in range(len(file_excel)):
                cliente = Cliente()
                cliente.nome = file_excel['nome'][lines]
                cliente.sobrenome = file_excel['sobrenome'][lines]
                cliente.sexo = file_excel['sexo'][lines]
                cliente.altura = file_excel['altura'][lines]
                cliente.peso = file_excel['peso'][lines]
                cliente.nascimento = self.to_date(str(file_excel['nascimento'][lines]))
                cliente.bairro = file_excel['bairro'][lines]
                cliente.cidade = file_excel['cidade'][lines]
                cliente.estado = file_excel['estado'][lines]
                cliente.numero = file_excel['numero'][lines]
                cliente.save()     
            os.remove(f'{os.getcwd()}/{default_storage.url(file_name)}')
            messages.success(request, 'Importado com sucesso!')
            return redirect('clientes:upload_file')
        else:
            messages.success(request, 'Erro ao importar o arquivo!')
            return redirect('clientes:upload_file')

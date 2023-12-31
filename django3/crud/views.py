from django.shortcuts import render
from .models import Pessoa
from django.views.decorators.csrf import csrf_protect

def listagem(request):
    titulo = 'Serviços'
    pessoas = Pessoa.objects.all()
    return render(request, 'listagem.html', {'titulo':titulo, 'pessoas':pessoas})

def selecao(request, id):
    titulo = 'Serviços'
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'listagem.html', {'titulo':titulo, 'pessoas':[pessoa]})

@csrf_protect
def consulta(request):
    consulta = request.POST.get('consulta')
    campo = request.POST.get('campo')

    if campo == 'nome':
        pessoas = Pessoa.objects.filter(nome__contains=consulta)
    elif campo == 'servico':
        pessoas = Pessoa.objects.filter(servico__contains=consulta)
    elif campo == 'telefone':
        pessoas = Pessoa.objects.filter(telefone__contains=consulta)
    elif campo == 'salario':
        pessoas = Pessoa.objects.filter(salario__contains=consulta)

    titulo = 'Serviços'
    return render(request, 'listagem.html', {'titulo':titulo, 'pessoas':pessoas})

_campo = ''
def ordenacao(request, campo):
    titulo = 'Serviços'
    global _campo
    if campo == _campo:
        pessoas = Pessoa.objects.all().order_by(campo).reverse()
        _campo = ''
    else:
        pessoas = Pessoa.objects.all().order_by(campo)
        _campo = campo
    return render(request, 'listagem.html', {'titulo':titulo, 'pessoas':pessoas})

def insercao(request):
    titulo = 'Inserir Cadastro'
    return render(request, 'insercao.html', {'titulo': titulo})

@csrf_protect
def salvar_insercao(request):
    nome = request.POST.get('nome')
    servico = request.POST.get('servico')
    telefone = request.POST.get('telefone')
    salario = request.POST.get('salario')
    salario = salario.replace(',','.')

    objeto = Pessoa(
        nome=nome,
        servico=servico,
        telefone=telefone,
        salario=salario
    )
    objeto.save()

    titulo = 'Serviços'
    pessoas = Pessoa.objects.all()
    return render(request, 'listagem.html', {'titulo':titulo, 'pessoas':pessoas})

def edicao(request, id):
    titulo = 'Editar Cadastro'
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'edicao.html', {'titulo':titulo, 'pessoa':pessoa})

@csrf_protect
def salvar_edicao(request):
    id = request.POST.get('id')
    nome = request.POST.get('nome')
    servico = request.POST.get('servico')
    telefone = request.POST.get('telefone')
    salario = request.POST.get('salario')
    salario = salario.replace(',','.')

    Pessoa.objects.filter(id=id).update(
        nome=nome,
        servico=servico,
        telefone=telefone,
        salario=salario
    )
    titulo = 'Serviços'
    pessoas = Pessoa.objects.all()
    return render(request, 'listagem.html', {'titulo':titulo, 'pessoas':pessoas})

def delecao(request, id):
    titulo = 'Deletar Cadastro'
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'delecao.html', {'titulo':titulo, 'pessoa':pessoa})

@csrf_protect
def salvar_delecao(request):
    id = request.POST.get('id')

    Pessoa.objects.filter(id=id).delete()

    titulo = 'Serviços'
    pessoas = Pessoa.objects.all()
    return render(request, 'listagem.html', {'titulo':titulo, 'pessoas':pessoas})

def graficos(request):
    titulo = 'Informações'
    pessoasPedreiro = Pessoa.objects.filter(servico='pedreiro')
    pessoasPintor = Pessoa.objects.filter(servico='pintor')
    pessoasProfessor = Pessoa.objects.filter(servico='professor')

    salarioPedreiro = 0
    for pe in pessoasPedreiro:
        salarioPedreiro += pe.salario
    if len(pessoasPedreiro) > 0:
        salarioPedreiro = salarioPedreiro / len(pessoasPedreiro)

    salarioPintor = 0
    for pi in pessoasPintor:
        salarioPintor += pi.salario
    if len(pessoasPintor) > 0:
        salarioPintor = salarioPintor / len(pessoasPintor)

    salarioProfessor = 0
    for pr in pessoasProfessor:
        salarioProfessor += pr.salario
    if len(pessoasProfessor) > 0:
        salarioProfessor = salarioProfessor / len(pessoasProfessor)

    return render(request, 'graficos.html', {'titulo': titulo, 'salarioPedreiro': salarioPedreiro, 'salarioPintor': salarioPintor, 'salarioProfessor': salarioProfessor})

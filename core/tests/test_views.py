from django.test import TestCase
from django.test import Client  # criar um navegador para exexutar os metodos, sem abrir o navegador
from django.urls import reverse_lazy  # para redirecionar


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Diego Evans',
            'email': 'diego@diego.com',
            'assunto': 'Um assunto qualquer',
            'mensagem': 'Uma mensagem de exemplo para realizar os testes'
        }
        self.cliente = Client()  # para testar post, get etc

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)  # assim verifica se eh valido ou nao
        self.assertEquals(request.status_code, 302)  # redirect eh o codigo 302, ele redireciona e confirma

    def test_form_invalid(self):
        dados = {
            'nome': 'Diego Evans',
            'assunto': 'Um assunto qualquer',
        }  # passando errado porque precisa ter todos os campos e nesta forma fica invalido
        request = self.cliente.post(reverse_lazy('index'), data=dados)  # assim verifica se eh valido ou nao
        self.assertEquals(request.status_code, 200)  # redirect eh o codigo 302, ele redireciona e confirm

from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Diego Evans'
        self.email = 'diego@diego.com'
        self.assunto = 'Um assunto qualquer'
        self.mensagem = 'Uma mensagem de exemplo para realizar os testes'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem,
        }

        self.form = ContatoForm(data=self.dados)  # mesmo coisa que contato request.POST, dados recebidos, via post

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res, res2)  # verificando se os dois tem os mesmo retorno pelo send mail

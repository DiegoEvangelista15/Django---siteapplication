from django.views.generic import FormView
from .models import Servico, Funcionario
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')  # para depois que mandar enviar para a pagina citada

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)  # recuperar o contexto da classe
        context['servicos'] = Servico.objects.order_by('?').all()  # usando isso, podemos embaralhar os dados
        context['funcionarios'] = Funcionario.objects.all()  # Buscando a infos do DBs
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso!!!')

        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar email')

        return super(IndexView, self).form_invalid(form, *args, **kwargs)

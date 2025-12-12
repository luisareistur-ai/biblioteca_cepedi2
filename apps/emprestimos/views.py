from django.contrib import messages
from django.shortcuts import redirect, render

from apps.emprestimos.forms import EmprestimoForm


def inserir_emprestimo(request):
    template_name = 'emprestimos/form_emprestimo.html'
    if request.method == 'POST':
        form = EmprestimoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro de empréstimo foi realizado com sucesso!')
        # return redirect('emprestimos:listar_emprestimos')
    form = EmprestimoForm()
    context = {'form': form}
    return render(request, template_name, context)
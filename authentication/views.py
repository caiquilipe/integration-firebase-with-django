
from django.shortcuts import render
from django.conf import settings

import pyrebase


def connection_firebase():
    """
        Responsável pela conexão com firebase
    """
    config = settings.CONFIG_FIREBASE
    firebase = pyrebase.initialize_app(config)
    return firebase

def connection_database(firebase):
    """
        Responsável pela conexão com banco de dados
    """
    return firebase.database()

def index(request):
    """
        Página inicial
    """
    message = None

    firebase = connection_firebase()
    if request.POST:
        auth = firebase.auth()
        try:
            user = auth.sign_in_with_email_and_password(request.POST.get('email'), request.POST.get('password'))
            session_id = user.get('idToken')
            request.session['uid'] = session_id
            print(auth.get_account_info(session_id))
            return render(request, 'logged.html')
        except:
            message = 'Inválid credentials'
    return render(request, 'index.html', {'message': message})

def logged(request):
    """
        Visualiza somente se estiver logado
    """
    response = render(request, 'logged.html')
    if not request.session.get('uid'):
        response = render(request, 'index.html')
    return response

def logout(request):
    """
        Responsável pela desconexão com firebase
    """
    del request.session['uid']
    return render(request, 'index.html')

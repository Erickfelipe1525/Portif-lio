const loginForm = document.getElementById('loginForm');
const googleBtn = document.getElementById('googleLogin');
const mensagem = document.getElementById('mensagem');

const usuarios = {
    'usuario1': 'senha123',
    'usuario2': 'senha456',
    'usuario3': 'senha789'
};

// Evento de login
loginForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const login = document.getElementById('login').value;
    const senha = document.getElementById('senha').value;

    if (usuarios[login] === senha) {
        mensagem.style.color = "green";
        mensagem.textContent = "Redirecionando...";
        setTimeout(function() {
            window.location.href = "segundaPagina.html"; // coloque sua página
        }, 2000);
    } else {
        mensagem.style.color = "red";
        mensagem.textContent = "Login ou senha incorretos, tente novamente.";
        setTimeout(function() {
            document.getElementById('login').value = '';
            document.getElementById('senha').value = '';
            mensagem.textContent = '';
        }, 5000);
    }
});

// Evento do botão Google
googleBtn.addEventListener('click', function() {
    mensagem.style.color = "blue";
    mensagem.textContent = "Simulação de login com Google clicada!";
});

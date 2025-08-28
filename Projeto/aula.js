
document.addEventListener('DOMContentLoaded', () => {

    const logoutBtn = document.getElementById("logoutBtn");
    const botoesCurso = document.querySelectorAll('.acessar-curso-btn');
    
    // Objeto para armazenar as descrições dos cursos
    const mensagens = {
        "HTML & CSS": "O curso de HTML e CSS vai te ensinar a como estruturar e estilizar sites profissionais.",
        "JavaScript": "O curso de JavaScript vai te ensinar a criar páginas dinâmicas e interativas.",
        "Python": "O curso de Python é perfeito para quem quer começar em programação e análise de dados.",
        "SQL & Banco de Dados": "O curso de Banco de Dados vai te ensinar a armazenar e gerenciar informações de forma eficiente."
    };

    // Função assíncrona para carregar o conteúdo do curso
    async function carregarCurso(cursoNome) {
        // Encontra o card pai e os elementos loader e detalhes
        const card = Array.from(botoesCurso).find(btn => btn.textContent.trim().includes(cursoNome)).parentElement;
        const loader = card.querySelector(".loader");
        const detalhes = card.querySelector(".detalhes");

        // Mostra o loader
        loader.style.display = "block";
        detalhes.style.display = "none";

        // Simula um tempo de espera (2 segundos)
        await new Promise(resolve => setTimeout(resolve, 2000));

        // Esconde o loader e mostra os detalhes
        loader.style.display = "none";
        detalhes.style.display = "block";

        // Atualiza o conteúdo HTML com a mensagem do curso
        detalhes.innerHTML = mensagens[cursoNome];
    }
    
    // Adiciona um evento de clique a cada botão
    botoesCurso.forEach(btn => {
        btn.addEventListener('click', () => {
            // Pega o título do curso que está no <h2> do card
            const cursoNome = btn.parentElement.querySelector('h2').textContent.trim();
            carregarCurso(cursoNome);
        });
    });

    // Lógica para o botão de Sair
    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            location.href = "aulapratica.html";
        });
    }

});
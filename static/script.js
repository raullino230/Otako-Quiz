console.log("JS carregado com sucesso!");

// Função atualizada
function verificarResposta(questao, respostaCorreta) {
  let respostaUsuario = "";

  // Caso 1: questão de múltipla escolha (checkbox)
  const checkboxes = document.querySelectorAll(`input[name^="${questao}"]:checked`);
  if (checkboxes.length > 0) {
    respostaUsuario = checkboxes[0].value; // Pega o valor da alternativa marcada
  }

  // Caso 2: questão de texto (input[type=text])
  const campoTexto = document.querySelector(`input[name="${questao}"]`);
  if (campoTexto && campoTexto.type === "text") {
    respostaUsuario = campoTexto.value.trim();
  }

  // Envia a resposta pro backend
  fetch('/verificar', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ questao, resposta: respostaUsuario })
  })
  .then(response => response.json())
  .then(data => {
    alert(data.mensagem);
  })
  .catch(error => {
    console.error('Erro:', error);
    alert('Erro ao verificar a resposta. Tente novamente.');
  });
}

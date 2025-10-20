console.log("JS carregado com sucesso!");

function verificarResposta(questao, resposta) {
  fetch('/verificar', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ questao, resposta })
  })
  .then(response => {
    if (!response.ok) throw new Error('Erro na resposta do servidor');
    return response.json();
  })
  .then(data => {
    alert(data.mensagem);
  })
  .catch(error => {
    console.error('Erro:', error);
    alert('Erro ao verificar a resposta. Tente novamente.');
  });
}

 <script>
function verificarResposta(questao, resposta) {
  fetch('http://127.0.0.1:5000/site.html/verificar', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ questao: questao, resposta: resposta })
  })
  .then(response => response.json())
  .then(data => {
    alert(data.mensagem);
  });
}
 </script>
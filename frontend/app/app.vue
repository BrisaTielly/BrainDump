<script setup>
  const { data: boards, error, status } = await useFetch('http://127.0.0.1:8000/boards/')
</script>

<template>
  <div style="font-family: sans-serif; padding: 20px;">
    <h1>🧠BrainDump</h1>

    <div v-if="status === 'pending'">
      <p>Carregando dados do servidor...</p>
    </div>

    <div v-else-if="error" style="color: red; border: 1px solid red; padding: 10px;">
      <h3>Vixe, deu erro!</h3>
      <p>{{ error }}</p>
      <small>Dica: Verifique se o Django está rodando na porta 8000 e se instalou o django-cors-headers.</small>
    </div>

    <div v-else>
      <h2>Meus Quadros:</h2>
      <ul>
        <li v-for="board in boards" :key="board.id">
          <strong>{{ board.title }}</strong> (ID: {{ board.id }})
        </li>
      </ul>
      
      <hr>
      <pre style="background: #f4f4f4; padding: 10px;">{{ boards }}</pre>
    </div>
  </div>
</template>
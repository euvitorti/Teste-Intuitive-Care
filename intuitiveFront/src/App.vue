<script setup>
import { ref } from 'vue'

const termo = ref('')
const resultados = ref([])
const erro = ref(null)

const buscarOperadoras = async () => {
  erro.value = null
  resultados.value = []

  try {
    const response = await fetch(`http://127.0.0.1:8000/operadoras/?termo=${termo.value}`)

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.detail)
    }

    resultados.value = data.resultados
  } catch (err) {
    erro.value = err.message
  }
}
</script>

<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <div class="search-box">
      <input v-model="termo" placeholder="Digite um termo" class="search-input" />
      <button @click="buscarOperadoras" class="search-button">Buscar</button>
    </div>

    <div v-if="erro" class="error">{{ erro }}</div>

    <div v-if="resultados.length" class="result-list">
      <div v-for="operadora in resultados" :key="operadora.razao_social" class="card">
        <h2>{{ operadora.razao_social }}</h2>
        <p><strong>Modalidade:</strong> {{ operadora.modalidade }} ({{ operadora.uf }})</p>
        <p><strong>Telefone:</strong> {{ operadora.telefone }}</p>
        <p><strong>Representante:</strong> {{ operadora.representante }} ({{ operadora.cargo_representante }})</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #1e1e1e;
  color: white;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(255, 255, 255, 0.1);
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.search-box {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

.search-input {
  flex: 1;
  padding: 12px;
  font-size: 16px;
  border: 1px solid #444;
  border-radius: 8px;
  outline: none;
  background: #333;
  color: white;
}

.search-input:focus {
  border-color: #00bfff;
}

.search-button {
  padding: 12px 20px;
  font-size: 16px;
  border: none;
  background: #00bfff;
  color: white;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s;
}

.search-button:hover {
  background: #009acd;
}

.error {
  color: red;
  text-align: center;
  margin-bottom: 20px;
}

.result-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.card {
  padding: 20px;
  border-radius: 8px;
  background: #292929;
  box-shadow: 0 2px 5px rgba(255, 255, 255, 0.1);
  transition: transform 0.2s;
}

.card:hover {
  transform: scale(1.02);
}

.card h2 {
  margin: 0 0 10px;
  font-size: 22px;
  color: #00bfff;
}

.card p {
  margin: 5px 0;
  color: #ccc;
}
</style>

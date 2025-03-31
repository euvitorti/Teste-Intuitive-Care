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

    if (!response.ok) {
      throw new Error('Nenhuma operadora encontrada')
    }

    const data = await response.json()
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
      <input
        v-model="termo"
        placeholder="Digite um termo"
        class="search-input"
      />
      <button @click="buscarOperadoras" class="search-button">Buscar</button>
    </div>

    <div v-if="erro" class="error">{{ erro }}</div>

    <div v-if="resultados.length" class="result-list">
      <div
        v-for="operadora in resultados"
        :key="operadora.cnpj"
        class="card"
      >
        <h2>{{ operadora.razao_social }}</h2>
        <p>
          <strong>Modalidade:</strong> {{ operadora.modalidade }} ({{ operadora.uf }})
        </p>
        <p>
          <strong>Telefone:</strong> {{ operadora.telefone }}
        </p>
        <p>
          <strong>Representante:</strong>
          {{ operadora.representante }} ({{ operadora.cargo_representante }})
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  color: white;
}

.search-box {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.search-input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px 0 0 4px;
  outline: none;
}

.search-input:focus {
  border-color: #007bff;
}

.search-button {
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  background-color: #007bff;
  color: #fff;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
  transition: background-color 0.3s;
}

.search-button:hover {
  background-color: #0056b3;
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
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.card h2 {
  margin: 0 0 10px;
  font-size: 20px;
  color: #333;
}

.card p {
  margin: 5px 0;
  color: #555;
}
</style>

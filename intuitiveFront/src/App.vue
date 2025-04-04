<script setup>
import { ref } from 'vue'

const termo = ref('')
const resultados = ref([])
const erro = ref(null)

const buscarOperadoras = async () => {
  erro.value = null
  resultados.value = []

  try {
    const response = await fetch(`https://intuitive-api-vitor-kvo5dr02d-euvitortis-projects.vercel.app/operadoras/?termo=${termo.value}`)

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
      <div v-for="operadora in resultados" :key="operadora.cnpj" class="card">
        <h2>{{ operadora.razao_social }} ({{ operadora.nome_fantasia }})</h2>
        <p><strong>CNPJ:</strong> {{ operadora.cnpj }}</p>
        <p><strong>Modalidade:</strong> {{ operadora.modalidade }}</p>
        <p><strong>Localização:</strong> {{ operadora.cidade }} - {{ operadora.uf }}</p>
        <p><strong>Telefone:</strong> {{ operadora.telefone }}</p>
        <p><strong>E-mail/Site:</strong> {{ operadora.endereco_eletronico || 'Não informado' }}</p>
        <p><strong>Registro ANS desde:</strong> {{ operadora.data_registro_ans }}</p>
      </div>
    </div>
  </div>
</template>

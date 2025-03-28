<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Busca de Operadoras de Saúde</h1>
    
    <input 
      v-model="searchQuery" 
      @input="performSearch"
      placeholder="Digite nome ou registro da operadora"
      class="w-full p-2 border rounded mb-4"
    />

    <div v-if="loading" class="flex justify-center items-center">
      <div class="loader"></div>
    </div>

    <table v-else-if="results.length" class="w-full border-collapse">
      <thead>
        <tr class="bg-gray-200">
          <th class="border p-2">Registro</th>
          <th class="border p-2">Nome</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="operator in results" :key="operator.REGISTRO" class="hover:bg-gray-100">
          <td class="border p-2">{{ operator.REGISTRO }}</td>
          <td class="border p-2">{{ operator.NOME }}</td>
        </tr>
      </tbody>
    </table>

    <p v-else-if="searchQuery && !results.length">Nenhum resultado encontrado.</p>
  </div>
</template>

<script>
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000'
})

export default {
  name: 'HealthOperatorSearch',
  data() {
    return {
      searchQuery: '',
      results: [],
      loading: false
    }
  },
  methods: {
    async performSearch() {
      if (!this.searchQuery.trim() || this.searchQuery.length < 2) {
        this.results = []
        return
      }

      this.loading = true
      try {
        console.log('Enviando requisição para a API com query:', this.searchQuery)
        const response = await api.get('/search', {
          params: { query: this.searchQuery }
        })
        console.log('Resposta da API:', response.data)
        this.results = Array.isArray(response.data) ? response.data : []
      } catch (error) {
        console.error('Erro na busca:', error)
        this.results = []
        alert('Ocorreu um erro ao buscar os dados. Tente novamente mais tarde.')
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style>
.loader {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
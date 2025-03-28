<template>
  <div id="app" class="container mx-auto p-4">
    <HealthOperatorSearch />
  </div>
</template>

<script>
import HealthOperatorSearch from './components/HealthOperatorSearch.vue'

export default {
  name: 'App',
  components: {
    HealthOperatorSearch
  }
}
</script>
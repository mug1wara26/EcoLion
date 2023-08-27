<template>
  <v-container fluid>
    Overview page
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'

  export default Vue.extend({
    name: 'Overview',

    data: () => ({
    }),
    created() {
      this.$root.$emit('show-tabs')
    }
  })
</script>

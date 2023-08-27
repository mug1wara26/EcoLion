<template>
  <v-container fluid>
    You have not joined or created any organizations
  </v-container>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  name: "Events",
  created() {
    this.$root.$emit('show-tabs')
  }
})
</script>
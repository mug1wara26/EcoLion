<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="5">
        <v-card outlined style="border: 2px solid black; background-color: #98F47C">
          <v-card-title>
            Title
          </v-card-title>
          <v-card-subtitle>
            Request/Offer
          </v-card-subtitle>
          <v-card-text>
            Description
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
  import Vue from 'vue'

  export default Vue.extend({
    name: 'Recycle',

    data: () => ({
    }),
    created() {
      this.$root.$emit('show-tabs')
    }
  })
</script>

<template>
  <v-app style="background-color: #98F47C">
    <div>
      <v-toolbar
          flat color="primary"
      >
        <v-toolbar-title
            style="cursor: pointer; color: white"
            @click="$router.push('/overview')"
        >
          SG EcoLion
        </v-toolbar-title>

        <v-spacer/>

        <template v-slot:extension v-if="show_tabs">
          <v-tabs
              v-model="tab"
              background-color="primary"
              :optional="true"
          >
            <v-tabs-slider color="yellow"></v-tabs-slider>

            <v-tab
                v-for="item in items"
                :key="item"
                :to="item.toLowerCase()"
            >
              {{ item }}
            </v-tab>
          </v-tabs>
        </template>
      </v-toolbar>
    </div>
    <v-main style="background-color: #98F47C">
      <v-container fluid :key="reRender">
        <router-view :key="$route.fullPath"/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import {getCookie} from "typescript-cookie";

Vue.prototype.apiLink = "http://127.0.0.1:8000"

export default Vue.extend({
  name: 'App',
  data() {
    return {
      tab: 'overview',
      items: ['overview', 'Organizations', 'Events', 'Recycling'],
      show_tabs: true,
      reRender: 0,
    }
  },
  created() {
    this.$root.$on('show-tabs', () => {
      this.show_tabs = true
    })
    this.$root.$on('hide-tabs', () => {
      this.show_tabs = false
    })
    this.$root.$on('re-render', () => {
      this.reRender++
    })
  }
});
</script>

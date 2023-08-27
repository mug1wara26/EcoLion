<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="4" class="mx-auto">
        <v-row align="center">
          <v-col cols="11">
            <v-container class="d-flex justify-center">
              <v-icon>mdi-magnify</v-icon>
              <v-text-field
                  autofocus
                  v-model="search"
                  label="Search"
                  class="ml-2"
              />
            </v-container>
          </v-col>
          <v-col cols="1">
            <v-btn icon to="/create_organization">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-col>
        </v-row>

        <v-card
            outlined
            style="border: 2px solid black; background-color: #98F47C"
            v-for="org in orgs"
            :key="org.id"
        >
          <v-card-title>
            <a :href='`/organizations/${org.id}/`'>{{org.name}}</a>
          </v-card-title>
          <v-card-subtitle>
            {{org.description}}
          </v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import {Org} from "@/schema/types";
import {getOrgs} from "@/api/organizationApi";

export default Vue.extend({
  name: "Organizations",
  data() {
    return {
      search: '',
      orgs: [] as Array<Org>
    }
  },
  created() {
    this.$root.$emit('show-tabs')

    getOrgs().then(data => {
      this.orgs = data
      console.log(JSON.stringify(data))
    })
  }
})
</script>
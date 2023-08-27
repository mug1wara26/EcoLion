<template>
  <v-container fluid style="background-color: #98F47C">
    <v-progress-circular v-if="!loaded" indeterminate class="d-flex justify-center mx-auto"/>
    <v-row justify="center" v-else>
      <v-col cols="5">
        <v-alert type="error" v-if="error">
          There was an error creating the organization
        </v-alert>

        <h1>Create a new organization</h1>
        <v-text-field v-model="org_name" autofocus label="Organization name*"/>
        <v-textarea v-model="desc" counter maxlength="200" label="Description*"/>
        <v-text-field v-model="img_url" autofocus label="Image URL*"/>

        <v-row class="mb-2 align-center d-flex">
          Location*: {{ center.lat ? `${center.lat}, ${center.lng}` : 'Drag around the map' }}
          <v-btn color="error" class="ml-auto" @click="cancelLocation">
            Cancel
          </v-btn>
        </v-row>
        <iframe
            id="leaflet"
            src="leaflet.html"
            frameborder="0"
            width="100%"
            height="100%"
        />
        <v-row class="d-flex justify-end mt-2">
          <v-btn color="primary" @click="createOrganization">Create</v-btn>
        </v-row>
      </v-col>
    </v-row>

  </v-container>
</template>

<script lang="ts">
import Vue from "vue"
import {createOrg} from "@/api/organizationApi";
import {BasicOrg} from "@/schema/types";

export default Vue.extend({
  name: "CreateCommunity",
  data() {
    return {
      center: {lat: NaN, lng: NaN},
      org_name: '',
      desc: '',
      loaded: true,
      error: false,
      img_url: ''
    }
  },
  methods: {
    cancelLocation() {
      this.center = {lat: NaN, lng: NaN}
    },
    createOrganization() {
      this.loaded = false
      const basicOrg: BasicOrg = {
        name: this.org_name,
        desc: this.desc,
        lat: this.center.lat,
        lng: this.center.lng,
        img_url: this.img_url
      }
       createOrg(basicOrg).then(org_id => {
         this.$router.push(`/organizations/${org_id}`)
       }).catch(() => {
         this.error=true
         setTimeout(() => {
           this.error=false
         }, 3000)
       }).finally(() => this.loaded=true)
    }
  },
  created() {
    this.$root.$emit('hide-tabs')
    window.addEventListener('message', (data) => {
      if (data.data.center) {
        this.center = data.data.center
      }
    })
  },
})

</script>
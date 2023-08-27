<template>
  <v-container fluid>
    <v-row justify="center" class="fill-height">
      <v-col cols="6">
        <h1>Carpool for {{name[0].toUpperCase() + name.substring(1)}}</h1>
        <h2>{{joined ? 'You have joined this carpool slot' : 'You have not joined this carpool slot'}}</h2>
        <v-btn v-if="!joined" color="primary" @click="onJoin"> Join </v-btn>
        <p v-if="joined">Your carpool marker is in green</p>

        <iframe
            class="mb-16"
            id="leaflet"
            src="/leaflet.html"
            frameborder="0"
            width="100%"
            height="100%"
            v-on:load="onLoadIFrame"
        />

        <div class="mt-16" style="color: #98F47C">|</div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import {getCarpoolUsers} from "@/api/carpoolApi";
import {getUser} from "@/api/userApi";

export default Vue.extend({
  name: "Carpool",
  data () {
    return {
      name: '',
      joined: false,
    }
  },
  methods: {
    onJoin() {
      this.joined = true
    },
    onLoadIFrame() {
      getCarpoolUsers().then(data => {
          getUser().then(user=> {
            const iframe = document.querySelector("iframe");
            if (iframe != null && iframe.contentWindow != null) {
              iframe.contentWindow.postMessage({
                'event': 'sendData', 'data': data, 'user': user
              }, '*')
            }
          })
      })
    }
  },
  created() {
    this.$root.$emit('hide-tabs')
    this.name = this.$route.query.carpool.toString()


    this.joined = Boolean(this.$route.query.join)


  }
})
</script>
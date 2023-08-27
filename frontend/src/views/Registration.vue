<template>
  <v-container fluid>
    <v-progress-circular v-if="!loaded" indeterminate class="d-flex justify-center mx-auto"/>
    <v-row justify="center" class="d-flex" v-else>
      <v-col cols="4">
        <v-alert type="error" v-if="error">
          There was an error registering, please try again later.
        </v-alert>

        <v-text-field v-if="!login" v-model="user.username" label="Username*"/>
        <v-text-field v-model="user.email" label="Email*"/>
        <v-text-field
            v-model="user.password"
            label="Password*"
            :type="showPass ? '' : 'password'"
            :append-icon="showPass? 'mdi-eye-off-outline' : 'mdi-eye-outline'"
            @click:append="showPass = !showPass"
        />
        <v-text-field v-model="user.number" label="Contact Number (+65)*"/>


        <v-row class="mb-2 align-center d-flex">
          Location*: {{ user.lat ? `${user.lat}, ${user.lng}` : 'Drag around the map' }}
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
        <v-row justify="end" class="mt-2">
          <v-btn color="blue" :disabled="unclean" @click="onRegister">{{ login ? 'Login' : 'Register'}}</v-btn>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import {register} from "@/api/userApi";
import {BasicUser} from "@/schema/types";
import {setCookie} from "typescript-cookie";
export default Vue.extend({
  name: "Registration",
  data() {
    return {
      login: false,
      user: {
        username: '',
        email: '',
        password: '',
        number: undefined,
        lat: NaN,
        lng: NaN,
        car_capacity: 0,
      },
      showPass: false,
      loaded: true,
      error: false
    }
  },
  computed: {
    unclean(): boolean {
      return Object.values(this.user).every((val: any) => val === '' || val === null || isNaN(val))
    }
  },
  methods: {
    cancelLocation() {
      this.user.lat = NaN
      this.user.lng = NaN
    },
    onRegister() {
      this.loaded = false
      const basicUser: BasicUser = this.user
      register(basicUser).then(res => {
        if (res.status === 200) {
          res.json().then(data => {
            setCookie('token', data.token, {sameSite: "lax"});
            this.loaded=true

            this.$router.push('/overview')
          })
        }
        else {
          this.error = true
          this.loaded = true
          setTimeout(() => {
            this.error = false
          }, 3000)
        }
      })
    }
  },
  created() {
    window.addEventListener('message', (data) => {
      if (data.data.center) {
        this.user.lat = Math.round(data.data.center.lat * 10000)/10000
        this.user.lng = Math.round(data.data.center.lng * 10000)/10000
      }
    })
  }
})
</script>
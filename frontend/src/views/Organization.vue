<template>
  <v-container>
    <v-row>
      <v-col cols="4" class="ma-0 pa-0">
        <v-card color="secondary">
          <v-img
              :src="org.img_url"
              height="200px"
          />
          <v-card-title>
            {{org.name}}
          </v-card-title>
          <v-card-subtitle>
            Members
          </v-card-subtitle>
          <v-card-text>
            Get member list from backend api along with roles
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="8" class="ma-0 pa-0">
        <v-card color="secondary">
          <div style="height: 200px">
            <v-card-title>
              {{org.name}}
            </v-card-title>
            <v-card-subtitle>
              {{org.description}}
            </v-card-subtitle>
          </div>
          <v-divider/>
          <v-card-text>
            <b>Carpool timeslots</b>

            <v-card color="#67dfa2" class="pa-0 mt-4">
              <v-row class="ma-0" align="center">
                <v-col cols="9">
                  <v-card-title> Arrival </v-card-title>
                  <v-card-subtitle>7:30am</v-card-subtitle>
                </v-col>
                <v-col cols="3" class="d-flex justify-end">
                  <v-btn color="primary" @click="onJoin('arrival')">
                    Join
                  </v-btn>
                </v-col>
              </v-row>
            </v-card>

            <v-card color="#78cdc0" class="pa-0 mt-4">
              <v-row class="ma-0" align="center">
                <v-col cols="9">
                  <v-card-title> Leaving </v-card-title>
                  <v-card-subtitle>5:00pm</v-card-subtitle>
                </v-col>
                <v-col cols="3" class="d-flex justify-end">
                  <v-btn color="primary" @click="onJoin('leaving')">
                    Join
                  </v-btn>
                </v-col>
              </v-row>
            </v-card>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import {getOrg} from "@/api/organizationApi";

export default Vue.extend({
  name: "Organization",
  data() {
    return {
      org_id: -1,
      org: {}
    }
  },
  methods: {
    onJoin(carpool_name: string) {
      this.$router.push(`/carpool/?join=true&carpool=${carpool_name}&id=${this.org_id}`)
    }
  },
  mounted() {
    this.$root.$emit('hide-tabs')
  },
  created() {
    this.org_id = Number.parseInt(this.$route.params.id)
    if (this.org_id !== -1) {
      getOrg(this.org_id).then(org => {
        this.org = org
      })
    }
  }
})
</script>
import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import CreateOrganization from "@/views/CreateOrganization.vue";
import Overview from "@/views/Overview.vue";
import Organizations from "@/views/Organizations.vue";
import Events from "@/views/Events.vue";
import Recycle from "@/views/Recycle.vue";
import Organization from "@/views/Organization.vue"
import Registration from "@/views/Registration.vue"
import {getCookie} from "typescript-cookie";
import Carpool from "@/views/Carpool.vue";

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: Overview
  },
  {
    path: '/overview',
    name: 'overview',
    component: Overview
  },
  {
    path: '/organizations',
    name: 'organizations',
    component: Organizations
  },
  {
    path: '/organizations/:id',
    name: 'organization',
    component: Organization
  },
  {
    path: '/carpool',
    name: 'carpool',
    component: Carpool,
  },
  {
    path: '/events',
    name: 'event',
    component: Events
  },
  {
    path: '/recycling',
    name: 'recycle',
    component: Recycle
  },
  {
    path: '/create_organization',
    name: 'create_organization',
    component: CreateOrganization
  },
  {
    path: '/register',
    name: 'register',
    component: Registration
  },
]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach(async (to, from, next) => {
  const token = getCookie('token') || ''

  if (to.path !== '/register') {
    if (token === '') next({ name: 'register' })
    else next()
  }
  else next()
})

export default router

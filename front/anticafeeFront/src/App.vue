<template>
  <router-view />
  <leftnav></leftnav>
</template>

<script>
  //import Leftnav from './components/Leftnav.vue'
  export default {
    name: 'App',
    data() {
      return {
        page: 1
      }
    },
    methods: {

    },
    // components: {
    //   Leftnav
    // }
  }
</script>

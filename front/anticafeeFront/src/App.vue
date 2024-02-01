<template>
  <router-view />
  <MainPage/>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        page: 1
      }
    },
    methods: {

    },
  }
</script>

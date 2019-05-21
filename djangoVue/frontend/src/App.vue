<template>
  <div id="app">
    <v-menu></v-menu>
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
import vMenu from './components/menu.vue';
export default {
  components: {vMenu},
  name: 'App'
}
</script>

<style>
</style>

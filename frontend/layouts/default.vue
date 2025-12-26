<template>
  <div id="app-layout">
    <AppSidebar />

    <main class="main-content">
    <AppTopbar />
      
      <nuxt /> 
      
    </main>
  </div>
</template>

<script>
import AppSidebar from '@/components/App/AppSidebar.vue'
import AppTopbar from '~/components/App/AppTopbar.vue';

export default {
  components: { AppSidebar }
}
</script>

<style>
/* Aqui vai aquele CSS de Grid (grid-template-columns) que fizemos */
#app-layout {
  display: grid;
  grid-template-columns: 240px 1fr;
  height: 100vh;
}
 #pro-app {
    display: grid;
    grid-template-columns: 240px 1fr; /* Sidebar fixa, resto fluido */
    height: 100vh;
    overflow: hidden;
  }

    .main-content {
    background-color: white;
    display: flex;
    flex-direction: column;
    overflow-y: auto; /* Scroll apenas aqui */
  }
</style>
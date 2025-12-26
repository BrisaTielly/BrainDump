<template>
  <div>
    <h1>Board {{ boardId }}</h1>
  </div>
</template>

<script>
export default {
  computed: {
    boardId() {
      return this.$route.params.id
    }
  }
}
</script>

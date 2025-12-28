<template>
  <div 
  ref="boardContainer"
  class="board-container"
  @mousemove="catchMouse"
  @click="catchClick">
    X: {{ x }} | Y: {{ y }}
      <h1>Board {{ boardId }}</h1>
  </div>
</template>

<script>
export default {
  data(){
    return {
      x: 0,
      y: 0
    }
  },
  computed: {
    boardId() {
      return this.$route.params.id
    }
  },
  methods: {
    catchMouse(event){
      this.x = event.clientX
      this.y = event.clientY
    },
    catchClick(){
      const dot = document.createElement('div')
      dot.className = 'dot'
      dot.style.top = this.y + 'px'
      dot.style.left = this.x + 'px'
      this.$refs.boardContainer.appendChild(dot)
    }
  }
}
</script>

<style>
.board-container {
  width: 100%;
  height: 100%;
}

.dot {
  background-color: var(--accent);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  position: absolute;
}
</style>

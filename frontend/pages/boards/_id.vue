<template>
  <div 
  ref="boardContainer"
  class="board-container"
  @mousemove="catchMouse"
  @mousedown="catchClick($event)">
    X: {{ x }} | Y: {{ y }}
      <h1>Board {{ boardId }}</h1>
    <div
    v-for="dot in dots"
    :key="dot.id"
    :style="{ left: dot.x + 'px', top: dot.y + 'px' }"
    @mousedown="handleMouseDown(dot, $event)"
    class="canvas-dot">

    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      x: 0,
      y: 0,
      dots: [],
      draggingDot: null
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
    catchClick(event){
      if(event.target.closest('.canvas-dot')) return
      this.dots.push({
        x: this.x,
        y: this.y,
        id: (this.dots.length) + 1
      })
      console.log(this.dots)
    },
    handleMouseDown(dot, event){
      console.log(event)
      console.log('Segurando:', dot.x, dot.y)
      this.draggingDot = dot
      document.addEventListener('mouseup', this.handleDocumentMouseUp)
    },
    handleDocumentMouseUp(){
      if(this.draggingDot){
        this.draggingDot.x = this.x
        this.draggingDot.y = this.y
        this.draggingDot = null
        document.removeEventListener('mouseup', this.handleDocumentMouseUp)
      }
    }
  }
}
</script>

<style>
.board-container {
  width: 100%;
  height: 100%;
}

.canvas-dot {
  background-color: var(--accent);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  position: absolute;
}
</style>

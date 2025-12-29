<template>
  <div 
  ref="boardContainer"
  class="board-container"
  @mousemove="catchMouse"
  @mousedown="catchClick($event)">
    X: {{ x }} | Y: {{ y }}
      <h1>Board {{ boardId }}</h1>

    <Block
    v-for="block in blocks"
    :key="block.id"
    :style="{ left: block.x + 'px', top: block.y + 'px' }"
    @mousedown.block="handleMouseDown(block, $event)">

    </Block>
  </div>
</template>

<script>
import Block from '~/components/Blocks/Block.vue';
export default {
  components: {
    Block
  },
  data(){
    return {
      x: 0,
      y: 0,
      blocks: [],
      draggingblock: null
    }
  },
  computed: {
    boardId() {
      return this.$route.params.id
    }
  },
  methods: {
    catchMouse(event){
      this.x = event.clientX - 260/2 //Trocar depois por valor dinâmico
      this.y = event.clientY
    },
    catchClick(event){
      if(event.target.closest('.block-card')) return
      this.blocks.push({
        x: this.x,
        y: this.y,
        id: (this.blocks.length) + 1
      })
      console.log('Clicou')
      console.log(this.blocks)

    },
    handleMouseDown(block, event){
      console.log(event)
      console.log('Segurando:', block.x, block.y)
      this.draggingblock = block
      document.addEventListener('mouseup', this.handleDocumentMouseUp)
    },
    handleDocumentMouseUp(){
      if(this.draggingblock){
        this.draggingblock.x = this.x
        this.draggingblock.y = this.y
        this.draggingblock = null
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
  background-color: #fafafa;
}
</style>

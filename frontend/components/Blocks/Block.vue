<template>
    <div class="block-card "
    @mousedown="$emit('mousedown', $event)">
        <p class="block-title">Ideia Central</p>
        <p class="block-text">BrainDump MVP: O objetivo é criar um espaço onde as listas se transformam em um quadro visual interativo.</p>
    </div>
  </template>
  
  <script>
    
  export default {
    name: 'Block',
    components: {
    }
  }
  </script>

  <style>
    .block-card{
        background-color: white;
        max-width: 260px;
        min-height: 150px;
        border-radius: 8px;
        border: 1px solid var(--border);
        box-shadow: var(--shadow-card);
        position: absolute;
        cursor: grab;
        user-select: none;
        transition: transform 0.12s ease-out;

    }
    .block-card:hover{
        border-color: var(--border-hover);
    }
    .block-title{
        background-color: var(--accent-fade);
        font-size: 13px;
        font-weight: 600;
        padding: 10px 12px;
        color: var(--accent);
    }
    .block-text{
        padding: 12px;
        color: var(--text-muted);
    }
  </style>
  
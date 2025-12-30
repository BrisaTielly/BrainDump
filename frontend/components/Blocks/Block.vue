<template>
    <div class="block-card "
    @mousedown="$emit('mousedown', $event)">
        <div class="block-title">
            <input 
            type="text"
            v-model="title"
            placeholder="Insira o Titulo"
            @mousedown.stop>
            <div class="block-title-menu">
                <span> </span>
                <span> </span>
                <span> </span>
            </div>
        </div>
        <input 
        type="textarea"
        class="block-text" 
        v-model="text"
        placeholder="Coloque sua ideia aqui!"
        @mousedown.stop
        autofocus>
    </div>
  </template>
  
  <script>
    
  export default {
    name: 'Block',
    data() {
        return {
       
        } 
    },
    props: {
        title: {type: String, default: ''},
        text: {type: String, default: ''}
    }
  }
  </script>

  <style>
    .block-card{
        background-color: white;
        max-width: 260px;
        min-height: 150px;
        min-width: 260px;
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
        display: flex;
        justify-content: space-between;
    }
    .block-title input {
        border: none;
        background: transparent;
        font-size: 13px;
        font-weight: 600;
        color: var(--accent);
        width: 100%;
        outline: none;
    }
     .block-title input::placeholder{
        color: var(--accent);
    }
    
    .block-text {
        border: none;
        background: transparent;
        width: 100%;
        padding: 12px;
        color: var(--text-muted);
        outline: none;
        resize: none;
        box-sizing: border-box;
}
    .block-title-menu {
        display: flex;
        flex-direction: column; 
        gap: 1px;
        justify-content: center;
    }
    .block-title-menu span{
        background-color: var(--accent);
        width: 3px;
        height: 3px;
        border-radius: 50%;
        
    }
  </style>
  
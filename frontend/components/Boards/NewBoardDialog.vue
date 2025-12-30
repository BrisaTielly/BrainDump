<template>
  <div class="modal-overlay">
    <div class="modal-box">
      
      <div class="modal-header">
        <span class="modal-title">Novo Fluxo</span>
        <button class="btn-close" @click="$emit('close')">×</button>
      </div>

      <div class="modal-body">
        
        <div class="form-group">
          <label class="label">Nome do Quadro</label>
          <input 
            type="text" 
            class="input" 
            placeholder="Ex: Planejamento Q4"
            autofocus
            v-model="newBoardTitle"
          >
        </div>

        <div class="form-group">
          <label class="label">Descrição</label>
          <textarea 
            class="input" 
            rows="3" 
            placeholder="Qual o objetivo desse fluxo?"
          ></textarea>
        </div>

        <div class="form-group">
            <label class="label">Visibilidade</label>
            <div class="radio-group-visual">
                <div class="radio-card selected">Privado</div>
                <div class="radio-card">Time</div>
            </div>
        </div>

      </div>

      <div class="modal-footer">
        <button class="btn btn-ghost" @click="$emit('close')">
          Cancelar
        </button>
        <button class="btn btn-primary" @click="submit">
          Criar Quadro
        </button>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'NewBoardModal',
  data() {
    return {
      newBoardTitle: ''
    }
  },
  methods: {
    submit(){
      this.$emit('create-board', this.newBoardTitle)
      this.newBoardTitle = ''
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0, 0, 0, 0.5); 
  z-index: 1000;
  display: flex; 
  align-items: center; 
  justify-content: center;
  pointer-events: auto;
}

.modal-box {
  background: white;
  width: 100%; 
  max-width: 440px;
  border-radius: 16px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  overflow: hidden;
}

.modal-header {
  padding: 16px 24px;
  border-bottom: 1px solid #e5e7eb;
  display: flex; 
  justify-content: space-between; 
  align-items: center;
}

.modal-title { 
  font-weight: 600; 
  font-size: 16px; 
  color: #111827; 
}

.btn-close {
  background: transparent; 
  border: none; 
  font-size: 20px; 
  color: #9ca3af; 
  cursor: pointer;
  line-height: 1;
  padding: 4px;
}
.btn-close:hover { 
  color: #111827; 
}

.modal-body {
  padding: 24px;
  display: flex; 
  flex-direction: column; 
  gap: 16px;
}

.modal-footer {
  padding: 16px 24px;
  background: #f9fafb;
  border-top: 1px solid #e5e7eb;
  display: flex;
   justify-content: flex-end; 
   gap: 12px;
}

.form-group { 
  display: flex; 
  flex-direction: column; 
  gap: 6px; }

.label { 
  font-size: 13px; 
  font-weight: 500; 
  color: #374151; }

.input {
  padding: 10px 12px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  font-family: inherit; 
  font-size: 14px; 
  color: #111827;
  outline: none; transition: all 0.2s;
}

.input:focus {
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px #eef2ff;
}

.btn {
  padding: 8px 16px; 
  border-radius: 8px;
  font-size: 14px; 
  font-weight: 500; 
  cursor: pointer;
  transition: all 0.2s; 
  border: 1px solid transparent;
}

.btn-ghost {
  background: white; 
  border-color: #e5e7eb; 
  color: #374151;
}
.btn-ghost:hover {
  background: #f3f4f6; 
  border-color: #d1d5db;
}

.btn-primary {
  background: #4f46e5; 
  color: white;
}
.btn-primary:hover {
  background: #4338ca;
  transform: translateY(-1px);
}

.radio-group-visual { 
  display: flex; 
  gap: 10px; }

.radio-card {
    border: 1px solid #e5e7eb; 
    padding: 8px 12px; 
    border-radius: 6px;
    font-size: 13px; 
    cursor: pointer; 
    color: #6b7280;
}
.radio-card.selected {
    background: #eef2ff; 
    border-color: #4f46e5; 
    color: #4f46e5; 
    font-weight: 600;
}
</style>
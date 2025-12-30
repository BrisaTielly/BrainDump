<template>
  <div>  
    <!-- <NewBoardDialog/>  -->
      <div class="data-list">
        
        <div class="list-header">
          <span class="col-name">NOME DO FLUXO</span>
          <span class="col-status">STATUS IA</span>
          <span class="col-metrics">COMPLEXIDADE</span>
          <span class="col-date">ATUALIZADO</span>
        </div>

        <div class="list-body">
          <NuxtLink 
          :to="`/boards/${board.id}`" 
          v-for="board in boards" 
          :key="board.id" 
          class="list-row">
              
            <div class="cell-name">
              <div class="file-icon">
                <span class="mini-nodes"></span>
              </div>
              <div class="text-group">
                <span class="row-title">{{ board.title }}</span>
                <span class="row-desc">{{ board.desc }}</span>
              </div>
            </div>

             <StatusBadge 
             :text="board.aiStatus === 'organized' ? 'Organizado': 'Rascunho'" 
             :badgeStatus="board.aiStatus"/>


            <div class="cell-metrics">
              <span class="metric" title="Blocos">
                ▢ {{ board.nodes }}
              </span>
              <span class="metric-divider">/</span>
              <span class="metric" title="Conexões">
                ☍ {{ board.connections }}
              </span>
            </div>

            <div class="cell-date">
              {{ board.lastMod }}
            </div>

            <div class="cell-action">
              <span class="btn-open">Abrir ↵</span>
            </div>

          </NuxtLink>
        </div>

      </div>
  </div>
</template>

<script>
  import StatusBadge from '@/components/UI/StatusBadge.vue';
  import NewBoardDialog from '~/components/Boards/NewBoardDialog.vue';
export default {
  name: 'BoardList',
  components: {
    StatusBadge,
    NewBoardDialog
  },
  data() {
    return {
      boards: [
      ]
    };
  },
  async mounted(){
    this.loadBoards();
  },
  methods:{
    async loadBoards(){
      let response = await this.$axios.get('/boards')
        this.boards = response.data;
        // this.boards = [{ 
        //   id: 1, 
        //   title: 'Sprint 1: MVP BrainDump', 
        //   desc: 'Fluxo principal de desenvolvimento',
        //   nodes: 42, connections: 38, 
        //   aiStatus: 'organized', lastMod: '2h atrás' 
        // },
        // { 
        //   id: 2, 
        //   title: 'Arquitetura de Banco de Dados', 
        //   desc: 'Modelagem das tabelas e relações',
        //   nodes: 12, connections: 15, 
        //   aiStatus: 'draft', lastMod: 'Ontem' 
        // },
        // { 
        //   id: 3, 
        //   title: 'Estudos Vue.js & Design', 
        //   desc: 'Anotações de cursos e referências',
        //   nodes: 156, connections: 210, 
        //   aiStatus: 'organized', lastMod: '23 out' 
        // },
        // { 
        //   id: 4, 
        //   title: 'Ideias Aleatórias', 
        //   desc: 'Sem categoria definida',
        //   nodes: 5, connections: 0, 
        //   aiStatus: 'draft', lastMod: '10 out' 
        // }]
      },
    async createNewBoard(){
      await this.$axios.post('boards/', {title: 'title'})
    }
    },
  }

</script>

<style>
  .data-list {
    padding: 32px;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
  }

  .list-header {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr 80px; 
    padding: 0 16px 12px 16px;
    border-bottom: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.5px;
  }

  .list-body { display: flex; flex-direction: column; }

  .list-row {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr 80px;
    align-items: center;
    text-decoration: none;
    color: inherit;
    padding: 16px; /* Altura controlada, não gigante */
    border-bottom: 1px solid var(--border);
    transition: all 0.15s ease;
    background: white;
  }

  .list-row:hover {
    background-color: var(--bg-subtle);
    border-bottom-color: var(--border-hover);
  }

  .cell-name { display: flex; gap: 12px; align-items: center; }
  
  .file-icon {
    width: 36px; height: 36px;
    background: var(--bg-subtle);
    border: 1px solid var(--border);
    border-radius: 8px;
    display: grid; place-items: center;
  }
  .mini-nodes { 
    width: 6px; height: 6px; background: var(--text-muted); border-radius: 50%; box-shadow: 8px -4px 0 var(--text-muted), 4px 6px 0 var(--text-muted); 
    opacity: 0.5;
  }
  .list-row:hover .mini-nodes { background: var(--accent); box-shadow: 8px -4px 0 var(--accent), 4px 6px 0 var(--accent); opacity: 1; }

  .text-group { display: flex; flex-direction: column; gap: 2px; }
  .row-title { font-weight: 500; font-size: 14px; color: var(--text-main); }
  .row-desc { font-size: 12px; color: var(--text-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 250px;}

  .cell-metrics {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--text-muted);
  }
  .metric-divider { margin: 0 4px; opacity: 0.3; }

  .cell-date { font-size: 13px; color: var(--text-muted); }

  .cell-action { 
    text-align: right; 
    opacity: 0; 
    transform: translateX(-10px); 
    transition: all 0.2s; 
  }
  
  .btn-open {
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    background: var(--accent-fade);
    padding: 4px 8px;
    border-radius: 4px;
    text-transform: uppercase;
  }

  .list-row:hover .cell-action { opacity: 1; transform: translateX(0); }

</style>
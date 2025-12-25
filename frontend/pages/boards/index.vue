<template>
  <div id="pro-app">
    
    <aside class="sidebar">
      <div class="brand">
        <div class="brand-logo">
          <div class="logo-shape"></div>
        </div>
        <span class="brand-name">BrainDump</span>
      </div>

      <nav class="nav-menu">
        <a href="#" class="nav-item active">
          <span class="icon"></span> Meus Fluxos
        </a>
        <a href="#" class="nav-item">
          <span class="icon"></span> Insights IA
        </a>
        <a href="#" class="nav-item">
          <span class="icon"></span> Configurações
        </a>
      </nav>

      <div class="user-profile">
        <div class="avatar">B</div>
        <div class="user-info">
          <span class="name">Brisa Silva</span>
          <span class="role">Pro Plan</span>
        </div>
      </div>
    </aside>

    <main class="main-content">
      
      <header class="top-bar">
        <div class="breadcrumbs">
          <span>Workspace</span>
          <span class="separator">/</span>
          <span class="current">Todos os Quadros</span>
        </div>
        <button class="btn-primary">
          <span>+</span> Novo Quadro
        </button>
      </header>

      <div class="data-list">
        
        <div class="list-header">
          <span class="col-name">NOME DO FLUXO</span>
          <span class="col-status">STATUS IA</span>
          <span class="col-metrics">COMPLEXIDADE</span>
          <span class="col-date">ATUALIZADO</span>
        </div>

        <div class="list-body">
          <a href="#" v-for="board in boards" :key="board.id" class="list-row">
            
            <div class="cell-name">
              <div class="file-icon">
                <span class="mini-nodes"></span>
              </div>
              <div class="text-group">
                <span class="row-title">{{ board.title }}</span>
                <span class="row-desc">{{ board.desc }}</span>
              </div>
            </div>

            <div class="cell-status">
              <span class="status-pill" :class="board.aiStatus">
                <span class="dot"></span>
                {{ board.aiStatus === 'organized' ? 'Organizado' : 'Rascunho' }}
              </span>
            </div>

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

          </a>
        </div>

      </div>
    </main>

  </div>
</template>

<script>
export default {
  name: 'BoardList',
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
      }
    },
  }

</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

  :root {
    /* Paleta Profissional "Linear-like" */
    --bg-app: #ffffff;
    --bg-subtle: #f9fafb; /* Cinza muito claro para hovers/sidebar */
    --border: #e5e7eb;    /* Borda sutil */
    --border-hover: #d1d5db;
    
    --text-main: #111827;
    --text-muted: #6b7280;
    
    --accent: #4f46e5;    /* Indigo Profissional */
    --accent-fade: #eef2ff;
    
    --status-green: #10b981;
    --status-gray: #9ca3af;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background-color: var(--bg-app);
    font-family: 'Inter', sans-serif;
    color: var(--text-main);
    font-size: 14px; /* Fonte base menor = mais profissional */
  }

  /* LAYOUT GERAL (Grid Sidebar + Content) */
  #pro-app {
    display: grid;
    grid-template-columns: 240px 1fr; /* Sidebar fixa, resto fluido */
    height: 100vh;
    overflow: hidden;
  }

  /* --- 1. SIDEBAR --- */
  .sidebar {
    background-color: var(--bg-subtle);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    padding: 20px 16px;
  }

  .brand {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 32px;
    padding-left: 8px;
  }

  .logo-shape {
    width: 20px; height: 20px;
    background: var(--text-main);
    border-radius: 4px;
    position: relative;
  }
  .logo-shape::after {
    content: ''; position: absolute; top: 4px; left: 4px;
    width: 6px; height: 6px; background: white; border-radius: 50%;
  }

  .brand-name { font-weight: 600; font-size: 15px; letter-spacing: -0.3px; }

  .nav-menu { display: flex; flex-direction: column; gap: 4px; flex: 1; }

  .nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 12px;
    color: var(--text-muted);
    text-decoration: none;
    border-radius: 6px;
    font-weight: 500;
    transition: all 0.2s;
  }

  .nav-item:hover { background-color: rgba(0,0,0,0.04); color: var(--text-main); }
  .nav-item.active { background-color: white; color: var(--text-main); box-shadow: 0 1px 2px rgba(0,0,0,0.05); }

  .user-profile {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-top: 16px;
    border-top: 1px solid var(--border);
  }
  .avatar { width: 32px; height: 32px; background: var(--accent); color: white; border-radius: 50%; display: grid; place-items: center; font-size: 12px; font-weight: bold; }
  .user-info { display: flex; flex-direction: column; }
  .name { font-weight: 500; font-size: 13px; }
  .role { font-size: 11px; color: var(--text-muted); }


  /* --- 2. MAIN CONTENT --- */
  .main-content {
    background-color: white;
    display: flex;
    flex-direction: column;
    overflow-y: auto; /* Scroll apenas aqui */
  }

  .top-bar {
    height: 64px;
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 32px;
    position: sticky;
    top: 0;
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(8px);
    z-index: 10;
  }

  .breadcrumbs { color: var(--text-muted); font-size: 13px; }
  .breadcrumbs .current { color: var(--text-main); font-weight: 500; }
  .separator { margin: 0 8px; color: var(--border); }

  .btn-primary {
    background-color: var(--text-main);
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.2s;
  }
  .btn-primary:hover { background-color: #000; }


  /* --- 3. DATA LIST (O coração do design Pro) --- */
  .data-list {
    padding: 32px;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
  }

  .list-header {
    display: grid;
    /* Grid de colunas alinhado com as linhas */
    grid-template-columns: 2fr 1fr 1fr 1fr 80px; 
    padding: 0 16px 12px 16px;
    border-bottom: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.5px;
  }

  .list-body { display: flex; flex-direction: column; }

  /* A LINHA (Row) - Fina e Elegante */
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

  /* Coluna Nome */
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


  /* Coluna Status */
  .status-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 500;
    border: 0px solid transparent;
  }
  
  .dot { width: 6px; height: 6px; border-radius: 50%; }

  .organized { background: #ecfdf5; color: #065f46; border-color: #a7f3d0; }
  .organized .dot { background: #10b981; }

  .draft { background: #f3f4f6; color: #4b5563; border-color: #e5e7eb; }
  .draft .dot { background: #9ca3af; }


  /* Coluna Metrics (Tech font) */
  .cell-metrics {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--text-muted);
  }
  .metric-divider { margin: 0 4px; opacity: 0.3; }


  /* Coluna Date */
  .cell-date { font-size: 13px; color: var(--text-muted); }


  /* Coluna Ação */
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
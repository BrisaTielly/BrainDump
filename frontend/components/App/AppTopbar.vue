 <template>
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
</template>
<script>
  
export default {
  name: 'AppTopbar',
}
</script>

<style>
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

</style>

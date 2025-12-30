<template>
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
</template>

<script>
  
export default {
  name: 'AppSidebar',
}
</script>

<style>
    .sidebar {
    background-color: var(--bg-subtle);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    padding: 20px 16px;
    position: relative;
    z-index: 10;
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
</style>
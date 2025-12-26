<template>
  <div class="cell-status">
        <span class="status-pill" :class="badgeStatus">
        <span class="dot"></span>
            {{text}}
    </span>
    </div>
</template>

<script>
  
export default {
  name: 'StatusBadge',
  props:{
    text: {type: String, default: ''},
    badgeStatus:{ type: String, default: '' }
  }
}
</script>

<style>
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

  .organized { background: #ecfdf5; color:  #065f46; border-color: #a7f3d0; }
  .organized .dot { background: #10b981; }

  .draft { background: #f3f4f6; color: #4b5563; border-color: #e5e7eb; }
  .draft .dot { background: #9ca3af; }

  .fail { background: #fef2f2; color: #7f1d1d; border-color: #fecaca; }
  .fail .dot {background: #ef4444;}

  .warning { background: #fffbeb; color: #92400e;border-color: #fde68a;}
  .warning .dot {background: #f59e0b;}


</style>
<script setup lang="ts">
defineProps<{
  co2Saved: number;
  stats: { label: string; value: string | number }[];
}>();
</script>

<template>
  <div class="bg-emerald-900 rounded-lg p-5 text-white flex justify-between items-center gap-4">
    <div class="flex-1">
      <div class="text-[9px] text-emerald-400 font-bold uppercase tracking-widest mb-1">Total Dampak</div>
      <div class="text-2xl font-bold tracking-tight">{{ co2Saved.toFixed(1) }} Tons CO2</div>
    </div>
    
    <div class="h-10 w-px bg-emerald-800"></div>

    <div class="flex gap-4">
      <div v-for="s in stats" :key="s.label" class="text-center">
        <div class="text-xs font-bold text-white">{{ s.value }}</div>
        <div class="text-[8px] text-emerald-400 font-bold uppercase tracking-tighter">{{ s.label }}</div>
      </div>
    </div>
  </div>
</template>

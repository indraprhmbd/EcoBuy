<script setup lang="ts">
import AppIcon from './AppIcon.vue';

defineProps<{
  title: string;
}>();

defineEmits(['back']);
</script>

<template>
  <div class="fixed inset-0 z-[70] bg-white flex flex-col max-w-2xl mx-auto border-x border-slate-200">
    <header class="p-4 border-b border-slate-100 flex items-center gap-4 flex-shrink-0">
      <button @click="$emit('back')" class="text-slate-400 hover:text-emerald-600 transition-colors">
        <AppIcon name="chevron-left" :size="16" />
      </button>
      <h2 class="text-sm font-bold text-slate-900 uppercase tracking-widest">{{ title }}</h2>
    </header>
    
    <main class="flex-1 overflow-y-auto p-4">
      <slot>
        <div class="py-20 text-center space-y-4">
          <div class="text-slate-300 flex justify-center">
            <AppIcon :name="'home'" :size="48" />
          </div>
          <div class="text-sm font-bold text-slate-400 uppercase tracking-widest">Mockup Halaman {{ title }}</div>
          <p class="text-xs text-slate-400 max-w-xs mx-auto">Halaman ini sedang dalam pengembangan untuk versi produksi.</p>
        </div>
      </slot>
    </main>
  </div>
</template>

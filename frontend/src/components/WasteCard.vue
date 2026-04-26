<script setup lang="ts">
import type { Waste } from '../api/waste';

const props = defineProps<{
  item: Waste;
  variant?: 'grid' | 'list';
}>();

const emit = defineEmits<{
  (e: 'click', item: Waste): void;
}>();

const formatPrice = (p: number) => `Rp ${p.toLocaleString('id-ID')}`;
</script>

<template>
  <div 
    @click="emit('click', props.item)"
    :class="[
      'cursor-pointer bg-white border border-slate-200 transition-colors rounded-lg overflow-hidden',
      props.variant === 'list' ? 'flex gap-3 items-center p-3' : 'flex flex-col p-3 space-y-2'
    ]"
  >
    <!-- Image Section -->
    <div 
      :class="[
        'rounded bg-slate-50 flex-shrink-0 border border-slate-100',
        props.variant === 'list' ? 'w-12 h-12' : 'aspect-square w-full'
      ]"
    >
      <img v-if="props.item.image_url" :src="props.item.image_url" class="w-full h-full object-cover" />
      <div v-else class="w-full h-full flex items-center justify-center text-[10px] text-slate-400 font-bold uppercase p-2 text-center leading-tight">
        No Image
      </div>
    </div>

    <!-- Info Section -->
    <div :class="props.variant === 'list' ? 'flex-1 min-w-0' : 'space-y-1'">
      <div class="flex justify-between items-center mb-0.5">
        <span class="text-[8px] font-bold px-1.5 py-0.5 bg-slate-100 text-slate-600 rounded uppercase tracking-wider">
          Grade A
        </span>
      </div>
      
      <div class="font-bold text-slate-900 text-sm truncate">{{ props.item.type || 'Limbah' }}</div>
      
      <div class="flex items-center justify-between">
        <div class="text-emerald-600 font-bold text-sm">{{ formatPrice(850) }}</div>
        <div class="text-[10px] text-slate-400 font-bold">{{ props.item.weight || 0 }} kg</div>
      </div>
    </div>
  </div>
</template>

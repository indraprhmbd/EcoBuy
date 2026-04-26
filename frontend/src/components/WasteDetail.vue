<script setup lang="ts">
import type { Waste } from '../api/waste';
import AppIcon from './AppIcon.vue';

defineProps<{
  item: Waste;
}>();

defineEmits(['close', 'buy']);

const formatPrice = (p: number) => `Rp ${p.toLocaleString('id-ID')}`;
</script>

<template>
  <div class="fixed inset-0 z-[60] bg-white flex flex-col max-w-2xl mx-auto shadow-2xl border-x border-slate-200">
    <!-- Header -->
    <div class="p-4 flex items-center justify-between border-b border-slate-100 flex-shrink-0">
      <button @click="$emit('close')" class="text-xs font-bold text-slate-500 uppercase flex items-center gap-1 hover:text-emerald-600 transition-colors">
        <AppIcon name="chevron-left" :size="14" />
        Kembali
      </button>
      <div class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Detail Listing</div>
    </div>

    <!-- Content -->
    <div class="flex-1 overflow-y-auto p-4 space-y-6">
      <div class="aspect-[3/2] bg-slate-100 rounded border border-slate-200 overflow-hidden relative">
        <img v-if="item.image_url" :src="item.image_url" class="w-full h-full object-cover" />
        <div v-else class="w-full h-full flex items-center justify-center text-slate-300 font-bold uppercase text-[10px]">
          Foto tidak tersedia
        </div>
      </div>

      <div class="space-y-4">
        <div class="flex justify-between items-start">
          <div class="flex-1 pr-4">
            <h2 class="text-xl font-bold text-slate-900 leading-tight">{{ item.type }}</h2>
            <p class="text-slate-500 text-xs mt-1 font-medium">Surabaya, Jawa Timur</p>
          </div>
          <div class="text-right">
            <div class="text-xl font-bold text-emerald-600">{{ formatPrice(850) }}</div>
            <div class="text-[10px] text-slate-400 font-bold uppercase">Per kg</div>
          </div>
        </div>
        
        <div class="grid grid-cols-2 gap-3">
          <div class="bg-slate-50 p-4 rounded border border-slate-100">
            <div class="text-[9px] text-slate-400 uppercase font-bold mb-1 tracking-wider">Kuantitas</div>
            <div class="font-bold text-slate-800 text-lg">{{ item.weight }} kg</div>
          </div>
          <div class="bg-slate-50 p-4 rounded border border-slate-100">
            <div class="text-[9px] text-slate-400 uppercase font-bold mb-1 tracking-wider">Grade AI</div>
            <div class="font-bold text-slate-800 text-lg">Grade A</div>
          </div>
        </div>

        <div class="bg-slate-50/50 p-4 rounded border border-slate-100 space-y-2">
          <h3 class="text-[10px] font-bold text-slate-900 uppercase tracking-widest">Deskripsi</h3>
          <p class="text-sm text-slate-600 leading-relaxed font-medium">
            Limbah berkualitas tinggi hasil sortir industri. Bersih, kering, dan siap diolah kembali. 
            Pengangkutan tersedia dengan biaya tambahan yang dapat dinegosiasikan.
          </p>
        </div>
      </div>
    </div>

    <!-- Actions -->
    <div class="p-4 border-t border-slate-100 bg-white flex gap-3 flex-shrink-0">
      <button class="btn btn-outline flex-1 py-4 text-sm font-bold">Chat</button>
      <button @click="$emit('buy', item.id)" class="btn btn-primary flex-1 py-4 text-sm font-bold">Beli</button>
    </div>
  </div>
</template>

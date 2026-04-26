<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { store } from './store';
import type { Waste } from './api/waste';

import AppIcon from './components/AppIcon.vue';
import WasteCard from './components/WasteCard.vue';
import WasteDetail from './components/WasteDetail.vue';
import ImpactHero from './components/ImpactHero.vue';
import ProfileSubPage from './components/ProfileSubPage.vue';

// Navigation
const activeTab = ref('home');
const activeSubPage = ref<string | null>(null);
const selectedWaste = ref<Waste | null>(null);

// Static Mockup Data
const staticWastes: Waste[] = [
  { id: 1, type: 'Kertas (Kardus)', weight: 500, status: 'available', lat: 0, lng: 0, validation_confidence: 0.98, image_url: '' },
  { id: 2, type: 'Plastik (PET)', weight: 250, status: 'available', lat: 0, lng: 0, validation_confidence: 0.95, image_url: '' },
  { id: 3, type: 'Logam (Aluminium)', weight: 120, status: 'available', lat: 0, lng: 0, validation_confidence: 0.92, image_url: '' },
  { id: 4, type: 'Kaca (Bening)', weight: 300, status: 'available', lat: 0, lng: 0, validation_confidence: 0.90, image_url: '' }
];

const homeStats = [
  { label: 'Listing', value: 12 },
  { label: 'Selesai', value: 8 },
  { label: 'Rating', value: 4.8 }
];

const tabs = [
  { id: 'home', label: 'Beranda', icon: 'home' as const },
  { id: 'marketplace', label: 'Pasar', icon: 'search' as const },
  { id: 'sell', label: 'Jual', icon: 'plus' as const },
  { id: 'profile', label: 'Profil', icon: 'user' as const }
];

const searchQuery = ref('');
const displayWastes = computed<Waste[]>(() => {
  const source = store.wastes.length > 0 ? store.wastes : staticWastes;
  if (!searchQuery.value) return source;
  return source.filter(w => (w.type || '').toLowerCase().includes(searchQuery.value.toLowerCase()));
});

const handleBuy = (id: number) => {
  console.log('Buying waste:', id);
  selectedWaste.value = null;
  alert('Permintaan pembelian dikirim');
};

onMounted(() => {
  store.fetchWastes();
});
</script>

<template>
  <div class="min-h-screen pb-20 flex flex-col bg-slate-50 font-sans">
    <!-- Header -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50">
      <div class="max-w-2xl mx-auto px-4 h-14 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 bg-emerald-600 rounded flex items-center justify-center text-white font-bold text-sm">EB</div>
          <h1 class="text-slate-900 font-bold text-lg">EcoBuy</h1>
        </div>
        <button class="text-slate-400">
          <AppIcon name="bell" :size="20" />
        </button>
      </div>
    </header>

    <main class="flex-1 max-w-2xl mx-auto w-full p-4 overflow-x-hidden">
      
      <!-- Detail View -->
      <WasteDetail 
        v-if="selectedWaste" 
        :item="selectedWaste!" 
        @close="selectedWaste = null"

        @buy="handleBuy"
      />

      <!-- Beranda -->
      <div v-if="activeTab === 'home'" class="space-y-6">
        <ImpactHero :co2-saved="12.4" :stats="homeStats" />

        <section>
          <div class="flex items-center justify-between mb-3 px-1">
            <h3 class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Listing Aktif</h3>
            <button @click="activeTab = 'marketplace'" class="text-[10px] text-emerald-600 font-bold uppercase tracking-widest">Lihat Semua</button>
          </div>
          <div class="grid grid-cols-2 gap-3">
            <WasteCard 
              v-for="item in displayWastes.slice(0, 4)" 
              :key="item.id" 
              :item="item" 
              variant="grid"
              @click="selectedWaste = $event"
            />
          </div>
        </section>
      </div>

      <!-- Pasar -->
      <div v-else-if="activeTab === 'marketplace'" class="space-y-4">
        <div class="relative">
          <AppIcon name="search" :size="16" class="absolute left-3.5 top-3.5 text-slate-400" />
          <input v-model="searchQuery" type="text" placeholder="Cari limbah..." class="input pl-11 py-3 text-sm border-slate-200" />
        </div>
        
        <div class="grid grid-cols-2 gap-3 pb-4">
          <WasteCard 
            v-for="item in displayWastes" 
            :key="item.id" 
            :item="item" 
            variant="grid"
            @click="selectedWaste = $event"
          />
        </div>
      </div>

      <!-- Jual -->
      <div v-else-if="activeTab === 'sell'" class="space-y-6">
        <div class="space-y-1">
          <h2 class="text-xl font-bold text-slate-900">Jual Limbah</h2>
          <p class="text-sm text-slate-500 font-medium">Layanan validasi AI untuk hasil maksimal.</p>
        </div>

        <div class="border-2 border-dashed border-slate-200 rounded p-12 text-center bg-white">
          <div class="bg-slate-50 w-12 h-12 rounded-full mx-auto flex items-center justify-center text-slate-400 mb-4 border border-slate-100">
            <AppIcon name="plus" :size="24" />
          </div>
          <div class="text-sm font-bold text-slate-900">Unggah Foto</div>
          <div class="text-[10px] text-slate-400 font-bold uppercase mt-1">Maksimal 10MB</div>
        </div>
      </div>

      <!-- Profil -->
      <div v-else-if="activeTab === 'profile'" class="space-y-6">
        <div class="card flex items-center gap-4 bg-white p-5 border-slate-200 rounded">
          <div class="w-12 h-12 bg-emerald-50 text-emerald-700 rounded flex items-center justify-center font-bold text-lg border border-emerald-100">BU</div>
          <div class="flex-1">
            <div class="text-base font-bold text-slate-900">Budi Utomo</div>
            <div class="text-[10px] text-emerald-600 uppercase font-bold tracking-widest">Farmer Terverifikasi</div>
          </div>
        </div>

        <section class="space-y-1">
          <button 
            v-for="link in ['Pengaturan Akun', 'Riwayat Transaksi', 'Laporan Dampak', 'Pusat Bantuan']" 
            :key="link" 
            @click="activeSubPage = link"
            class="w-full card flex justify-between items-center py-3 px-4 text-sm font-bold border-slate-200 hover:bg-slate-50 transition-colors"
          >
            <span class="text-slate-600">{{ link }}</span>
            <AppIcon name="chevron-right" :size="14" class="text-slate-300" />
          </button>
        </section>

        <button class="w-full py-4 text-[10px] font-bold text-slate-400 uppercase tracking-widest border border-slate-200 rounded hover:bg-red-50 hover:text-red-500 transition-colors">
          Keluar dari Akun
        </button>
      </div>

      <!-- Profile Sub Pages -->
      <ProfileSubPage 
        v-if="activeSubPage" 
        :title="activeSubPage" 
        @back="activeSubPage = null"
      >
        <!-- Custom Content for specific pages can go here -->
        <div v-if="activeSubPage === 'Riwayat Transaksi'" class="space-y-3">
          <div v-for="i in 3" :key="i" class="card border-slate-100 bg-slate-50 p-3 flex justify-between items-center">
            <div>
              <div class="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">26 Apr 2026</div>
              <div class="text-sm font-bold text-slate-800">Pembelian Kardus Bekas</div>
            </div>
            <div class="text-emerald-600 font-bold text-sm">Selesai</div>
          </div>
        </div>
        <div v-else-if="activeSubPage === 'Laporan Dampak'" class="space-y-4">
          <div class="bg-emerald-900 rounded p-6 text-white text-center">
            <div class="text-3xl font-bold mb-1">12.4</div>
            <div class="text-[10px] text-emerald-400 font-bold uppercase tracking-widest">Tons CO2 Diselamatkan</div>
          </div>
          <p class="text-xs text-slate-500 text-center font-medium">Laporan lengkap akan dikirimkan ke email Anda setiap bulan.</p>
        </div>
      </ProfileSubPage>



    </main>

    <!-- Bottom Nav -->
    <nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 z-[50]">
      <div class="max-w-2xl mx-auto flex h-16">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="activeTab = tab.id; selectedWaste = null;"
          class="flex-1 flex flex-col items-center justify-center gap-1"
          :class="activeTab === tab.id ? 'text-emerald-600 font-bold' : 'text-slate-300'"
        >
          <AppIcon :name="tab.icon" :size="20" />
          <span class="text-[9px] uppercase tracking-widest font-bold">{{ tab.label }}</span>
        </button>
      </div>
    </nav>
  </div>
</template>

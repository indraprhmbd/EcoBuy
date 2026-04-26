import { reactive } from 'vue';
import { getWasteList, createWaste, type Waste } from './api/waste';
import { getImpactDashboard } from './api/impact';
import { requestWaste } from './api/request';

export const store = reactive({
  user: { id: 1, name: 'Budi Utomo', role: 'farmer' },
  wastes: [] as Waste[],
  impact: null as any,
  loading: false,
  error: null as string | null,

  async fetchWastes() {
    this.loading = true;
    try {
      const data = await getWasteList();
      this.wastes = (data as any).data || data;
    } catch (e: any) {
      this.error = e.message;
    } finally {
      this.loading = false;
    }
  },

  async postWaste(payload: any) {
    this.loading = true;
    try {
      const res = await createWaste(payload);
      await this.fetchWastes();
      return res;
    } catch (e: any) {
      this.error = e.message;
    } finally {
      this.loading = false;
    }
  },

  async buyWaste(id: number) {
    try {
      await requestWaste(id);
      await this.fetchWastes();
    } catch (e: any) {
      this.error = e.message;
      throw e;
    }
  },

  async validateWaste(file: File) {
    this.loading = true;
    try {
      const formData = new FormData();
      formData.append('file', file);
      
      const response = await fetch('/api/v1/waste/validate', {
        method: 'POST',
        body: formData
      });
      
      if (!response.ok) throw new Error('Upload gagal');
      const res = await response.json();
      return res.data;
    } catch (e: any) {
      this.error = e.message;
      throw e;
    } finally {
      this.loading = false;
    }
  },

  async fetchImpact() {

    try {
      const data = await getImpactDashboard();
      this.impact = (data as any).data || data;
    } catch (e) {}
  }
});


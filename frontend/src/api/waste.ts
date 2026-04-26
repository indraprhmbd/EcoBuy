import { fetchClient } from './client';

export interface Waste {
  id: number;
  type: string;
  weight: number;
  lat: number;
  lng: number;
  status: string;
  validation_confidence: number;
}

export interface WasteCreatePayload {
  type: string;
  weight: number;
  lat: number;
  lng: number;
  image_url?: string;
}

export const getWasteList = async (status: string = 'available'): Promise<Waste[]> => {
  const params = new URLSearchParams({ status });
  return fetchClient<Waste[]>(`/waste?${params.toString()}`);
};

export const createWaste = async (payload: WasteCreatePayload): Promise<any> => {
  return fetchClient<any>('/waste', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
};

export const getRecommendations = async (lat: number, lng: number): Promise<any> => {
  const params = new URLSearchParams({ lat: lat.toString(), lng: lng.toString() });
  return fetchClient<any>(`/waste/recommendations?${params.toString()}`);
};

export const completeWaste = async (id: number): Promise<any> => {
  return fetchClient<any>(`/waste/${id}/complete`, {
    method: 'POST',
  });
};

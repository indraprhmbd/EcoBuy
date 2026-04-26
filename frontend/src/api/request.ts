import { fetchClient } from './client';

export const requestWaste = async (wasteId: number): Promise<any> => {
  return fetchClient<any>('/request', {
    method: 'POST',
    body: JSON.stringify({ waste_id: wasteId }),
  });
};

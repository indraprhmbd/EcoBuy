import { fetchClient } from './client';

export interface ImpactDashboard {
  total_waste: number;
  by_type: Record<string, number>;
  emission_reduction: number;
}

export const getImpactDashboard = async (): Promise<ImpactDashboard> => {
  return fetchClient<ImpactDashboard>('/impact');
};

export const API_BASE_URL = 'http://localhost:8000/api/v1';

export const fetchClient = async <T>(endpoint: string, options: RequestInit = {}): Promise<T> => {
  const url = `${API_BASE_URL}${endpoint}`;
  
  const headers = {
    'Content-Type': 'application/json',
    ...options.headers,
  };

  const response = await fetch(url, {
    ...options,
    headers,
  });

  if (!response.ok) {
    let errorMessage = 'An error occurred';
    try {
      const errorData = await response.json();
      errorMessage = errorData.message || errorMessage;
    } catch {
      // Ignored
    }
    throw new Error(errorMessage);
  }

  // Assuming the API standard wraps response in { data, message, error }
  // but if the endpoint just returns data directly we handle it here.
  const data = await response.json();
  return data;
};

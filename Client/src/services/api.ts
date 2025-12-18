import axios from 'axios';

const TOKEN_STORAGE_KEY = 'authToken';

const baseURL = import.meta.env.VITE_API_BASE_URL + '/api';

/* 🔍 REQUIRED DEBUG (keep for now) */
console.log('[API INIT] VITE_API_BASE_URL =', import.meta.env.VITE_API_BASE_URL);
console.log('[API INIT] Axios baseURL =', baseURL);

const api = axios.create({
  baseURL,
  withCredentials: true,
});

// Attach token from localStorage if present
api.interceptors.request.use((config) => {
  const token = localStorage.getItem(TOKEN_STORAGE_KEY);

  /* 🔍 REQUIRED DEBUG */
  console.log('[API REQUEST]', {
    method: config.method?.toUpperCase(),
    baseURL: config.baseURL,
    url: config.url,
    fullURL: `${config.baseURL}${config.url}`,
    hasToken: Boolean(token),
  });

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => {
    /* 🔍 REQUIRED DEBUG */
    console.log('[API RESPONSE]', {
      status: response.status,
      url: response.config?.url,
    });
    return response;
  },
  (error) => {
    /* 🔍 REQUIRED DEBUG */
    console.error('[API RESPONSE ERROR]', {
      status: error.response?.status,
      url: error.config?.url,
      fullURL: `${error.config?.baseURL}${error.config?.url}`,
    });
    return Promise.reject(error);
  }
);

export default api;

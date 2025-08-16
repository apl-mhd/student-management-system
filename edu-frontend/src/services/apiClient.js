import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  headers: {
    'X-Requested-With': 'XMLHttpRequest',
    Accept: 'application/json',
  },
})

apiClient.interceptors.request.use((config) => {
  const access = localStorage.getItem('access')
  console.log('access', access)
  if (access) {
    config.headers.Authorization = `Bearer ${access}`
  }
  return config
})

export default apiClient

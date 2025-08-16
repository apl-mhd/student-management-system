import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

export const showToast = (msg, type = 'info') => {
  const defaultOptions = {
    autoClose: 2000,
    position: toast.POSITION.TOP_RIGHT,
  }

  if (type === 'info') {
    toast.info(msg, defaultOptions)
  }
  if (type === 'success') {
    toast.success(msg, defaultOptions)
  }
  if (type === 'warning') {
    toast.warning(msg, defaultOptions)
  }
  if (type === 'error') {
    toast.error(msg, defaultOptions)
  }
}

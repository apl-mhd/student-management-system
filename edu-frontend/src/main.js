import './assets/main.css'
import 'vue-select/dist/vue-select.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
// import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
// import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'bootstrap'
import 'vue3-toastify/dist/index.css'
import VueSelect from 'vue-select'
import App from './App.vue'
import router from './router'


const app = createApp(App)

// app.use(BootstrapVue3)
app.use(createPinia())
app.use(router)
app.component('v-select', VueSelect)

app.mount('#app')

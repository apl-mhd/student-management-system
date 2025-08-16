<template>
  <div class="login">
    <h1>Student Login</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" id="username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import apiClient from '@/services/apiClient'

const router = useRouter()

const username = ref('')
const password = ref('')
const errorMessage = ref('')
const handleLogin = () => {
  apiClient
    .post('/students/token/', {
      username: username.value,
      password: password.value,
    })
    .then((response) => {
      if (response.data.access) {
        localStorage.setItem('access', response.data.access)
        localStorage.setItem('user', JSON.stringify(response.data.user))
        localStorage.setItem('isLoggedIn', true)
        router.push('/students')
      } else {
        errorMessage.value = 'Invalid credentials'
      }
    })
    .catch((error) => {
      errorMessage.value = 'An error occurred. Please try again.'
    })
}
</script>

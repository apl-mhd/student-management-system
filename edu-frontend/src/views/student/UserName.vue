<script setup>
const firstName = defineModel('firstName')
const lastName = defineModel('lastName')
const show = () => {
  console.log('clicked')
  firstName.value
  = 'orko'
}
</script>

<template>
  {{ firstName }} -- {{ lastName }}
  <input name="a" type="text" v-model="firstName" />
  <input type="text" v-model="lastName" />
  <button @click="show">click</button>
</template>

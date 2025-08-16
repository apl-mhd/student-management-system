<template>
  <div class="blog-post">
    <h4>{{ title }}</h4>
    <button @click="$emit('enlarge-text')">Enlarge Text</button>
  </div>
</template>

<script setup>
const a = 3
defineProps(['title'])
defineEmits(['enlarge-text'])
</script>

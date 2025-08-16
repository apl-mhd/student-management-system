<script setup></script>

<template>
  <div class="mt-5 mb-5">
    <form class="row gx-4 gy-4  pb-5">
      <div class="col-4">
        <label for="name" class="form-label">Name</label>
        <v-select :options="['Canada', 'United States']"></v-select>
      </div>
      <div class="col-4">
        <label for="name" class="form-label">Category</label>
        <v-select :options="['Canada', 'United States']"></v-select>
      </div>
      <div class="col-4">
        <label for="name" class="form-label">Course/Other</label>
        <v-select :options="['Canada', 'United States']"></v-select>
      </div>
    </form>
  </div>
</template>

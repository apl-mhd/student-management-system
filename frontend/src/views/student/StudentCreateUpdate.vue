<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'

const props = defineProps(['batches', 'academicYears', 'homeTowns', 'colleges', 'errors'])
const emit = defineEmits(['resetForm', 'createStudent'])

const student = defineModel('student')

const studentsList = ref([])

const studentForm = (studentData) => {
  axios.defaults.xsrfCookieName = 'csrftoken'
  axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

  emit('createStudent', studentData)
}
</script>

<template>
  <div class="mt-5">
    <form class="row gx-3 gy-4" @submit.prevent="studentForm(student)">
      <div class="col-4">
        <label for="name" class="form-label">Name *</label>
        <input
          type="text"
          name="name"
          placeholder="Mahmud"
          v-model="student.name"
          class="form-control"
          :class="errors.name ? 'is-invalid' : ''"
          id="name"
          aria-describedby="nameValidation"
        />
        <div id="validationServer03Feedback" class="invalid-feedback">
          {{ errors.name }}
        </div>
      </div>

      <div class="col-4">
        <label for="phone" class="form-label">Phone *</label>
        <input
          type="text"
          name="phone"
          placeholder="015-xx-xx-xx-xx"
          v-model="student.phone"
          class="form-control"
          :class="errors.phone ? 'is-invalid' : ''"
          aria-describedby="phoneValidation"
          id="phone"
        />
        <div id="phoneValidation" class="invalid-feedback">{{ errors.phone }}</div>
      </div>
      <div class="col-4">
        <label for="ParentsPhone" class="form-label">Gurdian Phone</label>
        <input
          type="text"
          name="gurdian_phone"
          placeholder="017-xx-xx-xx-xx"
          v-model="student.gurdian_phone"
          class="form-control"
          id="ParentsPhone"
        />
      </div>
      <div class="col-4">
        <label for="email" class="form-label">Email</label>
        <input
          type="email"
          placeholder="contact@mail.com"
          v-model="student.email"
          name="email"
          class="form-control"
          id="email"
        />
      </div>
      <div class="col-4">
        <label for="gender" class="form-label">Gender *</label>
        <select
          class="form-select"
          v-model="student.gender"
          name="gender"
          id="gender"
          :class="errors.gender ? 'is-invalid' : ''"
          aria-describedby="genderValidation"
        >
          <option value="M">Male</option>
          <option value="F">Female</option>
        </select>
        <div id="genderValidation" class="invalid-feedback">{{ errors.gender }}</div>
      </div>
      <div class="col-4">
        <label for="student-batch" class="form-label">Batch *</label>
        <select
          class="form-select"
          v-model="student.batch"
          name="course"
          id="student-batch"
          :class="errors.batch ? 'is-invalid' : ''"
          aria-describedby="batchValidation"
        >
          <option disabled value="null">Select Batch</option>
          <option v-for="batch in batches" :key="batch.id" :value="batch.id">
            {{ batch.title }}
          </option>
        </select>
        <div id="batchValidation" class="invalid-feedback">{{ errors.batch }}</div>
      </div>
      <div class="col-4">
        <label for="academicYear" class="form-label">HSC Batch *</label>
        <select
          class="form-select"
          name="hsc_batch"
          v-model="student.hsc_batch"
          id="academicYear"
          :class="errors.hsc_batch ? 'is-invalid' : ''"
          aria-describedby="hscBatchValidation"
        >
          <option disabled value="null">Select Batch</option>
          <option v-for="year in academicYears" :key="year.id" :value="year.id">
            HSC Batch {{ year.year }} -{{ year.year + 1 }}
          </option>
        </select>
        <div id="hscBatchValidation" class="invalid-feedback">{{ errors.hsc_batch }}</div>
      </div>
      <div class="col-4">
        <label for="location" class="form-label">Home Town</label>
        <select class="form-select" name="home_town" v-model="student.home_town" id="location">
          <option disabled value="null">Select Home Town</option>
          <option v-for="town in homeTowns" :key="town.id" :value="town.id">{{ town.name }}</option>
        </select>
      </div>
      <div class="col-4">
        <label for="college" class="form-label">College</label>
        <select class="form-select" name="college" v-model="student.college" id="college">
          <option disabled value="null">Select College</option>
          <option v-for="college in colleges" :key="college.id" :value="college.id">
            {{ college.name }}
          </option>
        </select>
      </div>
      <div class="col-12 d-flex justify-content-between">
        <button type="submit" class="btn btn-primary">
          {{ student.id ? 'Update' : 'Create' }}
        </button>
        <button :disabled="student.id" type="reset" class="btn btn-danger me-2" @click="resetForm">
          Reset
        </button>
      </div>
    </form>
  </div>
</template>

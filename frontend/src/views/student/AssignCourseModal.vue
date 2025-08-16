<script setup>
import { useTemplateRef, defineExpose } from 'vue'
import { Modal } from 'bootstrap'

const props = defineProps(['studentTableRow', 'courses'])
const courseAssignFormData = defineModel('courseAssignFormData')
const modalRef = useTemplateRef('modal')
const emit = defineEmits(['courseAssign'])

const submitForm = (data) => {
  emit('courseAssign', data)
}

const openModal = () => {
  const modal = new Modal(modalRef.value)
  modal.show()
}

defineExpose({ openModal })
</script>
<template>
  <div
    ref="modal"
    class="modal fade"
    id="assignCourseModal"
    tabindex="-1"
    aria-labelledby="assignCourseModalLable"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title fs-5" id="assignCourseModalLable">
            Payment of ID# {{ studentTableRow.student_roll }} --- Name: {{ studentTableRow.name }}
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitForm(courseAssignFormData)">
            <input type="text" hidden v-model="courseAssignFormData.student" />

            <div class="row mb-3">
              <div class="col-md-12">
                <label for="course">Select Course *</label>
                <select
                  class="form-select"
                  v-model="courseAssignFormData.course"
                  name="course"
                  id="course"
                >
                  <option disabled value="null">Select Course</option>
                  <option v-for="course in courses" :key="course.id" :value="course.id">
                    {{ course.name }}-{{ course.course_fee }} Tk
                  </option>
                </select>
              </div>
              <div class="col mt-3">
                <label for="courseFee" class="col-form-label">Discount Amount</label>
                <input
                  type="text"
                  class="form-control"
                  id="courseFee"
                  v-model="courseAssignFormData.discount_amount"
                />
              </div>
              <div class="col mt-3">
                <label for="payment" class="col-form-label">Payment Amount</label>
                <input
                  min="1"
                  type="text"
                  class="form-control"
                  v-model="courseAssignFormData.payment_amount"
                  id="payment"
                />
              </div>
            </div>

            <div class="mb-3">
              <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
              <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Submit</button>
            </div>
          </form>
        </div>
        <div class="footer"></div>
      </div>
    </div>
  </div>
</template>

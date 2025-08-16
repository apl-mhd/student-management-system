<script setup>
import { Modal } from 'bootstrap'
import { useTemplateRef, defineExpose, ref } from 'vue'

const paymentFormData = defineModel('paymentFormData')
const props = defineProps(['studentTableRow'])
const modalRef = useTemplateRef('modal')
const emit = defineEmits(['createPayment'])

const openModal = () => {
  const modal = new Modal(modalRef.value)
  modal.show()
}
const closeModal = () => {
  const modal = new Modal(modalRef.value)
  modal.dispose()
}

defineExpose({ openModal, closeModal })

const createPayment = (paymentData) => {
  emit('createPayment', paymentData)
}
</script>

<template>
  <div
    ref="modal"
    class="modal"
    id="paymentModal"
    tabindex="-1"
    aria-labelledby="paymentModal"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title fs-5" id="paymentModalLable">
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
          <form @submit.prevent="createPayment(paymentFormData)">
            <input type="text" hidden v-model="paymentFormData.student" />
            <div class="row mb-3">
              <div class="col">
                <label for="courseFee" class="col-form-label">Due Amount</label>
                <input
                  type="text"
                  class="form-control"
                  id="courseFee"
                  disabled
                  :value="studentTableRow.due_amount - paymentFormData.payment_amount"
                />
              </div>
              <div class="col">
                <label for="payment" class="col-form-label">Payment Amount</label>
                <input
                  min="1"
                  type="text"
                  class="form-control"
                  v-model="paymentFormData.payment_amount"
                  id="payment"
                />
              </div>
            </div>

            <div class="mb-3">
              <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
              <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Pay Now</button>
            </div>
          </form>
        </div>
        <div class="footer"></div>
      </div>
    </div>
  </div>
</template>

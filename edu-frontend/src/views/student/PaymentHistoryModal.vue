<script setup>
import { Modal } from 'bootstrap'
import { useTemplateRef, onMounted } from 'vue'
import { defineExpose } from 'vue'
const props = defineProps(['studentPaymentList', 'studentTableRow'])
const modalRef = useTemplateRef('modal')

onMounted(() => {})
const openModal = () => {
  const modal = new Modal(modalRef.value)
  modal.show()
}

defineExpose({ openModal })
</script>

<template>
  <!-- Modal -->
  <div
    ref="modal"
    class="modal fade"
    id="paymentHistoryModal"
    tabindex="-1"
    aria-labelledby="paymentHistoryModal"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <p class="modal-title fs-5" id="paymentHistoryModalLable">
            Student Payment History <br />
            ID # {{ studentTableRow.student_roll }} -- {{ studentTableRow.name }}
          </p>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="mb-2">
            <span class="f-3"
              >Total Fee:
              {{
                studentTableRow.total_course_amount ? studentTableRow.total_course_amount : 'N/A'
              }}
            </span>
            <br />
            <span class="f-1"
              >Total Payment:
              {{ studentTableRow.total_payment ? studentTableRow.total_payment : 'N/A' }}</span
            >
            <br />
            <span class="f-1"
              >Total Discount:
              {{ studentTableRow.total_discount ? studentTableRow.total_discount : 'N/A' }}</span
            >
            <br />
            <span class="f-1">Due Amount: {{ studentTableRow.due_amount }}</span>
          </div>
          <div class="row">
            <table class="table table-light table-striped table-hover table-bordered table-sm">
              <thead class="table-dark">
                <tr>
                  <th scope="col">ID</th>
                  <th scope="col">Amount</th>
                  <th scope="col">Payment Date</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(studentPayment, index) in studentPaymentList" :key="index">
                  <th>{{ index + 1 }}</th>
                  <th>{{ studentPayment.payment_amount }}</th>
                  <th>{{ studentPayment.payment_date }}</th>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useTemplateRef } from 'vue'
import { showToast } from '@/utils/toast'
import StudentCreateUpdate from '@/views/student/StudentCreateUpdate.vue'
import PaymentHistoryModal from './PaymentHistoryModal.vue'
import AssignCourseModal from './AssignCourseModal.vue'
import PaymentModal from './PaymentModal.vue'
import apiClient from '@/services/apiClient'
import { BOverlay, BCollapse, BButton } from 'bootstrap-vue-3'

const batches = ref([])
const academicYears = ref([])
const homeTowns = ref([])
const colleges = ref([])
const paymentList = ref(null)

const isLoading = ref(true)

const blankStudent = {
  id: null,
  name: null,
  phone: null,
  gurdian_phone: null,
  email: null,
  gender: 'M',
  batch: null,
  hsc_batch: null,
  home_town: null,
  college: null,
}
const student = ref(JSON.parse(JSON.stringify(blankStudent)))

const errors = ref({})
const students = ref({})
const studentPaymentList = ref([])
const studentTableRow = ref({})

const query = ref({
  q: '',
  sortBy: '',
  batchBy: '',
  filterBy: '',
  pageSize: 10,
  page: 1,
})

const q = ref('')
const sortBy = ref('')
const batchBy = ref('')
const filterBy = ref('')
const pageSize = ref(10)
const page = ref(1)
const pageSizes = ref([10, 25, 50, 100])

const courses = ref([])

const blankPaymentForm = ref({
  student: null,
  payment_amount: 0,
})

const paymentFormData = ref({
  student: null,
  payment_amount: 0,
})

const blankAssignCourseForm = ref({
  student: null,
  course: null,
  discount_amount: null,
  payment_amount: null,
})

const courseAssignFormData = ref({
  student: null,
  course: null,
  discount_amount: null,
  payment_amount: null,
})

const filters = ref([
  {
    id: 'name',
    value: 'Name',
  },
  {
    id: 'batch__name',
    value: 'Batch',
  },
  {
    id: 'hsc_batch__year',
    value: 'HSC',
  },
  {
    id: 'due_amount',
    value: 'Due amount',
  },
  {
    id: 'paid_current_month',
    value: 'Paid',
  },
  {
    id: 'latest_payment',
    value: 'Latest payment',
  },
])

const visible = ref(false)

const isLoadingFalse = () => {
  isLoading.value = false
}
const isLoadingTrue = () => {
  isLoading.value = true
}

const resetStudent = () => {
  student.value = JSON.parse(JSON.stringify(blankStudent))
}

const resetForm = () => {
  resetStudent()
  errors.value = {}
}

const fetchStudents = (url = null) => {
  isLoadingFalse()
  let apiUrl =
    url ||
    `/students/filter/?q=${q.value}&sort_by=${sortBy.value}&filter_by=${filterBy.value}&batch=${batchBy.value}&page=${page.value}&page_size=${query.value.pageSize}`
  console.log(apiUrl)
  console.log(filterBy.value)

  apiClient
    .get(apiUrl)
    .then((response) => {
      students.value = response.data
      isLoadingFalse()
    })
    .catch((error) => {})
}

const fetchCourses = () => {
  apiClient
    .get(`/courses/`)
    .then((response) => {
      courses.value = response.data
    })
    .catch((error) => {})
}

const createStudent = (studentData) => {
  isLoadingTrue()
  if (studentData.id) {
    apiClient
      .put(`/students/update/${studentData.id}/`, studentData)
      .then((response) => {
        fetchStudents()
        resetStudent()
        showToast("Student's information updated successfully", 'success')
        errors.value = {}
      })
      .catch((error) => {
        const errorsList = error.response.data
        const keys = Object.keys(errorsList)

        keys.forEach((i) => {
          showToast(`${i}: ${errorsList[i][0]}`, 'warning')
          errors.value[i] = errorsList[i][0]
        })
        isLoadingFalse()
      })
  } else {
    apiClient
      .post('api/students/create/', studentData)
      .then((response) => {
        showToast(response.data.message, 'success')
        resetStudent()
        errors.value = {}
        fetchStudents()
      })
      .catch((error) => {
        const errorsList = error.response.data.errors
        const keys = Object.keys(errorsList)

        keys.forEach((i) => {
          showToast(`${i}: ${errorsList[i][0]}`, 'warning')
          errors.value[i] = errorsList[i][0]
        })
        isLoadingFalse()
      })
  }
}

const studentData = (student) => {
  studentTableRow.value = student
  paymentFormData.value.student = student.id
  paymentModalRef.value.openModal()
}

const assignCourse = (student) => {
  fetchCourses()
  studentTableRow.value = student
  assignCourseModalRef.value.openModal()
  courseAssignFormData.value.student = student.id
}

const getStudent = (studentId) => {
  isLoading.value = true
  apiClient
    .get(`/students/${studentId}/`)
    .then((response) => {
      student.value = { ...response.data }
      isLoading.value = false
      visible.value = true
    })
    .catch((error) => {})
}

const getStudenDataForm = () => {
  apiClient.get('/students/data-form/').then((response) => {
    batches.value = response.data.batches
    academicYears.value = response.data.academic_years
    homeTowns.value = response.data.home_towns
    colleges.value = response.data.colleges
  })
}

const courseAssign = () => {
  apiClient
    .post('/courses/course-assign/', courseAssignFormData.value)
    .then((response) => {
      showToast(response.data.message, 'success')
      fetchStudents()
      courseAssignFormData.value = { ...blankAssignCourseForm.value }
    })
    .catch((error) => {
      const errorData = error.response.data
      // this.showToast(errorData.message, 'error')
    })
}

const createPayment = () => {
  apiClient
    .post('/courses/payment/', paymentFormData.value)
    .then((response) => {
      paymentFormData.value = { ...blankPaymentForm.value }
      showToast(response.data.message, 'success')
      fetchStudents()
    })
    .catch((error) => {
      const errorData = error.response.data
    })
}

//get payment history

const fetchPayments = (student) => {
  studentTableRow.value = student
  apiClient
    .get(`/courses/student-payment-list/${student.id}/`)
    .then((response) => {
      studentPaymentList.value = response.data
      paymentHistoryModalRef.value.openModal()
    })
    .catch((error) => {
      const errorData = error.response.data
      let msg = ''
      // for (const [key, value] of Object.entries(errorData.errors)) {
      //   msg += `${key}: ${value} <br>`
      // }

      // this.showToast(msg, 'error')
    })
}

onMounted(() => {
  fetchStudents()
  getStudenDataForm()
})

// watch(pageSize, (newPageSize) => {
//   fetchStudents()
// })
watch(query.value, (newQuery) => {
  fetchStudents()
})

const paymentHistoryModalRef = useTemplateRef('paymentHistoryModalRef')
const paymentModalRef = useTemplateRef('paymentModalRef')
const assignCourseModalRef = useTemplateRef('assignCourseModalRef')
</script>

<template>
  <b-overlay :show="isLoading">
    <!-- <div>{{ student }}</div> -->
    <b-collapse id="collapse-4" v-model="visible" class="mt-2 mb-5">
      <student-create-update
        v-model:student="student"
        :batches="batches"
        :academic-years="academicYears"
        :home-towns="homeTowns"
        :colleges="colleges"
        :errors="errors"
        @create-student="createStudent"
        @reset-form="resetForm"
      />
    </b-collapse>
    <div class="row g-3">
      <div class="col-md-2">
        <select @change="fetchStudents()" v-model="filterBy" class="form-select">
          <option value="">Filter By</option>
          <option :value="filter.id" v-for="filter in filters" :key="filter.id">
            {{ filter.value }}
          </option>
        </select>
      </div>
      <div class="col-md-2">
        <select @change="fetchStudents()" v-model="sortBy" class="form-select">
          <option value="" selected>ASC</option>
          <option value="-">DESC</option>
        </select>
      </div>
      <div class="col-md-3">
        <select
          @change="fetchStudents()"
          v-model="batchBy"
          class="form-select"
          name="course"
          id="student-batch"
        >
          <option value="">All Batch</option>
          <option v-for="batch in batches" :key="batch.id" :value="batch.id">
            {{ batch.title }}
          </option>
        </select>
      </div>
      <div class="col-md-2">
        <input
          placeholder="Search..."
          type="input"
          v-model="q"
          class="form-control input-sm"
          @input="fetchStudents()"
        />
      </div>
      <div class="col-auto ms-auto">
        <b-button
          variant="primary"
          size="sm"
          :class="visible ? null : 'collapsed'"
          :aria-expanded="visible ? 'true' : 'false'"
          aria-controls="collapse-2"
          @click="visible = !visible"
        >
          Add Student
        </b-button>
      </div>
    </div>

    <div>
      <!--Start Student Table-->
      <div class="row mt-5">
        <div>
          <table class="table table-light table-striped table-hover table-bordered table-sm">
            <thead class="table-dark">
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Student Info</th>
                <th scope="col">Batch</th>
                <th scope="col">HSC Batch</th>
                <th scope="col">Due Amount</th>
                <th scope="col">Paid This Month</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(i, index) in students.results"
                :key="i.id"
                :class="i.paid_current_month ? 'table-success' : 'table-danger'"
              >
                <td scope="row">{{ index + 1 }}</td>

                <td>
                  <small>{{ i.name }}</small> <br />
                  <small>Phone: {{ i.phone }}</small> <br />
                  <small>ID# {{ i.student_roll }}</small> <br />
                </td>
                <td>
                  <small class="">{{ i.batch__name }}</small> <br />
                  <small>{{ i.batch__start_time }} - {{ i.batch__end_time }}</small>
                </td>
                <td>{{ i.hsc_batch__year }} - {{ i.hsc_batch__year + 1 }}</td>
                <td>{{ i.due_amount ? i.due_amount : 0 }}</td>
                <td>
                  <span
                    class="me-2"
                    v-html="
                      i.paid_current_month
                        ? `<span class='badge text-bg-primary'>Yes</span>`
                        : `<span class='badge text-bg-danger'>No</span>`
                    "
                  ></span>

                  <span class="badge ml-3 text-bg-info" @click="fetchPayments(i)"
                    >Payment History</span
                  ><br />
                  <small>{{ i.latest_payment }}</small>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                      type="button"
                      class="btn btn-primary dropdown-toggle btn-sm"
                      data-bs-toggle="dropdown"
                      aria-expanded="false"
                    >
                      Action
                    </button>
                    <ul class="dropdown-menu">
                      <li>
                        <a href="#" class="dropdown-item" @click="studentData(i)">Make Payment</a>
                      </li>
                      <hr />
                      <li>
                        <a href="#" class="dropdown-item" @click="assignCourse(i)">Assign Course</a>
                      </li>
                      <hr />
                      <li>
                        <a href="#" class="dropdown-item">Assign Material</a>
                      </li>
                      <hr />
                      <li>
                        <a href="#" class="dropdown-item" @click="getStudent(i.id)">Edit</a>
                      </li>
                    </ul>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="row mt-3">
          <div class="col-md-10">
            <nav aria-label="Page navigation example">
              <ul class="pagination">
                <li class="page-item" :class="{ disabled: !students.previous }">
                  <a class="page-link" href="#" @click.prevent="fetchStudents(students.previous)"
                    >Previous</a
                  >
                </li>
                <li class="page-item">
                  <a
                    class="page-link"
                    href="#"
                    :class="{ disabled: !students.next }"
                    @click.prevent="fetchStudents(students.next)"
                    >Next</a
                  >
                </li>
              </ul>
            </nav>
          </div>

          <div class="col-md-2">
            <select v-model="query.pageSize" class="form-select" aria-label="Page Size">
              <option :value="i" v-for="i in pageSizes" :key="i">{{ i }}</option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <!-- modal payment history -->
    <payment-history-modal
      ref="paymentHistoryModalRef"
      :student-payment-list="studentPaymentList"
      :student-table-row="studentTableRow"
    />

    <payment-modal
      ref="paymentModalRef"
      v-model:payment-form-data="paymentFormData"
      :student-table-row="studentTableRow"
      @create-payment="createPayment"
    />
    <assign-course-modal
      ref="assignCourseModalRef"
      v-model:courseAssignFormData="courseAssignFormData"
      :student-table-row="studentTableRow"
      :courses="courses"
      @course-assign="courseAssign"
    />
  </b-overlay>
</template>

<style scoped></style>

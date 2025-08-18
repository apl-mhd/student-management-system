const StudentCreateForm = {

  props:{
    nameList:{
      type: Array,
      required: false,
    }
  },
  methods:{
     submit(){
            this.$emit('someEvent', {name: 'apel', id:1})
          }
  },
  data() {
    return {
      count: 0,
    };
  },
  template: `
    <div>
      

      <p v-for="name, index in nameList" :key="index">{{name}} <button @click="$emit('delName', index)">Del</button> </p>
      <hr/>
      <form class="row gx-3 gy-4" >
            <div class="col-6">
                <label for="name" class="form-label">Name *</label>
                <input
                  type="text"
                  name="name"
                  placeholder="Mahmud"
                  class="form-control"
                  id="name"
                />
              </div>
            <div class="col-6">
              <label for="phone" class="form-label">Phone *</label>
              <input
                type="text"
                name="phone"
                placeholder="015-xx-xx-xx-xx"
                class="form-control"
                id="phone"
              />
            </div>
            <div class="col-6">
              <label for="ParentsPhone" class="form-label">Gurdian Phone</label>
              <input
                type="text"
                name="gurdian_phone"
                placeholder="017-xx-xx-xx-xx"
                class="form-control"
                id="ParentsPhone"
              />
            </div>
            <div class="col-6">
              <label for="email" class="form-label">Email</label>
              <input
                type="email"
                placeholder="contact@mail.com"
                name="email"
                class="form-control"
                id="email"
              />
            </div>
            <div class="col-6">
              <label for="gender" class="form-label">Gender *</label>
              <select
                class="form-select"
                name="gender"
                id="gender"
              >
                <option disabled value="null">Select Gender</option>
                <option value="M">Male</option>
                <option value="F">Female</option>
              </select>
            </div>
            <div class="col-6">
              <label for="studetn-course" class="form-label">Batch</label>
              <select
                class="form-select"
                name="course"
                id="studetn-batch"
              >
                <option disabled value="null">Select Batch</option>
                
              </select>
            </div>
            <div class="col-6">
              <label for="academicYear" class="form-label">HSC Batch *</label>
              <select
                class="form-select"
                name="hsc_batch"
                id="academicYear"
              >
                <option disabled value="null">Select Batch</option>
                
              </select>
            </div>
            <div class="col-6">
              <label for="location" class="form-label">Home Town</label>
              <select
                class="form-select"
                name="home_town"
                id="location"
              >
                <option disabled value="null">Select Home Town</option>
                
              </select>
            </div>
            <div class="col-6">
              <label for="college" class="form-label">College</label>
              <select
                class="form-select"
                name="college"
                id="college"
              >
                <option disabled value="null">Select College</option>
               
              </select>
            </div>
            <div class="col-12 d-flex justify-content-between">
              <button type="submit" class="btn btn-primary">

              </button>
              <button  type="reset" class="btn btn-danger me-2">
                Reset
              </button>
            </div>
        </form>

    </div>`
};

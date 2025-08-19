<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import StudentView from './views/student/StudentView.vue'
</script>

<template>
  <div class="wrapper">
    <div class="sidebar">
      <div class="sidebar_top">
        <div class="user_logo">
          <img src="" alt="" />
        </div>
        <div class="menubar_toggle">
          <i id="toogle" class="bx bx-menu"></i>
        </div>
      </div>
      <ul>
        <!-- <li class="nav_links">
          <router-link to="/"><i class="bx bxs-home"></i> <span>Home</span></router-link>
        </li> -->
        <li class="nav_links">
          <router-link to="/students"><i class="bx bxs-home"></i> <span>Student</span></router-link>
        </li>

        <li class="nav_links">
          <a href="#"><i class="bx bxs-cog"></i><span>Service</span></a>
        </li>
        <li class="sub_menu_parent active nav_links">
          <a class="sub_menu_collapse" href="#"><i class="bx bxs-group"></i><span>Student</span></a>
          <ul class="sub_menu collapse_toggle">
            <li><a href="#">All Student</a></li>
            <li><a href="#">Create Student</a></li>
            <li><a href="#">Payment</a></li>
            <li><a href="#">Report</a></li>
          </ul>
        </li>

        <li class="nav_links">
          <a href="#"><i class="bx bxs-home"></i><span>Withdraw</span></a>
        </li>
        <li class="nav_links">
          <a href="#"><i class="bx bxs-home"></i><span>About</span></a>
        </li>
      </ul>
    </div>

    <div class="main">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

:root {
  --base-clr: #11121a;
  --line-clr: #42434a;
  --hover-clr: #222533;
  --text-clr: #e6e6ef;
  --accent-clr: #5e63ff;
  --secondary-text-clr: #b0b3c1;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Poppins', Arial, Helvetica, sans-serif;
  line-height: 1.5em;
}

a {
  text-decoration: none;
}

ul {
  list-style: none;
}

::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #888;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}

/*
 */

img {
  height: 100%;
  width: 100%;
}

.wrapper {
  min-height: 100vh;
  display: grid;
  grid-template-rows: auto 1fr;
}

.sidebar {
  width: 250px;
  min-height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  background: var(--base-clr);
  position: fixed;
  top: 0;
  left: 0;
  transition: 0.3s all;
}

.sidebar .sidebar_top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.6rem 1rem;
}

.sidebar .user_logo {
  height: 2rem;
  width: 2rem;
}

.sidebar .menubar_toggle {
  cursor: pointer;
  color: #fff;
}

.sidebar li {
  margin: 0.5rem 0;
  /* display: flex;
    align-items: center; */
  cursor: pointer;
}

.sidebar li a {
  width: 100%;
  border-radius: 0.5rem;
  display: inline-block;
  padding: 0.3rem 1rem;
  color: #fff;
  font-size: 0.8rem;
  font-weight: bold;
}

.sidebar li a:hover {
  background: gray;
  transition: 0.3s all ease-in-out;
}

.sidebar li i {
  margin-right: 1.6rem;
}

.sidebar li a {
  color: #fff;
  margin-right: 10px;
}

.sub_menu {
  max-height: 500px;
  transition: all 0.3s ease-out;
}

.collapse_toggle {
  max-height: 0;
  overflow: hidden;
  transition: all 0.3s ease-out;
}

.active {
  /* background: gray; */
}

.main {
  width: calc(100% - 250px);
  overflow: hidden;
  margin-left: 250px;
  transition: 0.3s all ease-in-out;
  padding: 1rem;
}

.sidebar_toogle {
  width: 100px;
  transition: 0.3s all;
}

span {
  /* display: none; */
}

.sidebar_toogle span {
  display: none;
}

.sidebar_toogle + .main {
  width: calc(100% - 100px);
  margin-left: 100px;
  transition: 0.3s all ease-in-out;
}

span.history {
  font-weight: normal;
  text-decoration: underline;
  cursor: pointer;
  padding: 5px 2px;
}
span.history:hover {
}

/* main section */
</style>

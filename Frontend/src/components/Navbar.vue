<template>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="collapse navbar-collapse">
    <ul class="navbar-nav mr-auto">
      <li class="navbar-brand">
        <img src="../assets/logo-social-sq.png" alt="Logo do site" height="60"/>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#" style="padding-top: 25px">Home</a>
      </li>
      <li class="nav-item text-right">
        <form class="form-inline my-2 my-lg-0" style="padding-top: 20px">
          <input class="form-control mr-sm-2" placeholder="Pesquisar por serviço" v-model="search" @keyup="updateSearch">
        </form>
    </li>
    </ul>
  </div>
</nav>
</template>
<script>
export default {
  name: "Navbar",
  components: {},
  data() {
    return {
      search: "",
    };
  },
  methods: {
    updateSearch: function () {
      this.$emit("inputData", this.search);
    },
  },
};
</script>

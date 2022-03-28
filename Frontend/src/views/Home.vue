<template>
<div>
  <Navbar @inputData="updateSearch" />

  <div class="container">    
    <div class="row">
      <div class="col-sm-3 servico-card" v-for="servico in filteredServicos" :key="servico.id">
        <div class="panel panel-primary">
          <div class="panel-heading card-title">{{ servico.nome }}</div>
          <div class="panel-body">
            <img :src= "servico.link_imagem" :alt="servico.nome" class="img-responsive" width="100%">
          </div>
        </div>
        <div class="card-button">
          <b-btn :id="servico.id" type="button" variant="primary">Ver mais</b-btn>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    Navbar,
  },
  data() {
    return {
      search: "",
      servicos: [],
    };
  },
  async created() {
    await axios
      .get("http://127.0.0.1:8000/api/services")
      .then((response) => (this.servicos = response.data))
      .catch((error) => console.log(error));
  },
  computed: {
    filteredServicos: function () {
      return this.servicos.filter((servicos) => {
        return servicos.nome.toLowerCase().match(this.search.toLowerCase()) !== null;
      });
    },

    searchServicos() {
      return this.$refs.search.search_return();
    },
    
  },
  
  methods:{
    updateSearch(data){
      this.search = data;
    },
  }
};
</script>

<style>
.row {
  justify-content: center;
}

.servico-card {
  background-color: #E7E9EB;
  margin: 1em .5em .5em .5em;
}

.card-title {
  font-size: 1.5em;
}

.card-button {
  padding-top: 1em;
  padding-bottom: .5em;
  
}
</style>


<template>
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Listado de libros</h2>

        <div class="col-md-12">
          <b-table striped hover :items="books" :fields="fields"> </b-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    data(){
        return {
            fields:[
                { key: 'title', label: 'Titulos'},
                { key: 'decription',label:'Descripciòn'},
                { key: 'year', label:'año'},
                { key: ' front_page', label:'Portada'},
                { key: 'action', label:'acciòn'},
                
            ],
            books:[]
        }
    },
    methods:{
        getBooks(){
            const path= 'http://localhost:8000/api/v1.0/book/'
            axios.get(path).then((response) => {
                this.books = response.data

            })
            .catch((error)=>{
                console.log("Error")
            })
        }
    },
    created(){
        this.getBooks()
    }

}
</script>

<style lang="css" scoped>
</style>
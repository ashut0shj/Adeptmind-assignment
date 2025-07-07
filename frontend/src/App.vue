<template>
  <div class="header">
    <span>CROMA HEADER</span>
  </div>
  <div>
    <h1>Croma Televisions & Accessories - Product Cards</h1>
    <div class="product-grid">
      <div> TODO: Implement product cards here. Feel free to create a Product.vue component </div>
      <div> Add css in the style section below to match the product grid layout on croma.com</div>
      <div> Use grid layout css if possible.</div>
    </div>
  </div>  
</template>

<script>
export default {  
  data() {
    return {
      products: [] // This will hold the products fetched from the backend
    }
  },
  mounted() {
    // Fetch the products from the backend service using fetch API
    // Store the products in the products data property created above
    fetch('TODO: URL')
      .then(res => res.json())
      .then(data => {
        // TODO
      })
  }
}
</script>

<style>
.header {
  background-color: #000;
  padding: 20px;
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  span {
    color: #fff;
  }
}
/*  TODO: Product card styles go here */
</style>




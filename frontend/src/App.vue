<template>
  <div class="header">
    <span>CROMA HEADER</span>
  </div>
  <div>
    <h1>Croma Televisions & Accessories - Product Cards</h1>
    <div class="product-grid">
      <Product v-for="product in products" :key="product.product_id" :product="product" />
    </div>
  </div>  
</template>

<script>
import Product from './Product.vue'

export default {  
  components: {
    Product
  },
  data() {
    return {
      products: []
    }
  },
  mounted() {
    fetch('http://localhost:5000/products')
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          this.products = data.products;
        }
      })
      .catch(err => {
        console.error('Failed to fetch products:', err);
      });
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
}
.header span {
  color: #fff;
}
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 24px;
  margin: 32px 0;
}
</style>




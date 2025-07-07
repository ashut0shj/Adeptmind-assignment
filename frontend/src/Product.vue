<template>
  <div class="product-card">
    <a :href="product.link" target="_blank" class="product-title">{{ product.title }}</a>
    <div class="product-prices">
      <span class="new-price">{{ product.price }}</span>
      <span v-if="product.old_price" class="old-price">{{ product.old_price }}</span>
      <span v-if="product.discount" class="discount">{{ product.discount }}</span>
    </div>
    <div v-if="product.tags && product.tags.length" class="product-tags">
      <span v-for="tag in product.tags" :key="tag" class="tag">{{ tag }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Product',
  props: {
    product: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.product-card {
  background: #fff;
  border: 1px solid #eee;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  transition: box-shadow 0.2s;
}
.product-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
.product-title {
  font-size: 18px;
  font-weight: 600;
  color: #0078d7;
  text-decoration: none;
  margin-bottom: 10px;
}
.product-prices {
  margin-bottom: 10px;
}
.new-price {
  font-size: 20px;
  font-weight: bold;
  color: #222;
  margin-right: 10px;
}
.old-price {
  font-size: 16px;
  color: #888;
  text-decoration: line-through;
  margin-right: 10px;
}
.discount {
  font-size: 15px;
  color: #d32f2f;
  font-weight: 500;
}
.product-tags {
  margin-top: 8px;
}
.tag {
  display: inline-block;
  background: #f0f0f0;
  color: #333;
  border-radius: 6px;
  padding: 2px 8px;
  font-size: 13px;
  margin-right: 6px;
  margin-bottom: 4px;
}
</style> 
<template>
  <div class="product-card">
    <div class="product-content">
      <a :href="product.link" target="_blank" class="product-title">{{ product.title }}</a>
      <div class="product-prices">
        <span class="new-price">{{ product.price }}</span>
        <span v-if="product.old_price" class="old-price">{{ product.old_price }}</span>
      </div>
      <div v-if="product.discount" class="discount-badge">{{ product.discount }}</div>
      <div v-if="product.tags && product.tags.length" class="product-tags">
        <span v-for="tag in product.tags" :key="tag" class="tag">{{ tag }}</span>
      </div>
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
  background: #ffffff;
  border:2px solid #e5e7eb;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.product-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
  border-color: #d1d5db;
}

.product-content {
  padding: 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.product-title {
  font-size: 16px;
  font-weight: 500;
  color: #1f2937;
  text-decoration: none;
  line-height: 1.4;
  margin-bottom: 16px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  transition: color 0.2s ease;
}

.product-title:hover {
  color: #2563eb;
}

.product-prices {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.new-price {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
}

.old-price {
  font-size: 16px;
  color: #9ca3af;
  text-decoration: line-through;
}

.discount-badge {
  background: #dc2626;
  color: white;
  font-size: 12px;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 6px;
  display: inline-block;
  margin-bottom: 16px;
  align-self: flex-start;
}

.product-tags {
  margin-top: auto;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  background: #f3f4f6;
  color: #374151;
  font-size: 11px;
  font-weight: 500;
  padding: 4px 10px;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
}
</style> 
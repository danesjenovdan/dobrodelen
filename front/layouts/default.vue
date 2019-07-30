<template>
  <div class="container">
    <div class="page">
      <page-header />
      <nuxt />
    </div>
  </div>
</template>

<script>
import PageHeader from '~/components/PageHeader.vue';

export default {
  components: {
    PageHeader,
  },
};
</script>

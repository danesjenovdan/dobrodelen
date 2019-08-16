<template>
  <div class="container-fluid">
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
  watch: {
    $route() {
      this.$nuxt.$emit('toggle-menu', false);
    },
  },
};
</script>

<style lang="scss" scoped>
.container-fluid {
  padding-left: 3.5rem;
  padding-right: 3.5rem;
  max-width: 1920px;

  @include media-breakpoint-down(sm) {
    padding: 0 1rem;
  }
}
</style>

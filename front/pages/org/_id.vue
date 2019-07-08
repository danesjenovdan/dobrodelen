<template>
  <div class="container">
    <h1>Organization: {{ organization.name }}</h1>
    <p>{{ organization.description }}</p>
    <span v-for="i in 5" :key="i">
      <span v-if="organization.stars >= i">⭐</span>
      <span v-else>⚪</span>
    </span>
  </div>
</template>

<script>
export default {
  validate({ params }) {
    return /^\d+$/.test(params.id);
  },
  async asyncData({ $axios, params }) {
    const orgResp = await $axios.$get(`http://127.0.0.1:8000/api/organizations/${params.id}`);
    return {
      organization: orgResp,
    };
  },
};
</script>

<style lang="scss" scoped>
.container {
  margin: 20px auto 0;
  max-width: 900px;
}
</style>

<template>
  <div class="container">
    <h1>Organization: {{ organization.name }}</h1>
    <p>{{ organization.description }}</p>
    <span v-for="i in 5" :key="i">
      <span v-if="organization.stars >= i">⭐</span>
      <span v-else>⚪</span>
    </span>
    <br />
    <img
      v-if="organization.cover_photo"
      :src="`http://127.0.0.1:8000${organization.cover_photo.url}`"
      :alt="`image ${organization.cover_photo.width}x${organization.cover_photo.height}`"
    />
  </div>
</template>

<script>
export default {
  validate({ params }) {
    return /^\d+$/.test(params.id);
  },
  async asyncData({ $axios, params, query }) {
    const editKey = query.edit_key ? `?edit_key=${query.edit_key}` : '';
    const orgResp = await $axios.$get(
      `http://127.0.0.1:8000/api/organizations/${params.id}/${editKey}`,
    );
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

<template>
  <div class="container">
    <h1>Organizations:</h1>
    <organization-list :organizations="organizations" />
    <nuxt-link :to="{ name: 'org-add' }" class="btn">add new org</nuxt-link>
  </div>
</template>

<script>
import OrganizationList from '~/components/OrganizationList';

export default {
  components: {
    OrganizationList,
  },
  async asyncData({ $axios }) {
    const orgsResp = await $axios.$get('http://127.0.0.1:8000/api/organizations/');
    return {
      organizations: orgsResp.results,
    };
  },
};
</script>

<style lang="scss" scoped>
.container {
  margin: 20px auto 0;
  max-width: 900px;
}

.btn {
  display: inline-block;
  background: green;
  padding: 0.4rem 0.7rem;
  margin: 2rem 0;
  color: white;
  border-radius: 6px;
  text-decoration: none;

  &:hover {
    background: lighten(green, 5%);
  }
}
</style>

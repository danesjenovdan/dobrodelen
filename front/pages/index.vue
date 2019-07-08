<template>
  <div class="container">
    <h1>Organizations:</h1>
    <organization-list :organizations="organizations" />
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
</style>

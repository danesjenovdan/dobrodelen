<template>
  <div class="content">
    <intro-text icon="heart" />
    <organization-list
      :organizations="organizations"
      :sort-query="orgSortQuery"
      :search-query="orgSearchQuery"
      @change="onOrgListChange"
    />
  </div>
</template>

<script>
import IntroText from '~/components/IntroText.vue';
import OrganizationList from '~/components/OrganizationList.vue';

export default {
  components: {
    IntroText,
    OrganizationList,
  },
  async asyncData({ $axios, query }) {
    const orgSortQuery = query.sort || undefined;
    const orgSearchQuery = query.q || undefined;
    const orgsResp = await $axios.$get('/api/organizations/');
    return {
      organizations: orgsResp.results,
      orgSortQuery,
      orgSearchQuery,
    };
  },
  head() {
    return {
      title: 'Организации',
    };
  },
  methods: {
    onOrgListChange(changes) {
      const query = {};
      if (changes.sort) {
        query.sort = changes.sort;
      }
      if (changes.search) {
        query.q = changes.search;
      }
      this.$router.replace({
        query,
      });
    },
  },
};
</script>

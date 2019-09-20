<template>
  <div class="content">
    <intro-text lead="Doniraj pametno." icon="heart" />
    <organization-list
      :organizations="organizations"
      :sort-query="orgSortQuery"
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
    const orgsResp = await $axios.$get('/api/organizations/');
    return {
      organizations: orgsResp.results,
      orgSortQuery,
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
  head() {
    return {
      title: 'Organizacije',
    };
  },
};
</script>
<template>
  <div class="content">
    <intro-text lead="Doniraj pametno." icon="heart" />
    <organization-list
      :organizations="organizations"
      :sort-query="orgSortQuery"
      :search-query="orgSearchQuery"
      :search-criteria="orgSearchCriteria"
      @change="onOrgListChange"
    />
  </div>
</template>

<script>
import axios from 'axios';
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
    const orgSearchCriteria = query.criteria || undefined;
    const url = orgSearchCriteria
      ? `/api/organizations-filtered-criteria/?filter_keys=${orgSearchCriteria}`
      : '/api/organizations/';
    const orgsResp = await $axios.$get(url);
    return {
      apiBaseUrl: process.env.API_BASE_URL,
      organizations: orgsResp.results,
      orgSortQuery,
      orgSearchQuery,
      orgSearchCriteria,
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
      if (changes.criteria) {
        query.criteria = changes.criteria.join(',');
        this.fetchOrganizationsFilteredCriteria(query.criteria);
      }
      this.$router.replace({
        query,
      });
    },
    async fetchOrganizationsFilteredCriteria(criteria) {
      try {
        this.loading = true;
        const response = await axios.get(
          `${this.apiBaseUrl}/api/organizations-filtered-criteria/?filter_keys=${criteria}`,
        );
        this.organizations = response.data.results || [];
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
  },
  head() {
    return {
      title: 'Organizacije',
    };
  },
};
</script>

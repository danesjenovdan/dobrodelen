<template>
  <Head>
    <Title>Organizacije</Title>
  </Head>
  <div class="content">
    <div v-if="orgDataError">
      <h2 style="text-align: center; color: red">{{ orgDataError }}</h2>
    </div>
    <template v-else>
      <intro-text
        v-if="orgDataPending"
        lead="Nalaganje ..."
        icon="heart"
        animate-icon
      />
      <template v-else>
        <intro-text lead="Doniraj pametno." icon="heart" />
        <organization-list
          :organizations="organizations"
          :sort-query="orgSortQuery"
          :search-query="orgSearchQuery"
          :search-criteria="orgSearchCriteria"
          @change="onOrgListChange"
        />
      </template>
    </template>
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
  async setup() {
    const config = useRuntimeConfig();
    const route = useRoute();

    const orgSortQuery = route.query.sort;
    const orgSearchQuery = route.query.q;
    const orgSearchCriteria = route.query.criteria;

    const {
      error: orgDataError,
      pending: orgDataPending,
      data: orgData,
    } = await useAsyncData(
      'organizations',
      async () => {
        const apiBase = process.server
          ? config.public.apiBaseServer
          : config.public.apiBase;
        const url = orgSearchCriteria
          ? `/api/organizations-filtered-criteria/?filter_keys=${orgSearchCriteria}`
          : '/api/organizations/';
        return $fetch(`${apiBase}${url}`);
      },
      {
        lazy: true,
        server: false,
      },
    );

    return {
      apiBaseUrl: config.public.apiBase,
      orgDataPending,
      orgDataError,
      orgData,
      orgSortQuery,
      orgSearchQuery,
      orgSearchCriteria,
    };
  },
  computed: {
    organizations() {
      return this.orgData?.results || [];
    },
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
        const response = await $fetch(
          `${this.apiBaseUrl}/api/organizations-filtered-criteria/?filter_keys=${criteria}`,
        );
        this.organizations = response.results || [];
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

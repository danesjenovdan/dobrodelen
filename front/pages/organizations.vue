<template>
  <div class="content">
    <intro-text />
    <organization-list :organizations="organizations" />
  </div>
</template>

<script>
import OrganizationList from '~/components/OrganizationList.vue';
import IntroText from '~/components/IntroText.vue';

export default {
  components: {
    IntroText,
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

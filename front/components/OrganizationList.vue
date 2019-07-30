<template>
  <div class="organization-list">
    <form class="form-inline justify-content-center" action="#" method="get" @submit.prevent>
      <input class="form-control mr-2" type="text" />
      <input class="form-control" type="submit" />
    </form>
    <ul>
      <li v-for="org in organizations" :key="org.id">
        <nuxt-link :to="{ name: 'org-id', params: { id: org.id } }">
          <span>{{ org.name }} ({{ org.stars }} stars)</span>
        </nuxt-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    organizations: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.organization-list {
  background: rgba(orange, 0.25);

  .form-inline {
    padding: 5rem 0;
  }
}
</style>

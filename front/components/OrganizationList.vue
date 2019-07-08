<template>
  <ul>
    <li v-for="org in organizations" :key="org.id">
      <nuxt-link :to="{ name: 'org-id', params: { id: org.id } }">
        <span>{{ org.name }} ({{ org.stars }} stars)</span>
      </nuxt-link>
    </li>
  </ul>
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

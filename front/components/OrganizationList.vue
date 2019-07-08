<template>
  <ul>
    <li v-for="org in organizations" :key="org.id">{{ org.name }} ({{ org.stars }} stars)</li>
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

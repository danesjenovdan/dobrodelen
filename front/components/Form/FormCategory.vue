<template>
  <fieldset>
    <legend>{{ title }}</legend>
    <small v-if="note" class="form-text">
      <span>* {{ note }}</span>
    </small>
    <slot />
  </fieldset>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    note: {
      type: String,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped>
fieldset {
  legend {
    font-size: 1.85rem;
    font-weight: 300;
    letter-spacing: 0.2em;
    margin-bottom: 1.5rem;

    + small {
      margin-top: -1.5rem;
      margin-bottom: 1.5rem;
      font-size: 0.9375rem;
    }
  }
}
</style>

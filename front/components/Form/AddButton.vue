<template>
  <div class="form-group">
    <button
      :class="['btn', 'btn-outline-primary', 'btn-form', 'icon', `icon-${icon}`]"
      v-text="text"
    />
  </div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
    icon: {
      type: String,
      default: 'add',
    },
  },
};
</script>

<style lang="scss" scoped>
.form-group {
  margin-bottom: 3rem;

  .btn-form {
    border-width: 2px;
    border-radius: 0.41em;
    font-weight: 700;
    font-size: 1.5rem;
    color: $body-color;
    letter-spacing: 0.2em;
    width: auto;
    height: 5rem;
    padding: 1rem 1.5rem 1rem 5rem;
    background-position: left center;
    background-size: 5rem 45%;
  }
}
</style>

<template>
  <span class="striped-text-shadow" :data-text="text" v-text="text" />
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.striped-text-shadow {
  display: inline-block;
  position: relative;
  z-index: 0;
  padding-right: 0.06em;
  color: inherit;

  &::after {
    content: attr(data-text);
    background-image: linear-gradient(
      0deg,
      transparent 40%,
      $primary 40%,
      $primary 50%,
      transparent 50%,
      transparent 90%,
      $primary 90%,
      $primary 100%
    );
    background-size: 10px 10px;
    background-clip: text;
    color: transparent;
    display: inline-block;
    position: absolute;
    left: 0.06em;
    top: 0;
    z-index: -1;
    transition: opacity 2s linear;

    @at-root {
      body.desaturated & {
        opacity: 0;
      }
    }
  }
}
</style>

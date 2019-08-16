<template>
  <div class="form-stages">
    <div
      v-for="(stage, i) in stages"
      :key="`stage-${i}`"
      :class="['stage', { active: i === active }]"
      @click="$emit('change', i)"
      v-text="stage.label"
    />
  </div>
</template>

<script>
export default {
  props: {
    stages: {
      type: Array,
      required: true,
    },
    active: {
      type: Number,
      default: 0,
    },
  },
};
</script>

<style lang="scss" scoped>
.form-stages {
  display: flex;
  margin-left: -0.5rem;
  margin-right: -0.5rem;

  @include media-breakpoint-down(sm) {
    margin-left: -0.75rem;
    margin-right: -0.75rem;
  }

  .stage {
    flex: 1;
    position: relative;
    text-align: center;
    padding-bottom: 1.5rem;
    font-size: 0.9375rem;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: flex-end;

    @include media-breakpoint-down(sm) {
      font-size: 0.75rem;
      padding-bottom: 1rem;
    }

    &::after {
      content: '';
      display: block;
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      height: 0.75rem;
      background: $blue;
      margin: 0 0.5rem;
      opacity: 0.3;

      @include media-breakpoint-down(sm) {
        margin: 0 0.25rem;
      }
    }

    &.active {
      color: $blue;
      cursor: default;

      &::after {
        opacity: 1;
      }
    }
  }
}
</style>

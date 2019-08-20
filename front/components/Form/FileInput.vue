<template>
  <div class="form-group">
    <div class="custom-file">
      <input :id="`${name}__id`" :name="name" type="file" class="custom-file-input" />
      <label class="custom-file-label icon icon-upload" :for="`${name}__id`">
        <span>{{ label }}</span>
      </label>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      default: 'Naloži datoteko',
    },
  },
};
</script>

<style lang="scss" scoped>
.form-group {
  margin-bottom: 3rem;

  @include media-breakpoint-down(sm) {
    margin-bottom: 1.5rem;
  }

  .custom-file {
    width: auto;

    &,
    .custom-file-input,
    .custom-file-label {
      height: 5rem;

      @include media-breakpoint-down(sm) {
        height: 3.5rem;
      }
    }

    .custom-file-input {
      position: absolute;
      top: 0;
      left: 0;
      bottom: 0;
      right: 0;
      cursor: pointer;
    }

    .custom-file-label {
      position: relative;
      display: flex;
      align-items: center;
      width: 100%;
      margin: 0;
      border-width: 2px;
      border-radius: 0.41em;
      border-color: $blue;
      font-weight: 700;
      font-size: 1.5rem;
      color: $body-color;
      letter-spacing: 0.2em;
      padding: 1rem 1.5rem 1rem 5rem;
      background-position: left center;
      background-size: 5rem 45%;

      @include media-breakpoint-down(sm) {
        font-size: 1rem;
        height: 3.5rem;
        padding: 0 1.5rem 0 3.5rem;
        background-size: 3.5rem 45%;
      }

      &::after {
        display: none;
      }
    }

    .custom-file-input:hover ~ .custom-file-label {
      background-color: $blue;
    }
  }
}
</style>

<template>
  <div class="form-group">
    <div :class="['custom-file', { 'is-invalid': hasError }]">
      <input
        :id="`${name}__id`"
        :name="name"
        type="file"
        class="custom-file-input"
        @change="onFileChanged"
      />
      <label class="custom-file-label icon icon-upload" :for="`${name}__id`">
        <span>{{ label }}</span>
        <small>
          {{ fileName }}
        </small>
      </label>
    </div>
    <div v-if="hasError" class="invalid-feedback">* {{ errorMessage }}</div>
  </div>
</template>

<script>
import { last } from 'lodash';

export default {
  model: {
    prop: 'value',
    event: 'change',
  },
  props: {
    name: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      default: 'Naloži datoteko',
    },
    value: {
      type: Object,
      default: null,
    },
    hasError: {
      type: [Boolean, String],
      default: false,
    },
  },
  data() {
    const fileName =
      (this.value && this.value.file && this.value.file.name) ||
      (this.value && this.value.name) ||
      (this.value && this.value.url && last(this.value.url.split('/'))) ||
      null;
    return {
      fileName,
    };
  },
  computed: {
    errorMessage() {
      return typeof this.hasError === 'string' ? this.hasError : 'napaka pri vnosu';
    },
  },
  methods: {
    onFileChanged(event) {
      const file = event.target.files[0];
      if (file) {
        this.fileName = file.name;
        this.$emit('change', { file });
      }
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
    max-width: 100%;

    &,
    .custom-file-input,
    .custom-file-label {
      height: 5rem;

      @include media-breakpoint-down(sm) {
        height: 3.5rem;
      }
    }

    &.is-invalid {
      .custom-file-input,
      .custom-file-label {
        border-color: $red;
      }

      input:focus + .custom-file-label {
        box-shadow: 0 0 0 0.2rem rgba($red, 0.25);
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
      flex-direction: column;
      justify-content: center;
      width: 100%;
      margin: 0;
      border-width: 2px;
      border-radius: 0.41em;
      border-color: $blue;
      color: $body-color;
      padding: 0 1.5rem 0 5rem;
      background-position: left center;
      background-size: 5rem 45%;

      @include media-breakpoint-down(sm) {
        height: 3.5rem;
        padding: 0 1.5rem 0 3.5rem;
        background-size: 3.5rem 45%;
      }

      span {
        display: block;
        font-weight: 700;
        font-size: 1.5rem;
        // letter-spacing: 0.2em;

        @include media-breakpoint-down(sm) {
          font-size: 1rem;
        }
      }

      small {
        display: block;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }

      &::after {
        display: none;
      }
    }

    .custom-file-input:hover ~ .custom-file-label {
      background-color: $blue;
    }
  }

  .invalid-feedback {
    display: block;
    font-size: 0.9375rem;
    padding: 0 2rem;

    @include media-breakpoint-down(sm) {
      padding: 0 1.5rem;
    }
  }
}
</style>

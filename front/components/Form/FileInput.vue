<template>
  <div class="form-group">
    <div :class="['custom-file', { 'is-invalid': hasError }]">
      <input
        :id="`${name}__id`"
        ref="input"
        :name="name"
        type="file"
        class="custom-file-input"
        @change="onFileChanged"
      />
      <label class="custom-file-label" :for="`${name}__id`">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="10.2 1.025 79.9 97.975">
          <path
            d="M83.4 32.5H67.9c-1.2 0-2.2 1-2.2 2.2 0 1.2 1 2.2 2.2 2.2h15.5c1.2 0 2.2.9 2.2 2.1v53.5c0 1.1-1 2.1-2.2 2.1H16.9c-1.2 0-2.2-.9-2.2-2.1V39c0-1.1 1-2.1 2.2-2.1h15.5c1.2 0 2.2-1 2.2-2.2 0-1.2-1-2.2-2.2-2.2H16.9c-3.7 0-6.7 2.9-6.7 6.5v53.5c0 3.6 3 6.5 6.7 6.5h66.5c3.7 0 6.7-2.9 6.7-6.5V39c-.1-3.6-3-6.5-6.7-6.5zM36.2 18.6L47.9 6.8V73c0 1.2 1 2.2 2.2 2.2 1.2 0 2.2-1 2.2-2.2V6.7L64 18.5c.4.4 1 .7 1.6.7.6 0 1.1-.2 1.6-.6.9-.9.9-2.3 0-3.1L54.9 2.9C52.4.4 48 .4 45.4 2.9L33 15.4c-.9.9-.9 2.3 0 3.1.9.9 2.3.9 3.2.1z"
          />
        </svg>
        <div class="text">
          <span>{{ label }}</span>
          <small>
            {{ fileName }}
          </small>
        </div>
      </label>
      <button
        v-if="fileName"
        type="button"
        class="btn btn-link remove-file"
        @click="onFileChanged(null)"
      >
        <span>&times;</span> Odstrani
      </button>
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
      default: 'Naložite datoteko',
    },
    value: {
      type: [Object, String],
      default: null,
    },
    hasError: {
      type: [Boolean, String],
      default: false,
    },
  },
  data() {
    const filePath =
      (typeof this.value === 'string' && this.value) ||
      (this.value && this.value.file && this.value.file.name) ||
      (this.value && this.value.name) ||
      (this.value && this.value.url) ||
      null;
    const fileName = (filePath && decodeURIComponent(last(filePath.split('/')))) || null;
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
      if (event == null) {
        this.fileName = null;
        this.$refs.input.value = null;
        this.$emit('change', null);
        return;
      }
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
      flex-direction: row;
      align-items: center;
      width: 100%;
      margin: 0;
      border-width: 2px;
      border-radius: 0.41em;
      border-color: $blue;
      color: $body-color;
      padding: 0 1.5rem 0 0;

      @include media-breakpoint-down(sm) {
        height: 3.5rem;
      }

      svg {
        flex-shrink: 0;
        width: 5rem;
        height: 45%;
        float: left;
        fill: $primary;
        transition: fill 0.15s ease-in-out;
      }

      .text {
        overflow: hidden;

        span {
          display: block;
          font-weight: 700;
          font-size: 1.5rem;

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
      }

      &::after {
        display: none;
      }
    }

    .custom-file-input:active ~ .custom-file-label,
    .custom-file-input:hover ~ .custom-file-label {
      background-color: $blue;

      svg {
        fill: $body-color;
      }
    }

    .remove-file {
      display: flex;
      padding: 0;
      font-size: 1rem;
      line-height: 2rem;
      z-index: 1;

      &,
      &:hover {
        text-decoration: none;
      }

      span {
        font-size: 2rem;
        line-height: 2rem;
        margin-right: 0.5rem;
      }
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

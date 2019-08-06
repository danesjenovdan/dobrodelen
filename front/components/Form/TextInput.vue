<template>
  <div class="form-group">
    <div v-if="hasError" class="invalid-feedback">* {{ errorMessage }}</div>
    <input
      v-if="!multiline"
      :id="`${name}_id`"
      :name="name"
      type="text"
      :class="['form-control', { 'is-invalid': hasError }]"
      :placeholder="label"
      :value="value"
    />
    <textarea
      v-else
      :id="`${name}_id`"
      :name="name"
      :class="['form-control', { 'is-invalid': hasError }]"
      :placeholder="label"
      :value="value"
      rows="8"
    />
    <label v-if="label" :for="`${name}_id`">{{ label }}</label>
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
      default: null,
    },
    value: {
      type: String,
      default: null,
    },
    multiline: {
      type: Boolean,
      default: false,
    },
    hasError: {
      type: [Boolean, String],
      default: false,
    },
  },
  computed: {
    errorMessage() {
      return typeof this.hasError === 'string' ? this.hasError : 'napaka pri vnosu';
    },
  },
};
</script>

<style lang="scss" scoped>
.form-group {
  display: flex;
  flex-direction: column-reverse;
  overflow: hidden;
  margin-bottom: 3rem;

  .form-control {
    border: 0;
    background: rgba(#f6f2f0, 0.4);
    font-size: 1.85rem;
    font-weight: 300;
    padding: 1rem 2rem;
    padding: 1.5rem 2rem 0.25rem;
    height: 5rem;
    border-bottom: 2px solid rgba($blue, 0.3);

    &::placeholder {
      font-weight: 300;
      color: $body-color;
    }

    &,
    &:focus {
      outline: 0;
      box-shadow: none;
    }

    &:focus {
      border-bottom-color: $blue;
    }

    &.is-invalid {
      color: $red;
      border-bottom-color: rgba($red, 0.3);

      &:focus {
        border-bottom-color: $red;
      }
    }
  }

  textarea.form-control {
    height: auto;
    font-size: 1.5rem;
  }

  label {
    font-weight: 400;
    font-size: 0.9375rem;
    line-height: 1.1;
    margin-bottom: -1.1em;
    margin-left: 2rem;
    transform: translate(0.1rem, 0.75rem) scale(1);
    cursor: text;
    transition: all 0.2s;
  }

  .form-control::placeholder {
    opacity: 0;
  }

  .form-control:placeholder-shown + label {
    max-width: 80%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    cursor: text;
    font-weight: 300;
    transform-origin: left bottom;
    transform: translate(-0.075rem, 2.5rem) scale(1.97);
  }

  .form-control:not(:placeholder-shown) + label,
  .form-control:focus + label {
    font-weight: 400;
    transform: translate(0.1rem, 0.75rem) scale(1);
  }

  .invalid-feedback {
    display: block;
    font-size: 0.9375rem;
    padding: 0 2rem;
  }
}
</style>

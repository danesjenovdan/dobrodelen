<template>
  <div :class="['custom-control', `custom-${type}`]">
    <input
      :id="`${name}__${value}__id`"
      :type="type"
      :name="name"
      class="custom-control-input"
      :value="value"
      :checked="isChecked"
      @change="onChange"
    />
    <label
      :class="['custom-control-label', { 'has-custom-input': customInput }]"
      :for="`${name}__${value}__id`"
    >
      {{ label }}
      <input
        v-if="customInput"
        ref="customInput"
        class="form-control"
        :value="customInputValue"
        @input="onCustomChange"
      />
    </label>
  </div>
</template>

<script>
export default {
  model: {
    prop: 'checked',
    event: 'change',
  },
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
      type: [String, Number],
      default: null,
    },
    checked: {
      type: [Boolean, Array],
      default: false,
    },
    type: {
      type: String,
      default: 'radio',
      validator(value) {
        if (value === 'radio' || value === 'checkbox') {
          return true;
        }
        return false;
      },
    },
    customInput: {
      type: Boolean,
      default: false,
    },
    customInputValue: {
      type: String,
      default: null,
    },
  },
  computed: {
    isChecked() {
      if (Array.isArray(this.checked)) {
        return this.checked.filter((e) => e === this.value).length > 0;
      }
      if (this.type === 'radio') {
        return this.checked === this.value;
      }
      return this.checked;
    },
  },
  methods: {
    onChange(event) {
      let val = event.target.checked;
      if (val && this.customInput) {
        this.$refs.customInput.focus();
      }
      if (Array.isArray(this.checked)) {
        if (val) {
          val = this.checked.slice();
          val.push(this.value);
        } else {
          val = this.checked.filter((e) => e !== this.value);
        }
      } else if (this.type === 'radio') {
        val = this.value;
      }
      this.$emit('change', val);
    },
    onCustomChange(event) {
      if (event.target.value && !this.isChecked) {
        this.onChange({ target: { checked: true } });
      }
      if (!event.target.value && this.isChecked) {
        this.onChange({ target: { checked: false } });
      }
      this.$emit('custom-change', event.target.value);
    },
  },
};
</script>

<style lang="scss" scoped>
.custom-radio,
.custom-checkbox {
  padding-left: 2.5rem;

  .custom-control-label {
    font-size: 1.85rem;
    font-weight: 300;
    line-height: 1.2;
    min-height: 2rem;
    margin: 1.75rem 0;
    display: flex;
    align-items: center;

    @include media-breakpoint-down(sm) {
      font-size: 1.25rem;
      margin: 1.5rem 0;
    }

    &::before,
    &::after {
      width: 1.75rem;
      height: 1.75rem;
      top: 50%;
      left: -2.5rem;
      transform: translateY(-50%);
      cursor: pointer;
    }

    &::before {
      border-width: 2px;
    }

    &.has-custom-input {
      .form-control {
        margin-top: -1rem;
        margin-bottom: -1rem;
        margin-left: 1.5rem;
        border: 0;
        background: rgba(#f6f2f0, 0.4);
        font-size: 1.5rem;
        font-weight: 300;
        padding: 0.5rem 1.75rem;
        border-bottom: 2px solid rgba($blue, 0.3);
        height: 4rem;

        @include media-breakpoint-down(sm) {
          font-size: 1.25rem;
          padding-left: 1rem;
          margin-left: 1rem;
          height: 2.5rem;
        }

        &,
        &:focus {
          outline: 0;
          box-shadow: none;
        }

        &:focus {
          border-bottom-color: $blue;
        }
      }
    }
  }

  .custom-control-input ~ .custom-control-label::before {
    border-color: $blue;
  }

  // .custom-control-input:checked ~ .custom-control-label::before {
  //   background-color: #fff;
  // }

  // .custom-control-input:checked ~ .custom-control-label::after {
  //   background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-10 -10 20 20'%3e%3ccircle r='5.5' fill='%23#{str-slice(#{$blue}, 2)}'/%3e%3c/svg%3e");
  //   background-size: contain;
  //   background-position: center;
  // }
}

legend + .custom-control {
  margin-top: -1.5rem;
}

.custom-control:last-of-type {
  margin-bottom: 3rem;

  @include media-breakpoint-down(sm) {
    margin-bottom: 1.5rem;
  }
}
</style>

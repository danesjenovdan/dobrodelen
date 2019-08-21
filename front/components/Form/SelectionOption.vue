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
    <label class="custom-control-label" :for="`${name}__${value}__id`">{{ label }}</label>
  </div>
</template>

<!--

<fieldset>
  <div class="custom-control custom-radio">
    <input id="cr3" type="radio" name="cr" class="custom-control-input" />
    <label class="custom-control-label d-flex align-items-center" for="cr3">
      Drugo:
      <input class="form-control" />
    </label>
  </div>
</fieldset>
-->

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
  },
  computed: {
    isChecked() {
      if (Array.isArray(this.checked)) {
        return this.checked.filter((e) => e === this.value).length > 0;
      }
      return this.checked;
    },
  },
  methods: {
    onChange(event) {
      let val = event.target.checked;
      if (Array.isArray(this.checked)) {
        if (val) {
          val = this.checked.slice();
          val.push(this.value);
        } else {
          val = this.checked.filter((e) => e !== this.value);
        }
      }
      this.$emit('change', val);
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

    &.d-flex {
      .form-control {
        margin-left: 1.5rem;
        border: 0;
        background: rgba(#f6f2f0, 0.4);
        font-size: 1.5rem;
        font-weight: 300;
        padding: 0.5rem 1.75rem;
        border-bottom: 2px solid rgba($blue, 0.3);
        height: 4rem;

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

<template>
  <div class="form-group">
    <div class="custom-file">
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
  </div>
</template>

<script>
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
  },
  data() {
    const fileName =
      (this.value && this.value.file && this.value.file.name) ||
      (this.value && this.value.name) ||
      null;
    return {
      fileName,
    };
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
        letter-spacing: 0.2em;

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
}
</style>

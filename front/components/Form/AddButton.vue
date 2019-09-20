<template>
  <div class="form-group">
    <button :class="['btn', 'btn-outline-primary', 'btn-form']">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="1.1 1.1 97.8 97.8">
        <path
          d="M74.4 98.9H25.6c-13.5 0-24.5-11-24.5-24.5V25.6c0-13.5 11-24.5 24.5-24.5h48.8c13.5 0 24.5 11 24.5 24.5v48.8c0 13.5-11 24.5-24.5 24.5zM25.6 5.6c-11 0-20 9-20 20v48.8c0 11 9 20 20 20h48.8c11 0 20-9 20-20V25.6c0-11-9-20-20-20H25.6z"
        />
        <path
          d="M73.3 47.8H53V27.6c0-1.4-1.1-2.5-2.5-2.5S48 26.2 48 27.6v20.3H27.8c-1.4 0-2.5 1.1-2.5 2.5s1.1 2.5 2.5 2.5H48v20.3c0 1.4 1.1 2.5 2.5 2.5s2.5-1.1 2.5-2.5V52.8h20.3c1.4 0 2.5-1.1 2.5-2.5s-1.1-2.5-2.5-2.5z"
        />
      </svg>
      <div class="text">
        <span>{{ text }}</span>
      </div>
    </button>
  </div>
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
.form-group {
  margin-bottom: 3rem;

  @include media-breakpoint-down(sm) {
    margin-bottom: 1.5rem;
  }

  .btn-form {
    display: flex;
    flex-direction: row;
    align-items: center;
    border-width: 2px;
    border-radius: 0.41em;
    font-weight: 700;
    font-size: 1.5rem;
    color: $body-color;
    width: auto;
    max-width: 100%;
    height: 5rem;
    padding: 0 1.5rem 0 0;
    text-align: left;

    @include media-breakpoint-down(sm) {
      font-size: 1rem;
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
    }

    &:hover,
    &:active {
      svg {
        fill: $body-color;
      }
    }
  }
}
</style>

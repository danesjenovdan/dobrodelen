<template>
  <div class="form-group">
    <button
      :class="['btn', 'btn-outline-warning', 'btn-form']"
      @click="onClick"
    >
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="8.13 4.1 83.72 91.79">
        <path
          d="M75.69 7a8.46 8.46 0 00-9.18-2.42L27.68 18.09c-2 .61-3.86 2.45-5.5 4.08a2.71 2.71 0 00-.24.27L10.5 37.77l-.08.11a13.6 13.6 0 00-1.26 12.73 131.1 131.1 0 004.32 8.63l1.39 2.66A20.88 20.88 0 1052 75v-1.3l20.05-10.34a14.66 14.66 0 005.41-4.66 2.42 2.42 0 00.17-.28c2.56-4.83 10.16-19.76 13.3-26A8.45 8.45 0 0089.75 23zM31.1 90.9a15.89 15.89 0 110-31.77h.16l-1.07.57a12.47 12.47 0 00-6.45 7.41 11.57 11.57 0 00.86 9.07 10.37 10.37 0 009.14 5.69 9.94 9.94 0 004.64-1.16l8.55-4.4A15.9 15.9 0 0131.1 90.9zM33.64 51a3.49 3.49 0 01.66-4l3.86-3.85a4.53 4.53 0 013.19-1.31 4.44 4.44 0 01.62 0l1.94.27a3.5 3.5 0 012.55 5.2L44 51.58a4.48 4.48 0 01-1.81 1.75l-3.93 2.08a20.73 20.73 0 00-2.87-.84zm52.84-20.8C83.37 36.32 75.92 51 73.3 55.92a9.58 9.58 0 01-3.51 3L36.06 76.28A5.17 5.17 0 0129 73.82a6.64 6.64 0 01-.5-5.21 7.55 7.55 0 014-4.46l12.09-6.4a9.48 9.48 0 003.81-3.7l2.43-4.27a8.5 8.5 0 00-6.2-12.62l-1.94-.27a9.43 9.43 0 00-1.31-.09 9.56 9.56 0 00-6.73 2.77l-3.86 3.85a8.49 8.49 0 00-1.6 9.82l.47.93-.58.06h-.16a20.48 20.48 0 00-10.34 3.9l-.65-1.23c-1.9-3.63-3.54-6.76-4.11-8.19a8.63 8.63 0 01.76-8l11.26-15.12c1-1 2.51-2.49 3.29-2.71h.14L68.15 9.29a3.48 3.48 0 013.78 1L86 26.32a3.48 3.48 0 01.48 3.88z"
        />
      </svg>
      <div class="text">
        <span>{{ text }}</span>
      </div>
    </button>
    <!-- <div class="small text-right mr-2">
      Donacije omogočata
      <a href="https://example.com/" target="_blank" rel="noopener noreferrer"
        >XX</a
      >
      in
      <a href="https://example.com/" target="_blank" rel="noopener noreferrer"
        >YY</a
      >
    </div> -->
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
  methods: {
    onClick() {
      alert('Direktne donacije so še zaenkrat onemogočene!');
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
      fill: $yellow;
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

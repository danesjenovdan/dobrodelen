<template>
  <div class="row button-row">
    <div class="col-6">
      <div v-if="page >= 0" class="prev-button float-left">
        <button
          class="btn btn-primary"
          :disabled="disabled"
          @click="$emit('change', false, page - 1)"
        >
          Nazaj
        </button>
      </div>
    </div>
    <div class="col-6">
      <div v-if="page < pages" class="next-button float-right">
        <button
          class="btn btn-primary"
          :disabled="disabled"
          @click="$emit('change', true, page + 1)"
        >
          <template v-if="page < pages - 1">Naprej</template>
          <template v-else>Oddaj</template>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    page: {
      type: Number,
      required: true,
    },
    pages: {
      type: Number,
      required: true,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="scss" scoped>
.button-row {
  margin-top: 4rem;
  margin-bottom: 4rem;

  .prev-button,
  .next-button {
    .btn {
      color: inherit;
      height: 5rem;
      padding: 0 2.5rem;
      font-weight: 700;
      font-size: 1.5rem;
      color: #383838;
      letter-spacing: 0.2em;
      border-radius: 0.41em;

      @include media-breakpoint-down(sm) {
        font-size: 1rem;
        height: 3.5rem;
        padding: 0 1.5rem;
      }
    }
  }
}
</style>

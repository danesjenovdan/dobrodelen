<template>
  <div class="jumbotron">
    <div class="row justify-content-center">
      <div class="col-10 text-center">
        <p v-if="lead" class="lead" v-text="lead" />
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-12 col-md-7 text-center">
        <p v-if="text" class="text" v-text="text" />
        <div v-if="icon" :class="`icon icon-${icon} mt-4`" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    lead: {
      type: String,
      default: null,
    },
    text: {
      type: String,
      default: null,
    },
    icon: {
      type: String,
      default: null,
    },
  },
};
</script>

<style lang="scss" scoped>
.jumbotron {
  background: transparent;
  padding: 5rem 2rem 5rem;

  @include media-breakpoint-down(sm) {
    padding: 1rem 0;
    margin-bottom: 1rem;
  }

  p.lead {
    font-size: 3.1rem;
    line-height: 1.25;
    letter-spacing: 0.2em;
    margin: 0;

    @include media-breakpoint-down(sm) {
      font-size: 1.5rem;
    }
  }

  p.text {
    font-size: 1.5rem;
    line-height: 1.4;
    color: #696969;
    font-weight: 300;
    margin-top: 2rem;
  }

  .icon {
    width: 13rem;
    height: 13rem;

    @include media-breakpoint-down(sm) {
      width: 7rem;
      height: 7rem;
    }
  }
}
</style>

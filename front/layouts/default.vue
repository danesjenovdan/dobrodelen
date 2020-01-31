<template>
  <div>
    <div class="container-fluid">
      <div class="page">
        <page-header />
        <nuxt />
      </div>
    </div>
    <footer class="footer">
      <div class="row">
        <div class="col-12 col-sm-auto text-center">
          <a
            href="https://www.cnvos.si/"
            target="_blank"
            rel="noopener"
            class="mr-4"
          >
            <img
              src="/img/cnvos-logo-hires-text.png"
              alt="cvnos logo"
              class="cnvos-logo"
            />
          </a>
        </div>
        <div class="col d-flex align-items-center">
          <div class="my-3 my-md-0">
            K nastanku spletnega mesta Dobrodelen.si sta pripomogla Ministrstvo
            za javno upravo Republike Slovenije ter U.S. Embassy Ljubljana
          </div>
        </div>
        <div class="col-12 col-md-12 col-lg-auto text-center mt-3 mt-lg-0">
          <a
            href="https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-javno-upravo/"
            target="_blank"
            rel="noopener"
          >
            <img
              src="/img/Ministrstvo_za_javno_upravo_.png"
              alt="mju logo"
              class="mju-logo"
            />
          </a>
          <a href="https://si.usembassy.gov/" target="_blank" rel="noopener">
            <img
              src="/img/usembassy.png"
              alt="us embassy logo"
              class="use-logo"
            />
          </a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import PageHeader from '~/components/PageHeader.vue';

export default {
  components: {
    PageHeader,
  },
  watch: {
    $route() {
      this.$nuxt.$emit('toggle-menu', false);
    },
  },
};
</script>

<style lang="scss" scoped>
.container-fluid {
  padding-left: 3.5rem;
  padding-right: 3.5rem;
  max-width: 1920px;

  @include media-breakpoint-down(sm) {
    padding: 0 1rem;
  }
}

.footer {
  background-color: rgba($blue, 0.1);
  padding: 2rem 3.5rem;

  @include media-breakpoint-down(sm) {
    padding: 1rem 1rem;
  }

  .cnvos-logo {
    height: 70px;
  }

  .mju-logo {
    mix-blend-mode: multiply;
    margin-right: 0.5rem;
    width: 300px;

    @include media-breakpoint-down(xs) {
      width: 200px;
    }
  }

  .use-logo {
    height: 70px;

    @include media-breakpoint-down(xs) {
      height: 50px;
    }
  }
}
</style>

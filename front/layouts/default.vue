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
        <div class="col-12 d-flex flex-wrap">
          <figure>
            <img src="/img/flag_yellow_low.jpg" alt="" />
            <figcaption>Проектот е финансиран од Европската Унија.</figcaption>
          </figure>
          <figure>
            <img src="/img/Logo_EU_so_TEBE_MK.png" alt="" />
          </figure>
          <figure>
            <img src="/img/MCMS_Dolgo.jpg" alt="" class="blend-logo" />
          </figure>
          <figure>
            <img src="/img/LOGOTIP_ANG_1.jpg" alt="" class="blend-logo" />
          </figure>
          <figure>
            <img src="/img/bcsdn-horizontal-FINAL.png" alt="" />
          </figure>
        </div>
        <div class="col-12 text-center">
          Оваа веб страна е подготвена со помош на Европската Унија. Самата
          содржина на веб страна е единствена одговорност на имплементаторите и
          во никој случај не може да се смета дека ги одразува ставовите на
          Европската Унија.
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

  figure {
    flex: 1;
    text-align: center;
    max-width: 100%;

    @include media-breakpoint-down(sm) {
      flex-basis: 100%;
      margin: 1rem 0;
    }

    img {
      display: block;
      margin: 0 auto;
      height: 80px;

      @include media-breakpoint-down(sm) {
        height: 60px;
      }

      &.blend-logo {
        mix-blend-mode: multiply;
      }
    }
  }
}
</style>

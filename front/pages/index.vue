<template>
  <div class="content">
    <div class="row">
      <div class="col-12 col-lg-8">
        <h1 class="text-warning">
          <striped-text-shadow text="DOBRODELEN.SI" />
        </h1>
        <div class="icon-container-sm d-lg-none">
          <div class="icon icon-heart" />
        </div>
        <p class="lead mt-3">
          <strong>Doniraj pametno.</strong>
          Pomagaj si z našim nepristranskim sistemom razvrščanja organizacij,
          poišči zaupanja vredne organizacije in jih podpri.
        </p>
        <p class="mt-4">
          Metodologija za pregled transparentnosti slovenskih nevladnih
          organizacij temelji na 23-ih kriterijih, ki se nanašajo na 5 sklopov –
          Osnovne informacije o organizaciji; Dostopnost vsebinskih poročil;
          Finančna transparentnost; Zbiranje donacijskih sredstev in Dostopnost
          objavljenih informacij.
        </p>
        <nuxt-link :to="{ name: 'organizacije' }" class="btn btn-warning mt-5">
          <span>VSTOPI</span>
        </nuxt-link>
      </div>
      <div class="col-12 col-lg-4 d-none d-lg-block">
        <div class="icon icon-heart" />
      </div>
    </div>
  </div>
</template>

<script>
import StripedTextShadow from '~/components/StripedTextShadow.vue';

definePageMeta({ layout: 'landing' })

export default {
  components: {
    StripedTextShadow,
  },
};
</script>

<style lang="scss" scoped>
.content {
  width: 100%;

  h1 {
    font-size: 6rem;
    font-weight: 900;
    letter-spacing: 0.2em;

    @include media-breakpoint-down(lg) {
      font-size: 4rem;
    }

    @include media-breakpoint-down(md) {
      font-size: 2rem;
      word-break: break-all;
      text-align: center;
      margin-bottom: 1rem;
    }
  }

  p {
    font-size: 1.5rem;
    font-weight: 300;
    line-height: 1.3;
    color: #696969;
    margin-right: 12rem;

    @include media-breakpoint-down(md) {
      font-size: 1rem;
      margin-right: 0;
      text-align: center;
    }

    &.lead {
      font-size: 2.5rem;
      letter-spacing: 0.2em;
      line-height: 1.4;
      color: inherit;
      margin-right: 0;

      @include media-breakpoint-down(md) {
        font-size: 1.25rem;
        text-align: center;
      }
    }

    strong {
      font-weight: 600;
    }
  }

  .btn {
    font-size: 2.5rem;
    font-weight: 700;
    padding: 0.75rem 4rem;
    letter-spacing: 0.2em;

    @include media-breakpoint-down(md) {
      font-size: 1.25rem;
      display: block;
      margin: 0 auto;
      width: min-content;
    }
  }

  .icon {
    width: 100%;
    height: 100%;
    background-position: top 2rem center;

    @include media-breakpoint-down(xxl) {
      margin-top: 7rem;
    }
  }

  .icon-container-sm {
    height: 8rem;
    margin: 2rem 0;

    .icon {
      width: 100%;
      height: 100%;
      background-position: center;
      margin-top: 0;
    }
  }
}
</style>

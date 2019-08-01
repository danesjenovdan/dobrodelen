<template>
  <div class="content">
    <div class="row">
      <div class="col-8">
        <h1 class="text-warning">
          <striped-text-shadow text="DOBRODELEN.SI" />
        </h1>
        <p class="lead mt-3">
          <strong>Doniraj pametno.</strong>
          Pomagaj si z našim nepristranskim sistemom razvrščanja organizacij, poišči zaupanja vredne
          organizacije in jih podpri.
        </p>
        <p class="mt-4">
          Metodologija razvrščanja in ocenjevanja slovenskih nevladnih organizacij temelji na 25
          kriterijih, ki se nanašajo na 4 področja – nadzor nad poslovanjem; strateško načrtovanje;
          finančno upravljanje in transparentnost.
        </p>
        <nuxt-link :to="{ name: 'organizations' }" class="btn btn-warning mt-5">VSTOPI</nuxt-link>
      </div>
      <div class="col-4">
        <div class="icon icon-heart" />
      </div>
    </div>
  </div>
</template>

<script>
import StripedTextShadow from '~/components/StripedTextShadow.vue';

export default {
  layout: 'landing',
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
  }

  p {
    font-size: 1.5rem;
    font-weight: 300;
    line-height: 1.3;
    color: #696969;
    margin-right: 12rem;

    &.lead {
      font-size: 2.5rem;
      letter-spacing: 0.2em;
      line-height: 1.4;
      color: #383838;
      margin-right: 0;
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
  }

  .icon {
    width: 100%;
    height: 100%;
    background-position: top 2rem center;
  }
}
</style>

<template>
  <div class="row">
    <div class="col-12">
      <div class="content-title-container text-center">
        <div class="embed-responsive embed-responsive-1by1">
          <div class="embed-responsive-item">
            <div class="img-container" v-if="image">
              <img :src="image" alt="title image" />
            </div>
            <div
              v-else-if="icon"
              class="rounded-circle icon-container bg-warning"
            >
              <i :class="['icon', `icon-${icon}`]" />
            </div>
          </div>
        </div>

        <h2>{{ title }}</h2>
        <div v-if="stars > -1" class="stars" @click="$emit('stars-click')">
          <i
            v-for="i in 5"
            :key="i"
            :class="['icon', 'icon-star', { 'icon-star--full': stars >= i }]"
          />
        </div>
        <div v-if="donation" class="org-donate">
          <donate-button
            text="Doniraj organizaciji"
            @click="$emit('donate-click')"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DonateButton from '~/components/Form/DonateButton.vue';

export default {
  components: {
    DonateButton,
  },
  props: {
    image: {
      type: String,
      default: null,
    },
    icon: {
      type: String,
      default: null,
    },
    title: {
      type: String,
      required: true,
    },
    stars: {
      type: Number,
      default: -1,
    },
    donation: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="scss" scoped>
.content-title-container {
  background: #f6f2f0;
  padding: 2.5rem 4.2rem;
  margin-bottom: 5rem;

  @include media-breakpoint-down(sm) {
    padding: 1rem;
    margin-bottom: 2rem;
  }

  .embed-responsive {
    max-width: 179px;
    height: 179px; // Chrome bug fix
    display: inline-block;
    margin-bottom: 1.5rem;

    @include media-breakpoint-down(sm) {
      max-width: 6rem;
      margin-bottom: 1rem;
    }

    .img-container {
      width: 100%;
      height: 100%;
      background: white;
      padding: 16px;

      img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: contain;
        object-position: center;
      }
    }

    .icon-container {
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;

      .icon {
        width: 4.5rem;
        height: 4.5rem;

        @include media-breakpoint-down(sm) {
          width: 2.7rem;
          height: 2.7rem;
        }
      }
    }
  }

  h2 {
    font-size: 3rem;
    font-weight: 300;
    line-height: 1.4;
    letter-spacing: 0.2em;

    @include media-breakpoint-down(sm) {
      font-size: 1.5rem;
    }
  }

  .stars {
    display: inline-block;
    margin-top: 1.5rem;
    cursor: pointer;

    @include media-breakpoint-down(sm) {
      margin-top: 0.5rem;
    }

    .icon {
      margin: 0 0.3rem;

      @include media-breakpoint-down(sm) {
        width: 1.5rem;
        height: 1.5rem;
      }
    }
  }

  .org-donate {
    display: flex;
    justify-content: center;
    margin-top: 1.5rem;

    .form-group {
      margin-bottom: 0;
    }
  }
}
</style>

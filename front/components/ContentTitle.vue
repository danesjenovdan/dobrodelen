<template>
  <div class="row">
    <div class="col-12">
      <div class="content-title-container text-center">
        <div class="embed-responsive embed-responsive-1by1 mb-4">
          <div class="embed-responsive-item">
            <img v-if="image" :src="image" alt="title image" class="rounded-circle bg-dark" />
            <div v-else-if="icon" class="rounded-circle icon-container bg-warning">
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
      </div>
    </div>
  </div>
</template>

<script>
export default {
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
  },
};
</script>

<style lang="scss" scoped>
.content-title-container {
  background: #f6f2f0;
  padding: 2.5rem 4.2rem;
  margin-bottom: 5rem;

  .embed-responsive {
    max-width: 10rem;
    display: inline-block;

    img {
      display: block;
      width: 100%;
      height: 100%;
      object-fit: contain;
      object-position: center;
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
      }
    }
  }

  h2 {
    font-size: 3rem;
    font-weight: 300;
    line-height: 1.4;
    letter-spacing: 0.2em;
  }

  .stars {
    display: inline-block;
    margin-top: 1.5rem;
    cursor: pointer;

    .icon {
      margin: 0 0.3rem;
    }
  }
}
</style>
